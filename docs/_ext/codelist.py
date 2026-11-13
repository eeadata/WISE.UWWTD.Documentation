"""Sphinx directive that renders a code list from its CSV in reference/codelist/.

The CSV files are the single source of the code list values; the documentation shows them, and other
tools (the Reportnet 3 schema, quality checks, the prefill) read the same files.

    :::{codelist} ConditionOfFacility
    :::

reference/codelist/codelists.csv lists every code list: the dataflow and page anchor it belongs to, its
caption, the column headers shown (in the order of the CSV's columns) and their widths, and which
columns hold codes (shown as code). An empty cell is shown as a dash.
"""

import csv
from pathlib import Path

from docutils import nodes
from docutils.parsers.rst import directives
from docutils.statemachine import StringList
from sphinx.util.docutils import SphinxDirective


def codelist_dir(env):
    return Path(env.srcdir).parent / 'reference' / 'codelist'


def read_csv(path):
    with open(path, encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))


class CodelistDirective(SphinxDirective):
    required_arguments = 1
    has_content = False
    option_spec = {'caption': directives.unchanged}

    def run(self):
        root = codelist_dir(self.env)
        name = self.arguments[0]
        index_path, path = root / 'codelists.csv', root / f'{name}.csv'
        for p in (index_path, path):
            self.env.note_dependency(str(p))
        index = {r['type']: r for r in read_csv(index_path)}
        if name not in index or not path.exists():
            raise self.error(f'codelist {name!r}: not in {index_path.name} or no {path.name}')
        meta = index[name]
        with open(path, encoding='utf-8', newline='') as f:
            reader = csv.DictReader(f)
            columns, rows = reader.fieldnames, list(reader)
        headers = meta['headers'].split('|')
        codes = set(meta['codeColumns'].split())
        if len(headers) != len(columns) or not codes <= set(columns):
            raise self.error(f'codelist {name!r}: the headers or code columns in codelists.csv do not match '
                             f'the columns of {path.name} ({", ".join(columns)})')

        lines = [f":::{{list-table}} {self.options.get('caption', meta['caption'])}", ':header-rows: 1']
        if meta['widths']:
            lines.append(f":widths: {meta['widths']}")
        lines.append('')

        def add(row):
            for i, value in enumerate(row):
                first, *rest = (value or '–').split('\n')
                lines.append(('* - ' if i == 0 else '  - ') + first)
                lines.extend(('    ' + line) if line else '' for line in rest)

        add(headers)
        for r in rows:
            add([f'`{r[c]}`' if c in codes and r[c] else r[c] for c in columns])
        lines.append(':::')

        container = nodes.container()
        self.state.nested_parse(StringList(lines, source=str(path)), self.content_offset, container)
        return container.children


def setup(app):
    app.add_directive('codelist', CodelistDirective)
    return {'version': '1.0', 'parallel_read_safe': True, 'parallel_write_safe': True}
