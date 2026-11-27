"""Pack filled tables of a dataflow into zip files ready to upload on the Reportnet 3 portal.

    python reference/schema/package.py <dataflow> <input> <out-dir> [options]
    python reference/schema/package.py --check

<dataflow> is Article23 or SpatialPoints. <input> holds the filled tables, either

* a folder with one CSV per table, named after the table (Measure.csv), UTF-8, with a header row;
  or
* a template database made by template.py (.sqlite or .gpkg), with its tables filled.

<out-dir> receives one zip per Reportnet 3 dataset of the dataflow that has a filled table
(Article23_DescriptiveDataset.zip, SpatialPoints.zip...), replacing those of an earlier run, and
manifest.json, which says what was packed, from which version of the specification, and what is
left to check.

Each zip holds one CSV per filled table, named after the table, whose header is exactly the
table's fields in the order of reference/schema/<dataflow>/<table>.csv. On the way:

* a column missing from the input is added empty (a warning if the field is Required);
* a column whose name differs only in case is renamed; any other unknown column is an error;
* values are trimmed; a date with a midnight time loses the time;
* several values of a field ([0..n], [1..n]) are joined with the separator (a comma);
* a point geometry, given as a GeoJSON Feature, a GeoJSON geometry, WKT, EWKT (SRID=4326;POINT
  (...)) or a GeoPackage geometry, is written as the GeoJSON Feature that Reportnet 3 stores, with
  its SRID in properties.srid. A value without SRID takes --srid, which must be 4258 or 4326.

Anything it cannot convert is an error: then it writes nothing and exits with status 1. It does
not check code values, keys or conditions: run validate.py first.

Options:
  --delimiter C          field delimiter of the CSV files written (default ,)
  --multi-separator S    separator between several values of one field (default ,)
  --srid N               SRID of geometries that carry none: 4258 or 4326

--check packs header-only zips of both dataflows in a temporary folder, reads them back, and
tests the geometry conversion.

Standard library only.
"""

import argparse
import contextlib
import csv
import io
import json
import re
import sqlite3
import struct
import sys
import tempfile
import zipfile
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from template import REPO, SCHEMA, FILES, build, commit, read  # noqa: E402

SRIDS = ('4258', '4326')


class Problems:
    def __init__(self):
        self.errors, self.warnings = [], []

    def error(self, where, text):
        self.errors.append(f'{where}: {text}')

    def warn(self, where, text):
        self.warnings.append(f'{where}: {text}')


# --- Geometry -------------------------------------------------------------------------------------

def gpkg_point(blob):
    """(x, y, srid) of a GeoPackage point geometry."""
    if blob[:2] != b'GP':
        raise ValueError('not a GeoPackage geometry')
    flags = blob[3]
    order = '<' if flags & 1 else '>'
    srid = struct.unpack(order + 'i', blob[4:8])[0]
    envelope = {0: 0, 1: 32, 2: 48, 3: 48, 4: 64}.get((flags >> 1) & 7)
    if envelope is None:
        raise ValueError('bad envelope')
    if flags & 16:
        raise ValueError('empty geometry')
    wkb = blob[8 + envelope:]
    worder = '<' if wkb[0] == 1 else '>'
    kind = struct.unpack(worder + 'I', wkb[1:5])[0]
    if kind != 1:
        raise ValueError(f'WKB type {kind} is not a 2D point')
    x, y = struct.unpack(worder + 'dd', wkb[5:21])
    return x, y, str(srid) if srid > 0 else None


