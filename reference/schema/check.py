"""Check the field tables in reference/schema against each other and against the code lists.

    python reference/schema/check.py

Exits with status 1 and lists the problems if:

* a table in datasets.csv has no CSV, or a CSV has no row in datasets.csv;
* a CSV does not have the expected columns;
* a field's type is in neither types.csv nor reference/codelist/codelists.csv;
* a field's status is not Required, Conditional or Optional;
* a notation is repeated within a table, or a primaryKey field is not a field of its table;
* a group in datasets.csv has no fields, or a field's group is not in datasets.csv;
* a page in datasets.csv does not show the table with a {fieldtable} directive;
* a cell has a line break.

The Sphinx build runs the same checks (docs/_ext/fieldtable.py) and reports them as warnings.
Standard library only.
"""

import csv
import re
import sys
from pathlib import Path

TABLE_COLUMNS = ['dataflow', 'dataset', 'table', 'group', 'order', 'page', 'anchor', 'caption',
                 'conditionHeader', 'widths', 'primaryKey']
FIELD_COLUMNS = ['notation', 'label', 'definition', 'type', 'multiplicity', 'unit', 'status',
                 'condition', 'group']
TYPE_COLUMNS = ['type', 'kind', 'dataflows', 'definition', 'reference']
STATUSES = {'Required', 'Conditional', 'Optional'}


def read(path):
    with open(path, encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        return reader.fieldnames, list(reader)


def check(repo):
    """Return the list of problems found; empty if there is none."""
    repo = Path(repo)
    schema, problems = repo / 'reference' / 'schema', []

    columns, tables = read(schema / 'datasets.csv')
    if columns != TABLE_COLUMNS:
        return [f'datasets.csv: columns are {columns}, expected {TABLE_COLUMNS}']
    columns, types = read(schema / 'types.csv')
    if columns != TYPE_COLUMNS:
        return [f'types.csv: columns are {columns}, expected {TYPE_COLUMNS}']
    simple = {t['type'] for t in types}
    codelists = {r['type'] for r in read(repo / 'reference' / 'codelist' / 'codelists.csv')[1]}
    for both in sorted(simple & codelists):
        problems.append(f'types.csv: {both} is also a code list in codelists.csv')

    groups = {}
    for t in tables:
        groups.setdefault((t['dataflow'], t['table']), []).append(t)
        page = repo / t['page']
        directive = f":::{{fieldtable}} {t['dataflow']}/{t['table']}"
        if t['group']:
            directive += f"\n:group: {t['group']}"
        if not page.exists():
            problems.append(f"datasets.csv: page {t['page']} does not exist")
        elif not re.search(re.escape(directive) + r'\n', page.read_text(encoding='utf-8')):
            problems.append(f"{t['page']}: no {directive!r} for {t['dataflow']}/{t['table']}")

    listed = {schema / d / f'{n}.csv' for d, n in groups}
    for path in sorted(schema.glob('*/*.csv')):
        if path not in listed:
            problems.append(f'{path.relative_to(schema)}: not in datasets.csv')

    for (dataflow, name), rows in groups.items():
        path = schema / dataflow / f'{name}.csv'
        rel = path.relative_to(schema)
        if not path.exists():
            problems.append(f'datasets.csv: {dataflow}/{name} has no CSV ({rel})')
            continue
        columns, fields = read(path)
        if columns != FIELD_COLUMNS:
            problems.append(f'{rel}: columns are {columns}, expected {FIELD_COLUMNS}')
            continue
        notations = [f['notation'] for f in fields]
        for n in sorted({n for n in notations if notations.count(n) > 1}):
            problems.append(f'{rel}: notation {n} is repeated')
        for key in {k for r in rows for k in r['primaryKey'].split()}:
            if key not in notations:
                problems.append(f'datasets.csv: primaryKey {key} is not a field of {dataflow}/{name}')
        declared = {r['group'] for r in rows}
        used = {f['group'] for f in fields}
        for g in sorted(declared - used):
            problems.append(f'{rel}: no field in group {g!r} of datasets.csv')
        for g in sorted(used - declared):
            problems.append(f'{rel}: group {g!r} is not in datasets.csv')
        for f in fields:
            where = f"{rel}: {f['notation']}"
            if f['type'] not in simple and f['type'] not in codelists:
                problems.append(f"{where}: type {f['type']} is in neither types.csv nor codelists.csv")
            if f['status'] not in STATUSES:
                problems.append(f"{where}: status {f['status']!r} is not one of {sorted(STATUSES)}")
            for column, value in f.items():
                if '\n' in (value or ''):
                    problems.append(f'{where}: {column} has a line break; a cell is a single paragraph')
            if f['multiplicity'] and not re.fullmatch(r'[01]\.\.(n|[1-9]\d*)', f['multiplicity']):
                problems.append(f"{where}: multiplicity {f['multiplicity']!r} is not like 0..n or 1..n")
    return problems


if __name__ == '__main__':
    found = check(Path(__file__).resolve().parents[2])
    for p in found:
        print(p)
    if found:
        sys.exit(1)
    print('reference/schema: no problem found')
