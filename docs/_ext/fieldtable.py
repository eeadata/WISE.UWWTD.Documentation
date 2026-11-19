"""Sphinx directive that renders a field table from its CSV in reference/schema/.

The CSV files are the single source of the fields of each table; the documentation shows them, and
other tools (the Reportnet 3 schema, quality checks, the prefill) read the same files.

    :::{fieldtable} Article23/Measure
    :group: cost
    :::

The argument is <dataflow>/<table>, the path of the CSV under reference/schema/ without the
extension. reference/schema/datasets.csv gives, for each table and group, the caption, the header of
the last column and the column widths. `:group:` is needed for a table whose fields are shown in
several parts, and renders only the fields of that group.

At the start of the build, the checks of reference/schema/check.py run and report each problem as a
warning: a Type that is neither a simple type nor a code list, or a table without its CSV.
"""

import csv
import importlib.util
from pathlib import Path

from docutils import nodes
from docutils.parsers.rst import directives
from docutils.statemachine import StringList
from sphinx.util import logging
from sphinx.util.docutils import SphinxDirective

logger = logging.getLogger(__name__)

HEADERS = ['Notation', 'Label', 'Definition', 'Type', 'Status']


def schema_dir(srcdir):
    return Path(srcdir).parent / 'reference' / 'schema'


def read_csv(path):
    with open(path, encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))


def type_cell(field):
    """The Type column as written in the documentation: type, then (unit), then [multiplicity]."""
    text = field['type']
    if field['unit']:
        text += f" ({field['unit']})"
    if field['multiplicity']:
        text += f" [{field['multiplicity']}]"
    return text


class FieldtableDirective(SphinxDirective):
    required_arguments = 1
    has_content = False
    option_spec = {'group': directives.unchanged}

    def run(self):
        root = schema_dir(self.env.srcdir)
        name, group = self.arguments[0], self.options.get('group', '')
        dataflow, _, table = name.partition('/')
        index_path, path = root / 'datasets.csv', root / f'{name}.csv'
        for p in (index_path, path):
            self.env.note_dependency(str(p))
        index = {(r['dataflow'], r['table'], r['group']): r for r in read_csv(index_path)}
        meta = index.get((dataflow, table, group))
        if meta is None or not path.exists():
            raise self.error(f'fieldtable {name!r} group {group!r}: not in {index_path.name} or no {name}.csv')
        fields = [f for f in read_csv(path) if f['group'] == group]
        if not fields:
            raise self.error(f'fieldtable {name!r}: no field in group {group!r}')

        lines = [f":::{{list-table}} {meta['caption']}", ':header-rows: 1']
        if meta['widths']:
            lines.append(f":widths: {meta['widths']}")
        lines.append('')

        def add(row):
            for i, value in enumerate(row):
                lines.append(('* - ' if i == 0 else '  - ') + (value or '–'))

        add(HEADERS + [meta['conditionHeader']])
        for f in fields:
            add([f"`{f['notation']}`", f['label'], f['definition'], type_cell(f), f['status'],
                 f['condition']])
        lines.append(':::')

        container = nodes.container()
        self.state.nested_parse(StringList(lines, source=str(path)), self.content_offset, container)
        return container.children


def run_checks(app):
    path = schema_dir(app.srcdir) / 'check.py'
    spec = importlib.util.spec_from_file_location('schema_check', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    for problem in module.check(Path(app.srcdir).parent):
        logger.warning(f'reference/schema: {problem}', type='fieldtable', subtype='check')


def setup(app):
    app.add_directive('fieldtable', FieldtableDirective)
    app.connect('builder-inited', run_checks)
    return {'version': '1.0', 'parallel_read_safe': True, 'parallel_write_safe': True}