def point(value, srid):
    """The GeoJSON Feature, as text, of a point given in one of the accepted forms."""
    if isinstance(value, bytes):
        x, y, own = gpkg_point(value)
    else:
        text = value.strip()
        own = None
        m = re.fullmatch(r'SRID=(\d+);(.*)', text, re.S | re.I)
        if m:
            own, text = m.group(1), m.group(2).strip()
        if text.startswith('{'):
            obj = json.loads(text)
            if obj.get('type') == 'Feature':
                props = obj.get('properties') or {}
                if props.get('srid') is not None:
                    own = str(props['srid'])
                obj = obj.get('geometry') or {}
            elif obj.get('srid') is not None:
                own = str(obj['srid'])
            if obj.get('type') != 'Point':
                raise ValueError(f"geometry type {obj.get('type')} is not Point")
            coords = obj.get('coordinates') or []
            if len(coords) != 2:
                raise ValueError('a point needs two coordinates')
            x, y = (float(c) for c in coords)
        else:
            m = re.fullmatch(r'POINT\s*\(\s*(\S+)\s+(\S+)\s*\)', text, re.I)
            if not m:
                raise ValueError('not a 2D point in GeoJSON or WKT')
            x, y = float(m.group(1)), float(m.group(2))
    own = own or srid
    if not own:
        raise ValueError('no SRID: the value carries none and no --srid was given')
    if own not in SRIDS:
        raise ValueError(f'SRID {own} is not 4258 (ETRS89) or 4326 (WGS 84)')
    if not (-180 <= x <= 180 and -90 <= y <= 90):
        raise ValueError(f'({x}, {y}) is not longitude, latitude in degrees')
    return json.dumps({'type': 'Feature', 'geometry': {'type': 'Point', 'coordinates': [x, y]},
                       'properties': {'srid': own}}, separators=(',', ':'))


# --- Input ----------------------------------------------------------------------------------------

def read_folder(folder, tables, problems):
    """{table: (columns, rows)} from the CSV files of a folder."""
    found = {}
    for path in sorted(Path(folder).glob('*.csv')):
        if path.stem not in tables:
            problems.error(path.name, f'no table {path.stem} in this dataflow')
            continue
        with open(path, encoding='utf-8-sig', newline='') as f:
            rows = list(csv.reader(f))
        if not rows:
            problems.error(path.name, 'empty file, without a header')
            continue
        found[path.stem] = (rows[0], rows[1:])
    return found


def read_database(path, tables, problems):
    """{table: (columns, rows)} from the filled tables of a template database."""
    con = sqlite3.connect(f'file:{path}?mode=ro', uri=True)
    present = {r[0] for r in con.execute("SELECT name FROM sqlite_master WHERE type = 'table'")}
    found = {}
    for table in tables:
        if table not in present:
            continue
        cur = con.execute(f'SELECT * FROM "{table}"')
        columns = [c[0] for c in cur.description]
        rows = cur.fetchall()
        if 'fid' in columns:  # the GeoPackage's own key, not a field
            i = columns.index('fid')
            columns = columns[:i] + columns[i + 1:]
            rows = [r[:i] + r[i + 1:] for r in rows]
        if rows:
            found[table] = (columns, [list(r) for r in rows])
    con.close()
    return found


# --- Packing --------------------------------------------------------------------------------------

def cell(field, value, args, where, problems):
    """The text of one value, as written for Reportnet 3."""
    if value is None:
        return ''
    if field['type'] == 'point':
        if isinstance(value, str) and not value.strip():
            return ''
        try:
            return point(value, args.srid)
        except (ValueError, struct.error, json.JSONDecodeError) as e:
            problems.error(where, str(e))
            return ''
    if isinstance(value, bytes):
        problems.error(where, 'binary value')
        return ''
    if isinstance(value, float) and value.is_integer() and field['type'] in (
            'integer', 'nonNegativeInteger', 'gYear'):
        value = int(value)
    text = str(value).strip()
    if field['multiplicity']:
        parts = [p.strip() for p in text.split(',') if p.strip()]
        return args.multi_separator.join(parts)
    if field['type'] == 'date' and text:
        m = re.fullmatch(r'(\d{4}-\d{2}-\d{2})(?:[T ]00:00(?::00(?:\.0+)?)?(?:Z|[+-]00:?00)?)?', text)
        if not m:
            problems.error(where, f'{text!r} is not a date yyyy-mm-dd')
            return text
        return m.group(1)
    return text


def match_columns(table, columns, fields, problems):
    """{field: position in the input} of the input columns; an unknown column is an error."""
    names = [f['notation'] for f in fields]
    lower = {n.lower(): n for n in names}
    index = {}
    for i, c in enumerate(columns):
        c = (c or '').strip()
        name = c if c in names else lower.get(c.lower())
        if name is None:
            problems.error(f'{table}.{c}', 'not a field of the table')
        elif name in index:
            problems.error(f'{table}.{c}', 'given twice')
        else:
            if name != c:
                problems.warn(f'{table}.{c}', f'renamed {name}')
            index[name] = i
    return index


