"""Make an empty template database of a dataflow from the CSV files of reference/.

    python reference/schema/template.py <dataflow> <file>    # Article23 or SpatialPoints
    python reference/schema/template.py --check              # build both and check them

A template has, for one dataflow:

* one empty table per reporting table of datasets.csv, with its fields in order, NOT NULL for the
  Required ones, the key the documentation states, and CHECK constraints derived from the types;
* one table per code list, cl_<Type>, filled from reference/codelist; a field of that type has a
  foreign key to it (a field with several values, [0..n], keeps them as text, separated by commas);
* foreign keys between reporting tables where a field holds the key of another table of the
  dataflow, such as measureCode in MeasureFinancing;
* Metadata: the tables and fields, in the layout of the Metadata table of the Water Framework
  Directive documentation (tableName, columnName, columnPosition, columnDataType, multiplicity,
  description, objectType, dataflowCode), with the label, status, condition, unit and link to the
  documentation added;
* _about: the dataflow, the version of the files it was made from, and how to use it.

The spatial points template is a GeoPackage: its tables have a point geometry in ETRS89
(EPSG:4258), and it opens in QGIS. The Article 23 template is a plain SQLite database.

SQLite checks foreign keys only when asked, on each connection: PRAGMA foreign_keys = ON.
Conditions ("Required if ...") are not enforced: they are left to the quality checks.

Standard library only.
"""

import csv
import os
import re
import sqlite3
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SCHEMA = REPO / 'reference' / 'schema'
CODELIST = REPO / 'reference' / 'codelist'
DOCS_URL = 'https://eeadata.github.io/WISE.UWWTD.Documentation/'
FILES = {'Article23': 'rUWWTD_Article23_template.sqlite',
         'SpatialPoints': 'rUWWTD_SpatialPoints_template.gpkg'}

ETRS89 = ('GEOGCS["ETRS89",DATUM["European_Terrestrial_Reference_System_1989",SPHEROID["GRS 1980",'
          '6378137,298.257222101,AUTHORITY["EPSG","7019"]],AUTHORITY["EPSG","6258"]],PRIMEM["Greenwich",0,'
          'AUTHORITY["EPSG","8901"]],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]],'
          'AUTHORITY["EPSG","4258"]]')
WGS84 = ('GEOGCS["WGS 84",DATUM["WGS_1984",SPHEROID["WGS 84",6378137,298.257223563,AUTHORITY["EPSG","7030"]],'
         'AUTHORITY["EPSG","6326"]],PRIMEM["Greenwich",0,AUTHORITY["EPSG","8901"]],UNIT["degree",'
         '0.0174532925199433,AUTHORITY["EPSG","9122"]],AUTHORITY["EPSG","4326"]]')


def read(path):
    with open(path, encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))


def q(name):
    return '"' + name.replace('"', '""') + '"'


def column_sql(field, codelists, external_lengths):
    """SQL type and CHECK constraints of a field, from its type."""
    name, typ, many = q(field['notation']), field['type'], bool(field['multiplicity'])
    if many:  # several values, separated by commas, as reported
        return 'TEXT', []
    m = re.fullmatch(r'string(\d*)', typ)
    if m:
        return 'TEXT', [f'length({name}) <= {m.group(1) or 4000}']
    if typ in ('wiseIdentifier', 'documentCode', 'referenceCode'):
        return 'TEXT', [f'length({name}) <= 42']
    if typ in codelists:
        return 'TEXT', []
    if typ in external_lengths:
        return 'TEXT', [f'length({name}) = {external_lengths[typ]}'] if external_lengths[typ] else []
    return {
        'date': ('DATE', [f'{name} IS date({name})']),
        'gYear': ('INTEGER', [f"typeof({name}) = 'integer' AND {name} BETWEEN 1000 AND 9999"]),
        'integer': ('INTEGER', [f"typeof({name}) = 'integer'"]),
        'nonNegativeInteger': ('INTEGER', [f"typeof({name}) = 'integer' AND {name} >= 0"]),
        'nonNegativeValue': ('REAL', [f'{name} >= 0']),
        'Percentage': ('REAL', [f'{name} BETWEEN 0 AND 100']),
        'range': ('TEXT', [f"{name} GLOB '[[(]*,*[])]'"]),
        'Email': ('TEXT', [f'length({name}) <= 250', f"{name} LIKE '%_@_%'"]),
        'URL': ('TEXT', [f'length({name}) <= 2100', f"{name} LIKE 'http%'"]),
        'url': ('TEXT', [f"{name} LIKE 'http%'"]),
        'Attachment': ('BLOB', []),
    }[typ]


