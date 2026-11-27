"""Make the files of a spatial points prefill release from a prefill baseline.

    python3 explorer/scripts/prefill_release.py <baseline folder> <output folder>

The baseline is the output folder of the spatial points prefill, built in the uwwtd repository
(dataflow/spatialpoints/prefill/output/), which is not in git. The output folder gets the files to attach to a GitHub release, which the
explorer downloads when it is built:

    agglomerations.parquet    one row per prefilled object, with its location as longitude and
    uwwtps.parquet            latitude, its fields as in the baseline, and what the prefill changed:
    discharge-points.parquet  the reported name, the reported location where it was corrected, and
                              the original code where it was converted
    flags.parquet             one row per object and failed quality check
    manifest.json             counts, provenance and the checksum of each file
    README.md                 what the release is, for the release notes

Python standard library, and the DuckDB command-line tool (duckdb) to write Parquet.
"""

import csv
import hashlib
import json
import shutil
import sqlite3
import struct
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

TABLES = {  # baseline table: release file
    'Agglomeration': 'agglomerations',
    'UWWTP': 'uwwtps',
    'DischargePoint': 'discharge-points',
}
EXTRA = ['reportedName', 'nameSteps', 'reportedLongitude', 'reportedLatitude', 'originalCode']
FLAG_COLUMNS = ['table', 'countryCode', 'thematicIdIdentifier', 'severity', 'check', 'detail']


def point(blob):
    """Longitude and latitude of a GeoPackage point geometry."""
    if blob is None:
        return None, None
    flags = blob[3]
    envelope = {0: 0, 1: 32, 2: 48, 3: 48, 4: 64}[(flags >> 1) & 7]
    wkb = blob[8 + envelope:]
    order = '<' if wkb[0] == 1 else '>'
    if struct.unpack(order + 'I', wkb[1:5])[0] % 1000 != 1:
        return None, None
    x, y = struct.unpack(order + 'dd', wkb[5:21])
    return (None, None) if x != x or y != y else (round(x, 6), round(y, 6))


def side_table(baseline, name, table, key='thematicIdIdentifier'):
    with open(baseline / name, encoding='utf-8', newline='') as f:
        return {r[key]: r for r in csv.DictReader(f) if r['table'] == table}


def to_parquet(source, target):
    query = (f"COPY (SELECT * FROM read_csv('{source}', header=true, auto_detect=true, "
             f"sample_size=-1)) TO '{target}' (FORMAT parquet, COMPRESSION zstd)")
    subprocess.run(['duckdb', '-c', query], check=True, capture_output=True)


def specification_version():
    versions = Path(__file__).resolve().parents[2] / 'reference' / 'versions.csv'
    with open(versions, encoding='utf-8', newline='') as f:
        row = {r['dataflow']: r for r in csv.DictReader(f)}['SpatialPoints']
    return f"spatialpoints-v{row['version']}"


def specification_fields(table):
    """The fields of a spatial points table in reference/schema, in their order."""
    path = Path(__file__).resolve().parents[2] / 'reference' / 'schema' / 'SpatialPoints' / f'{table}.csv'
    with open(path, encoding='utf-8', newline='') as f:
        return [r['notation'] for r in csv.DictReader(f)]


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main(baseline, out):
    baseline, out = Path(baseline), Path(out)
    gpkg = next(baseline.glob('*.gpkg'))
    source = json.loads((baseline / 'manifest.json').read_text(encoding='utf-8'))
    out.mkdir(parents=True, exist_ok=True)
    counts, differences = {}, {}
    con = sqlite3.connect(f'file:{gpkg}?mode=ro', uri=True)
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        for table, name in TABLES.items():
            names = side_table(baseline, 'name_cleaning.csv', table)
            moved = side_table(baseline, 'coordinate_corrections.csv', table)
            codes = side_table(baseline, 'code_conversion.csv', table)
            cursor = con.execute(f'select * from "{table}" order by thematicIdIdentifier')
            columns = [c[0] for c in cursor.description]
            fields = [c for c in columns if c not in ('fid', 'geometry')]
            spec = [c for c in specification_fields(table) if c != 'geometry']
            if fields != spec:
                differences[table] = {'notInSpecification': [c for c in fields if c not in spec],
                                      'notInBaseline': [c for c in spec if c not in fields]}
            with open(tmp / f'{name}.csv', 'w', encoding='utf-8', newline='') as f:
                w = csv.writer(f, lineterminator='\n')
                w.writerow(['countryCode', 'longitude', 'latitude', *fields, *EXTRA])
                n = 0
                for row in cursor:
                    r = dict(zip(columns, row))
                    code = r['thematicIdIdentifier']
                    nm, mv, cc = names.get(code, {}), moved.get(code, {}), codes.get(code, {})
                    lon, lat = point(r['geometry'])
                    w.writerow([nm.get('countryCode') or code[:2], lon, lat, *(r[c] for c in fields),
                                nm.get('reportedName', ''), nm.get('steps', ''),
                                mv.get('reportedLongitude', ''), mv.get('reportedLatitude', ''),
                                cc.get('originalCode', '')])
                    n += 1
            counts[name] = n
            to_parquet(tmp / f'{name}.csv', out / f'{name}.parquet')
        with open(baseline / 'qc_flags.csv', encoding='utf-8', newline='') as f, \
                open(tmp / 'flags.csv', 'w', encoding='utf-8', newline='') as g:
            w = csv.writer(g, lineterminator='\n')
            w.writerow(FLAG_COLUMNS)
            n = 0
            for r in csv.DictReader(f):
                w.writerow([r[c] for c in FLAG_COLUMNS])
                n += 1
        counts['flags'] = n
        to_parquet(tmp / 'flags.csv', out / 'flags.parquet')

    files = {p.name: {'bytes': p.stat().st_size, 'sha256': sha256(p)} for p in sorted(out.glob('*.parquet'))}
    manifest = {
        'title': f"rUWWTD spatial points prefill, reference year {source['reference_year']}",
        'reference_year': source['reference_year'],
        'release_status': source['release_status'],
        'note': ('Provisional and under development. Prefilled from the reporting under Directive '
                 '91/271/EEC, which is under Member State review. Not an EEA publication.'),
        # what the data comes from, without the paths of the machine the baseline was made on
        'source': {k: v for k, v in source['source'].items() if k in ('name', 'file', 'files', 'sha256', 'pinned')}
                  | {'name': source['source']['name'].split(': ', 1)[-1]},
        'baseline_made': source.get('created'),
        # the version of the spatial points specification when the release is made, and whether
        # the fields of the baseline are those of reference/schema/SpatialPoints
        'specification_version': specification_version(),
        'fields': (f'As in specification {specification_version()}.' if not differences
                   else {'note': f'Not as in specification {specification_version()}.', **differences}),
        'release_made': datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        'rows': counts,
        'files': files,
    }
    (out / 'manifest.json').write_text(json.dumps(manifest, indent=1, ensure_ascii=False) + '\n',
                                       encoding='utf-8')
    shutil.copy(Path(__file__).with_name('prefill_release_README.md'), out / 'README.md')
    print(json.dumps(counts))
    if differences:
        print('The fields differ from the specification:', json.dumps(differences), file=sys.stderr)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(*sys.argv[1:])