def dataflow_tables(dataflow):
    """({table: its first row in datasets.csv}, {table: its fields}) of a dataflow."""
    tables = {}
    for d in read(SCHEMA / 'datasets.csv'):
        if d['dataflow'] == dataflow:
            tables.setdefault(d['table'], d)
    return tables, {t: read(SCHEMA / dataflow / f'{t}.csv') for t in tables}


def read_input(source, tables, problems):
    """{table: (columns, rows)} from a folder of CSV files or a template database."""
    source = Path(source)
    if source.is_dir():
        return read_folder(source, tables, problems)
    if source.suffix in ('.sqlite', '.gpkg', '.db') and source.is_file():
        return read_database(source, tables, problems)
    sys.exit(f'{source}: neither a folder nor a .sqlite or .gpkg database')


def pack(dataflow, source, out_dir, args):
    tables, fields = dataflow_tables(dataflow)
    problems = Problems()
    source = Path(source)
    found = read_input(source, tables, problems)

    written = {}  # table: CSV text
    counts = {}
    for table, (columns, rows) in found.items():
        names = [f['notation'] for f in fields[table]]
        index = match_columns(table, columns, fields[table], problems)
        for f in fields[table]:
            if f['notation'] not in index and f['status'] == 'Required':
                problems.warn(f"{table}.{f['notation']}", 'Required, but no such column: added empty')
        buf = io.StringIO()
        out = csv.writer(buf, delimiter=args.delimiter, lineterminator='\r\n')
        out.writerow(names)
        n = 0
        for r, row in enumerate(rows, start=2):
            if len(row) > len(columns):
                problems.error(f'{table} row {r}', 'more values than columns')
            values = []
            for f in fields[table]:
                i = index.get(f['notation'])
                v = row[i] if i is not None and i < len(row) else None
                values.append(cell(f, v, args, f"{table}.{f['notation']} row {r}", problems))
            if any(values):
                out.writerow(values)
                n += 1
        written[table], counts[table] = buf.getvalue(), n

    for e in problems.errors:
        print('error:', e, file=sys.stderr)
    for w in problems.warnings:
        print('warning:', w, file=sys.stderr)
    if problems.errors:
        print(f'{len(problems.errors)} error(s): nothing written', file=sys.stderr)
        return 1
    if not written:
        print(f'{source}: no filled table of {dataflow}', file=sys.stderr)
        return 1

    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    version = {r['dataflow']: r for r in read(REPO / 'reference' / 'versions.csv')}.get(dataflow, {})
    zips = []
    for dataset in dict.fromkeys(d['dataset'] for d in tables.values()):  # none left from a last run
        (out_dir / (f'{dataflow}_{dataset}.zip' if dataset else f'{dataflow}.zip')).unlink(missing_ok=True)
    for dataset in dict.fromkeys(d['dataset'] for d in tables.values()):
        members = [t for t, d in tables.items() if d['dataset'] == dataset and t in written]
        if not members:
            continue
        name = f'{dataflow}_{dataset}.zip' if dataset else f'{dataflow}.zip'
        with zipfile.ZipFile(out_dir / name, 'w', zipfile.ZIP_DEFLATED) as z:
            for t in members:
                z.writestr(f'{t}.csv', written[t].encode('utf-8'))
        missing = [t for t, d in tables.items() if d['dataset'] == dataset and t not in written]
        zips.append({'file': name, 'dataset': dataset or dataflow,
                     'tables': {t: counts[t] for t in members}, 'tablesNotIncluded': missing})
        print(f'{name}: ' + ', '.join(f'{t} ({counts[t]})' for t in members))

    manifest = {
        'dataflow': dataflow,
        'specificationVersion': version.get('version', ''),
        'specificationStatus': version.get('status', ''),
        'commit': commit(),
        'made': datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        'source': source.name,
        'format': {'encoding': 'UTF-8', 'delimiter': args.delimiter,
                   'multiValueSeparator': args.multi_separator,
                   'geometry': 'GeoJSON Feature, SRID in properties.srid'},
        'zips': zips,
        'warnings': problems.warnings,
        'notChecked': 'Code values, keys, links between tables and conditions, unless validate.py '
                      'was run on the same input. The portal validation checks the conditions.',
        'upload': 'A person uploads each zip on the Reportnet 3 portal, into the dataset it is '
                  'named after, then checks the validation and releases the data.',
    }
    (out_dir / 'manifest.json').write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + '\n',
                                           encoding='utf-8')
    return 0