def metadata_type(field):
    """columnDataType as in the WFD Metadata table: string(254), date, a code list name..."""
    m = re.fullmatch(r'string(\d+)', field['type'])
    return f'string({m.group(1)})' if m else field['type']


def multiplicity(field):
    if field['multiplicity']:
        return f"[{field['multiplicity']}]"
    return '[1]' if field['status'] == 'Required' else '[0..1]'


def commit():
    sha = os.environ.get('GITHUB_SHA')
    if sha:
        return sha
    try:
        return subprocess.run(['git', '-C', str(REPO), 'rev-parse', 'HEAD'], capture_output=True,
                              text=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return ''


def build(dataflow, path):
    path = Path(path)
    if path.exists():
        path.unlink()
    geopackage = path.suffix == '.gpkg'
    datasets = [d for d in read(SCHEMA / 'datasets.csv') if d['dataflow'] == dataflow]
    tables = {}  # table: its row in datasets.csv (the first, for a table shown in parts)
    for d in datasets:
        tables.setdefault(d['table'], d)
    fields = {t: read(SCHEMA / dataflow / f'{t}.csv') for t in tables}
    index = read(CODELIST / 'codelists.csv')
    codelists = {c['type']: c for c in index}
    types = {t['type']: t for t in read(SCHEMA / 'types.csv')}
    external_lengths = {'Language': 3, 'ZoneType': 0}
    # A field that holds the single-field key of another table refers to that table. A key name
    # shared by several tables, such as thematicIdIdentifier, says nothing about which one.
    single = [d['primaryKey'] for d in tables.values() if d['primaryKey'] and ' ' not in d['primaryKey']]
    keys = {d['primaryKey']: t for t, d in tables.items() if d['primaryKey'] in single and single.count(d['primaryKey']) == 1}
    keys.setdefault('documentCode', 'Document' if 'Document' in tables else None)
    keys.setdefault('referenceCode', 'Reference' if 'Reference' in tables else None)

    con = sqlite3.connect(path)
    con.execute('PRAGMA foreign_keys = ON')
    if geopackage:
        con.execute('PRAGMA application_id = 1196444487')  # 'GPKG'
        con.execute('PRAGMA user_version = 10400')
        con.executescript('''
            CREATE TABLE gpkg_spatial_ref_sys (srs_name TEXT NOT NULL, srs_id INTEGER PRIMARY KEY,
              organization TEXT NOT NULL, organization_coordsys_id INTEGER NOT NULL,
              definition TEXT NOT NULL, description TEXT);
            CREATE TABLE gpkg_contents (table_name TEXT NOT NULL PRIMARY KEY, data_type TEXT NOT NULL,
              identifier TEXT UNIQUE, description TEXT DEFAULT '',
              last_change DATETIME NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now')),
              min_x DOUBLE, min_y DOUBLE, max_x DOUBLE, max_y DOUBLE, srs_id INTEGER,
              CONSTRAINT fk_gc_r_srs_id FOREIGN KEY (srs_id) REFERENCES gpkg_spatial_ref_sys(srs_id));
            CREATE TABLE gpkg_geometry_columns (table_name TEXT NOT NULL, column_name TEXT NOT NULL,
              geometry_type_name TEXT NOT NULL, srs_id INTEGER NOT NULL, z TINYINT NOT NULL,
              m TINYINT NOT NULL, CONSTRAINT pk_geom_cols PRIMARY KEY (table_name, column_name),
              CONSTRAINT fk_gc_tn FOREIGN KEY (table_name) REFERENCES gpkg_contents(table_name),
              CONSTRAINT fk_gc_srs FOREIGN KEY (srs_id) REFERENCES gpkg_spatial_ref_sys(srs_id));
        ''')
        con.executemany('INSERT INTO gpkg_spatial_ref_sys VALUES (?, ?, ?, ?, ?, ?)', [
            ('Undefined cartesian SRS', -1, 'NONE', -1, 'undefined', 'undefined cartesian coordinate reference system'),
            ('Undefined geographic SRS', 0, 'NONE', 0, 'undefined', 'undefined geographic coordinate reference system'),
            ('WGS 84 geodetic', 4326, 'EPSG', 4326, WGS84, 'longitude/latitude coordinates in decimal degrees on the WGS 84 spheroid'),
            ('ETRS89', 4258, 'EPSG', 4258, ETRS89, 'European Terrestrial Reference System 1989, longitude/latitude in decimal degrees'),
        ])

    def register(table, kind, description, srs=None):
        if geopackage:
            con.execute('INSERT INTO gpkg_contents (table_name, data_type, identifier, description, srs_id) '
                        'VALUES (?, ?, ?, ?, ?)', (table, kind, table, description, srs))

    # A GeoPackage table needs an integer key of its own: there, the documented key is UNIQUE
    own_key = 'fid INTEGER PRIMARY KEY AUTOINCREMENT, ' if geopackage else ''

    used = {f['type'] for fs in fields.values() for f in fs if f['type'] in codelists}
    for typ in sorted(used):
        meta = codelists[typ]
        columns = read(CODELIST / f'{typ}.csv')
        names = list(columns[0].keys()) if columns else ['notation']
        key = meta['codeColumns'].split()[0]
        defs = [f'{q(c)} TEXT' + (' NOT NULL UNIQUE' if c == key else '') for c in names]
        con.execute(f'CREATE TABLE {q("cl_" + typ)} ({own_key}{", ".join(defs)})')
        con.executemany(f'INSERT INTO {q("cl_" + typ)} ({", ".join(map(q, names))}) '
                        f'VALUES ({", ".join("?" * len(names))})',
                        [[r[c] or None for c in names] for r in columns])
        register('cl_' + typ, 'attributes', meta['caption'])

    for table, d in tables.items():
        defs, constraints, notnull = [], [], {f['notation'] for f in fields[table] if f['status'] == 'Required'}
        key = d['primaryKey'].split()
        geometry = None
        for f in fields[table]:
            name = f['notation']
            if f['type'] == 'point':
                geometry = name
                defs.append(f'{q(name)} POINT' + (' NOT NULL' if name in notnull else ''))
                continue
            sql_type, checks = column_sql(f, codelists, external_lengths)
            line = f'{q(name)} {sql_type}' + (' NOT NULL' if name in notnull else '')
            for c in checks:
                line += f' CHECK ({c})'
            if not f['multiplicity']:
                if f['type'] in codelists:
                    line += f' REFERENCES {q("cl_" + f["type"])}({q(codelists[f["type"]]["codeColumns"].split()[0])})'
                elif keys.get(name) not in (None, table):
                    line += f' REFERENCES {q(keys[name])}({q(tables[keys[name]]["primaryKey"])})'
                elif f['type'] in ('documentCode', 'referenceCode') and keys.get(f['type']) not in (None, table):
                    target = keys[f['type']]
                    line += f' REFERENCES {q(target)}({q(tables[target]["primaryKey"])})'
            defs.append(line)
        if key and set(key) <= notnull:
            constraints.append(('UNIQUE' if geopackage else 'PRIMARY KEY') + f' ({", ".join(map(q, key))})')
        con.execute(f'CREATE TABLE {q(table)} ({own_key}{", ".join(defs + constraints)})')
        if key and not set(key) <= notnull:  # a key with optional fields: empty counts as a value
            parts = [q(k) if k in notnull else f"coalesce({q(k)}, '')" for k in key]
            con.execute(f'CREATE UNIQUE INDEX {q(table + "_key")} ON {q(table)} ({", ".join(parts)})')
        description = f'{table} table of the {dataflow} dataflow. {DOCS_URL}{d["page"].removeprefix("docs/")[:-3]}.html'
        if geometry and geopackage:
            register(table, 'features', description, 4258)
            con.execute('INSERT INTO gpkg_geometry_columns VALUES (?, ?, ?, ?, ?, ?)',
                        (table, geometry, 'POINT', 4258, 0, 0))
        else:
            register(table, 'attributes', description)

    # Metadata, in the layout of the WFD documentation's Metadata table
    con.execute(f'''CREATE TABLE "Metadata" ({own_key}tableName TEXT, columnName TEXT, columnPosition INTEGER,
        columnDataType TEXT, multiplicity TEXT, description TEXT, objectType TEXT, dataflowCode TEXT,
        label TEXT, status TEXT, condition TEXT, unit TEXT, documentation TEXT)''')
    rows = []
    for table, d in tables.items():
        page = DOCS_URL + d['page'].removeprefix('docs/')[:-3] + '.html'
        rows.append((table, None, None, None, None, f'{table} table of the {dataflow} dataflow.', 'table',
                     f'UWWTD{dataflow}', None, None, None, None, page))
        for i, f in enumerate(fields[table]):
            rows.append((table, f['notation'], i, metadata_type(f), multiplicity(f), f['definition'], 'column',
                         f'UWWTD{dataflow}', f['label'], f['status'], f['condition'] or None, f['unit'] or None,
                         page))
    con.executemany('INSERT INTO "Metadata" (tableName, columnName, columnPosition, columnDataType, multiplicity, '
                    'description, objectType, dataflowCode, label, status, condition, unit, documentation) '
                    'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', rows)
    register('Metadata', 'attributes', 'The tables and fields, as in the documentation')

    con.execute(f'CREATE TABLE "_about" ({own_key}"key" TEXT NOT NULL UNIQUE, "value" TEXT)')
    version = {r['dataflow']: r for r in read(REPO / 'reference' / 'versions.csv')}.get(dataflow, {})
    con.executemany('INSERT INTO "_about" ("key", "value") VALUES (?, ?)', [
        ('title', f'rUWWTD {dataflow} template'),
        ('dataflow', dataflow),
        ('version', f"{version.get('version', '')} ({version.get('status', '')}), tag "
                    f"{dataflow.lower()}-v{version.get('version', '')}"),
        ('status', 'Draft, under development: tables, fields and code lists may change'),
        ('documentation', DOCS_URL),
        ('source', 'https://github.com/eeadata/WISE.UWWTD.Documentation, reference/schema and reference/codelist'),
        ('commit', commit()),
        ('made', datetime.now(timezone.utc).replace(microsecond=0).isoformat()),
        ('foreign keys', 'Checked only when enabled on each connection: PRAGMA foreign_keys = ON'),
        ('several values', 'A field with several values ([0..n]) holds them as text, separated by commas'),
        ('conditions', 'Conditions (Required if ...) are not enforced; they are in Metadata.condition'),
    ])
    register('_about', 'attributes', 'What this template is and how to use it')
    con.commit()
    problems = con.execute('PRAGMA foreign_key_check').fetchall() + \
        [r for r in con.execute('PRAGMA integrity_check').fetchall() if r != ('ok',)]
    con.execute('VACUUM')
    con.close()
    if problems:
        raise SystemExit(f'{path.name}: {problems}')
    return path


def check():
    """Build both templates in a temporary folder, and check that they can take rows."""
    with tempfile.TemporaryDirectory() as tmp:
        for dataflow, name in FILES.items():
            path = build(dataflow, Path(tmp) / name)
            con = sqlite3.connect(path)
            tables = [r[0] for r in con.execute("SELECT DISTINCT tableName FROM Metadata")]
            cls = [r[0] for r in con.execute("SELECT name FROM sqlite_master WHERE name LIKE 'cl\\_%' ESCAPE '\\'")]
            values = sum(con.execute(f'SELECT count(*) FROM "{c}"').fetchone()[0] for c in cls)
            print(f'{name}: {len(tables)} tables, {len(cls)} code lists with {values} values')
            con.close()


if __name__ == '__main__':
    if sys.argv[1:] == ['--check']:
        check()
    elif len(sys.argv) == 3 and sys.argv[1] in FILES:
        build(sys.argv[1], sys.argv[2])
    else:
        sys.exit(__doc__)
