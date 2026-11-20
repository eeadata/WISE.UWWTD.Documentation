"""Data loader: the reference data of the repository, as one JSON document.

Reads the code lists (reference/codelist), the field tables and simple types (reference/schema),
and the labels of the documentation pages (docs/rUWWTD2024), so that the explorer can show them,
link each one to its definition in the documentation, and list the fields that use each code list.
Standard library only.
"""

import csv
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
CODELIST = REPO / 'reference' / 'codelist'
SCHEMA = REPO / 'reference' / 'schema'
DOCS = REPO / 'docs'
# Working notes, left out of the published documentation (docs/_ext/internal.py)
INTERNAL_PAGES = ['rUWWTD2024/SpatialPoints/OpenIssues.md', 'rUWWTD2024/Article23/OpenIssues.md']


def read(path):
    with open(path, encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        return reader.fieldnames, list(reader)


def labels():
    """Every label of the rUWWTD documentation: its page and the title it is shown with."""
    found = {}
    for page in sorted((DOCS / 'rUWWTD2024').rglob('*.md')):
        rel = page.relative_to(DOCS).as_posix()
        lines = page.read_text(encoding='utf-8').split('\n')
        for i, line in enumerate(lines):
            m = re.fullmatch(r'\((.+)\)=', line)
            if not m:
                continue
            title = next((re.sub(r'^#+\s*', '', l) for l in lines[i + 1:] if l.startswith('#')), m.group(1))
            found[m.group(1).lower()] = {
                'page': rel[:-3] + '.html',
                'title': title.strip(),
                'internal': rel in INTERNAL_PAGES,
            }
    return found


def main():
    _, index = read(CODELIST / 'codelists.csv')
    codelists = []
    for meta in index:
        columns, rows = read(CODELIST / f"{meta['type']}.csv")
        codelists.append({**meta, 'columns': columns, 'headers': meta['headers'].split('|'),
                          'codeColumns': meta['codeColumns'].split(), 'rows': rows})

    _, datasets = read(SCHEMA / 'datasets.csv')
    tables, seen = [], set()
    for d in datasets:
        key = (d['dataflow'], d['table'])
        if key in seen:
            continue
        seen.add(key)
        _, fields = read(SCHEMA / d['dataflow'] / f"{d['table']}.csv")
        tables.append({'dataflow': d['dataflow'], 'dataset': d['dataset'], 'table': d['table'],
                       'page': d['page'].removeprefix('docs/')[:-3] + '.html', 'anchor': d['anchor'],
                       'primaryKey': d['primaryKey'].split(),
                       'groups': [{'group': g['group'], 'caption': g['caption']}
                                  for g in datasets if (g['dataflow'], g['table']) == key],
                       'fields': fields})

    _, types = read(SCHEMA / 'types.csv')
    json.dump({'codelists': codelists, 'tables': tables, 'types': types, 'labels': labels()},
              sys.stdout, ensure_ascii=False)


if __name__ == '__main__':
    main()