# --- Self-check -----------------------------------------------------------------------------------

def check():
    """Pack empty tables of both dataflows, read the zips back, and test the geometry."""
    args = argparse.Namespace(delimiter=',', multi_separator=',', srid=None)
    feature = '{"type":"Feature","geometry":{"type":"Point","coordinates":[10.5,50.25]},' \
              '"properties":{"srid":"4326"}}'
    for value, srid in [('POINT (10.5 50.25)', '4326'), ('SRID=4326;POINT(10.5 50.25)', None),
                        ('{"type":"Point","coordinates":[10.5,50.25]}', '4326'), (feature, None),
                        (b'GP\x00\x01' + struct.pack('<i', 4326) + b'\x01'
                         + struct.pack('<Idd', 1, 10.5, 50.25), None)]:
        got = point(value, srid)
        assert got == feature, (value, got)
    for value in ('POINT (10.5 50.25)', 'SRID=3035;POINT (10.5 50.25)', 'LINESTRING (0 0, 1 1)'):
        try:
            point(value, None)
        except ValueError:
            continue
        raise AssertionError(f'{value} accepted')

    with tempfile.TemporaryDirectory() as tmp:
        for dataflow in FILES:
            datasets = [d for d in read(SCHEMA / 'datasets.csv') if d['dataflow'] == dataflow]
            tables = list(dict.fromkeys(d['table'] for d in datasets))
            folder = Path(tmp) / dataflow / 'in'
            folder.mkdir(parents=True)
            for t in tables:  # one row with only the first field, to see the others added
                first = read(SCHEMA / dataflow / f'{t}.csv')[0]
                value = {'date': '2026-01-01 00:00:00', 'point': 'POINT (10.5 50.25)'}.get(first['type'], 'x')
                (folder / f'{t}.csv').write_text(f"{first['notation']}\n{value}\n", encoding='utf-8')
            out = Path(tmp) / dataflow / 'out'
            args.srid = '4326'
            with contextlib.redirect_stderr(io.StringIO()) as log:
                failed = pack(dataflow, folder, out, args)
            if failed:
                sys.exit(log.getvalue())
                raise SystemExit(f'{dataflow}: packing failed')
            seen = set()
            for z in sorted(out.glob('*.zip')):
                with zipfile.ZipFile(z) as f:
                    for member in f.namelist():
                        t = member[:-4]
                        header = next(csv.reader(io.StringIO(f.read(member).decode('utf-8'))))
                        expected = [r['notation'] for r in read(SCHEMA / dataflow / f'{t}.csv')]
                        assert header == expected, (z.name, member)
                        seen.add(t)
            assert seen == set(tables), (dataflow, set(tables) - seen)
            # An empty template database has nothing to pack
            db = build(dataflow, Path(tmp) / FILES[dataflow])
            with contextlib.redirect_stderr(io.StringIO()), contextlib.redirect_stdout(io.StringIO()):
                failed = pack(dataflow, db, Path(tmp) / dataflow / 'empty', args)
            if failed != 1:
                raise SystemExit(f'{dataflow}: an empty template should give nothing to pack')
            print(f'{dataflow}: {len(tables)} tables packed and read back')


def main():
    if sys.argv[1:] == ['--check']:
        check()
        return 0
    p = argparse.ArgumentParser(usage=__doc__)
    p.add_argument('dataflow', choices=list(FILES))
    p.add_argument('input')
    p.add_argument('out_dir')
    p.add_argument('--delimiter', default=',')
    p.add_argument('--multi-separator', default=',')
    p.add_argument('--srid', choices=SRIDS)
    args = p.parse_args()
    if len(args.delimiter) != 1:
        p.error('--delimiter must be one character')
    return pack(args.dataflow, args.input, args.out_dir, args)


if __name__ == '__main__':
    sys.exit(main())
