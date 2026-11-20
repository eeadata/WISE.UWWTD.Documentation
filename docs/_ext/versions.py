"""The version of a dataflow specification, from reference/versions.csv.

    **Specification version:** {specversion}`Article23`

shows the version and status, such as "0.1.0 (draft)", linked to its GitHub release. The versions and
how they change are explained in reference/README.md.
"""

import csv
from pathlib import Path

from docutils import nodes

RELEASES = 'https://github.com/eeadata/WISE.UWWTD.Documentation/releases/tag/'


def versions_path(env):
    return Path(env.srcdir).parent / 'reference' / 'versions.csv'


def specversion_role(name, rawtext, text, lineno, inliner, options=None, content=None):
    env = inliner.document.settings.env
    path = versions_path(env)
    env.note_dependency(str(path))
    with open(path, encoding='utf-8', newline='') as f:
        rows = {r['dataflow']: r for r in csv.DictReader(f)}
    row = rows.get(text.strip())
    if row is None:
        message = inliner.reporter.error(f'specversion: no dataflow {text!r} in {path.name}', line=lineno)
        return [inliner.problematic(rawtext, rawtext, message)], [message]
    tag = f"{row['dataflow'].lower()}-v{row['version']}"
    reference = nodes.reference(rawtext, row['version'], refuri=RELEASES + tag, internal=False)
    return [nodes.strong('', '', reference), nodes.Text(f" ({row['status']}, {row['date']})")], []


def setup(app):
    app.add_role('specversion', specversion_role)
    return {'version': '1.0', 'parallel_read_safe': True, 'parallel_write_safe': True}
