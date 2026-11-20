"""Versions of the dataflow specifications: what changed, and whether the version says so.

    python reference/versioning.py check [base]        # fail if a change is not matched by a bump
    python reference/versioning.py report [base]       # the changes per dataflow, in Markdown
    python reference/versioning.py changelog <dataflow> <base>   # release notes since <base>
    python reference/versioning.py new-tags            # the tags to create: versions without a tag
    python reference/versioning.py tag <dataflow>      # the tag of the current version

<base> is a git revision, such as origin/main or a tag; the default is origin/main. The current
state is the working tree.

The specification of a dataflow is its tables in reference/schema (datasets.csv and
<dataflow>/<table>.csv), the code lists of that dataflow in reference/codelist, and the types of
types.csv it uses. Its version is in reference/versions.csv. A change is:

* major (breaking): a delivery that was valid may no longer be. A table, field, code value or code
  list removed or renamed; a field made required or added as required; a type changed or a string
  shortened; a field that took several values now taking one; a key changed;
* minor (compatible): everything valid before is still valid. A table, optional field, code value
  or code list added; a string lengthened; a field relaxed from required;
* patch (text): a label, definition, note, condition or caption changed.

While a dataflow is a draft (version 0.x), a breaking change needs a minor bump. From 1.0.0, it
needs a major one. A larger bump than needed is always accepted.

Standard library only.
"""

import csv
import io
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
LEVELS = ['none', 'patch', 'minor', 'major']
STATUSES = ('draft', 'consultation', 'adopted')
# Stricter first: a change to the right of another makes a delivery fail more often
STATUS_ORDER = {'Optional': 0, 'Conditional': 1, 'Required': 2}


class Tree:
    """The files of the repository, in the working tree or at a git revision."""

    def __init__(self, rev=None):
        self.rev = rev

    def read(self, path):
        if self.rev is None:
            p = REPO / path
            return p.read_text(encoding='utf-8') if p.exists() else None
        r = subprocess.run(['git', '-C', str(REPO), 'show', f'{self.rev}:{path}'], capture_output=True)
        return r.stdout.decode('utf-8') if r.returncode == 0 else None

    def rows(self, path):
        text = self.read(path)
        return list(csv.DictReader(io.StringIO(text))) if text else []


def tag_name(dataflow, version):
    return f'{dataflow.lower()}-v{version}'


def versions(tree):
    return {r['dataflow']: r for r in tree.rows('reference/versions.csv')}


def load(tree, dataflow):
    """The specification of a dataflow, as dictionaries that can be compared."""
    tables = {}
    for d in tree.rows('reference/schema/datasets.csv'):
        if d['dataflow'] != dataflow:
            continue
        t = tables.setdefault(d['table'], {'primaryKey': d['primaryKey'], 'captions': [], 'fields': {}})
        t['captions'].append(d['caption'])
    for name, t in tables.items():
        for f in tree.rows(f'reference/schema/{dataflow}/{name}.csv'):
            t['fields'][f['notation']] = f
    codelists = {}
    for c in tree.rows('reference/codelist/codelists.csv'):
        if c['dataflow'] != dataflow:
            continue
        key = c['codeColumns'].split()[0]
        values = {r[key]: r for r in tree.rows(f"reference/codelist/{c['type']}.csv")}
        codelists[c['type']] = {'meta': c, 'key': key, 'values': values}
    types = {t['type']: t for t in tree.rows('reference/schema/types.csv') if dataflow in t['dataflows'].split()}
    return {'tables': tables, 'codelists': codelists, 'types': types}


def string_length(typ):
    m = re.fullmatch(r'string(\d*)', typ or '')
    return (int(m.group(1)) if m.group(1) else 4000) if m else None


def compare_field(table, old, new, out):
    where = f'`{table}.{old["notation"]}`'
    if old['type'] != new['type'] or old['unit'] != new['unit']:
        a, b = string_length(old['type']), string_length(new['type'])
        if a and b and old['unit'] == new['unit']:
            out.append(('minor' if b > a else 'major', f'{where}: {old["type"]} → {new["type"]}'))
        else:
            out.append(('major', f'{where}: type {old["type"]}{" (" + old["unit"] + ")" if old["unit"] else ""} '
                                 f'→ {new["type"]}{" (" + new["unit"] + ")" if new["unit"] else ""}'))
    if old['multiplicity'] != new['multiplicity']:
        level = 'minor' if not old['multiplicity'] else 'major'
        out.append((level, f'{where}: multiplicity [{old["multiplicity"] or "1"}] → [{new["multiplicity"] or "1"}]'))
    if old['status'] != new['status']:
        stricter = STATUS_ORDER[new['status']] > STATUS_ORDER[old['status']]
        out.append(('major' if stricter else 'minor', f'{where}: {old["status"]} → {new["status"]}'))
    for column in ('label', 'definition', 'condition'):
        if old[column] != new[column]:
            out.append(('patch', f'{where}: {column} changed'))


def compare(old, new):
    """The changes from one specification to another, as (level, description)."""
    out = []
    for name in sorted(old['tables'].keys() - new['tables'].keys()):
        out.append(('major', f'Table `{name}` removed'))
    for name in sorted(new['tables'].keys() - old['tables'].keys()):
        out.append(('minor', f'Table `{name}` added'))
    for name in sorted(old['tables'].keys() & new['tables'].keys()):
        a, b = old['tables'][name], new['tables'][name]
        if a['primaryKey'] != b['primaryKey']:
            out.append(('major', f'`{name}`: key `{a["primaryKey"] or "–"}` → `{b["primaryKey"] or "–"}`'))
        if a['captions'] != b['captions']:
            out.append(('patch', f'`{name}`: caption changed'))
        for f in sorted(a['fields'].keys() - b['fields'].keys()):
            out.append(('major', f'`{name}.{f}` removed'))
        for f in sorted(b['fields'].keys() - a['fields'].keys()):
            required = b['fields'][f]['status'] == 'Required'
            out.append(('major' if required else 'minor',
                        f'`{name}.{f}` added ({b["fields"][f]["status"]}, {b["fields"][f]["type"]})'))
        for f in sorted(a['fields'].keys() & b['fields'].keys()):
            compare_field(name, a['fields'][f], b['fields'][f], out)
        if [f for f in a['fields'] if f in b['fields']] != [f for f in b['fields'] if f in a['fields']]:
            out.append(('patch', f'`{name}`: order of the fields changed'))
    for name in sorted(old['codelists'].keys() - new['codelists'].keys()):
        out.append(('major', f'Code list `{name}` removed'))
    for name in sorted(new['codelists'].keys() - old['codelists'].keys()):
        out.append(('minor', f'Code list `{name}` added'))
    for name in sorted(old['codelists'].keys() & new['codelists'].keys()):
        a, b = old['codelists'][name], new['codelists'][name]
        for v in sorted(a['values'].keys() - b['values'].keys()):
            out.append(('major', f'`{name}`: value `{v}` removed'))
        for v in sorted(b['values'].keys() - a['values'].keys()):
            out.append(('minor', f'`{name}`: value `{v}` added'))
        for v in sorted(a['values'].keys() & b['values'].keys()):
            if a['values'][v] != b['values'][v]:
                out.append(('patch', f'`{name}`: text of `{v}` changed'))
        if a['meta']['caption'] != b['meta']['caption']:
            out.append(('patch', f'`{name}`: caption changed'))
    for name in sorted(old['types'].keys() & new['types'].keys()):
        if old['types'][name]['definition'] != new['types'][name]['definition']:
            out.append(('patch', f'Type `{name}`: definition changed'))
    return out


def level_of(changes):
    return max((LEVELS.index(level) for level, _ in changes), default=0)


def parse(version):
    m = re.fullmatch(r'(\d+)\.(\d+)\.(\d+)', version or '')
    if not m:
        raise ValueError(f'version {version!r} is not like 1.2.3')
    return tuple(int(x) for x in m.groups())


def bump_of(old, new):
    """The bump from one version to another: none, patch, minor, major, or None if it goes down."""
    a, b = parse(old), parse(new)
    if b < a:
        return None
    if b == a:
        return 'none'
    return 'major' if b[0] > a[0] else 'minor' if b[1] > a[1] else 'patch'


def needed(level, version):
    """The bump a change of `level` needs: in a draft (0.x), a breaking change needs a minor one."""
    if level == 'major' and parse(version)[0] == 0:
        return 'minor'
    return level


def dataflows(*trees):
    names = []
    for tree in trees:
        for d in tree.rows('reference/schema/datasets.csv'):
            if d['dataflow'] not in names:
                names.append(d['dataflow'])
    return names


def report(base):
    """For each dataflow: the changes, the bump they need, the bump made, and any problem."""
    old_tree, new_tree = Tree(base), Tree()
    old_v, new_v = versions(old_tree), versions(new_tree)
    results = []
    for df in dataflows(old_tree, new_tree):
        changes = compare(load(old_tree, df), load(new_tree, df))
        level = LEVELS[level_of(changes)]
        problems = []
        if df not in new_v:
            problems.append(f'{df} has no row in reference/versions.csv')
            results.append((df, changes, level, None, None, problems))
            continue
        row = new_v[df]
        if row['status'] not in STATUSES:
            problems.append(f'{df}: status {row["status"]!r} is not one of {", ".join(STATUSES)}')
        try:
            parse(row['version'])
        except ValueError as e:
            problems.append(f'{df}: {e}')
            results.append((df, changes, level, row['version'], None, problems))
            continue
        if df not in old_v:  # a new dataflow, or versions.csv is new: its first version
            results.append((df, changes, level, row['version'], 'first', problems))
            continue
        bump = bump_of(old_v[df]['version'], row['version'])
        if bump is None:
            problems.append(f'{df}: version goes down, {old_v[df]["version"]} → {row["version"]}')
        else:
            need = needed(level, old_v[df]['version'])
            if LEVELS.index(bump) < LEVELS.index(need):
                problems.append(f'{df}: the changes need a {need} bump of {old_v[df]["version"]}, '
                                f'but the version is {row["version"]}')
        results.append((df, changes, level, row['version'], bump, problems))
    return results


def markdown(results, base):
    lines = [f'Changes to the specifications since `{base}`:', '']
    for df, changes, level, version, bump, problems in results:
        head = f'**{df}**: ' + ('no change' if level == 'none' else f'{level} change') + (f'; version {version}' if version else '')
        head += {None: '', 'first': ' (first version)', 'none': ' (unchanged)'}.get(bump, f' ({bump} bump)')
        lines.append(f'- {head}')
        for lvl, text in changes:
            lines.append(f'  - {lvl}: {text}')
        for p in problems:
            lines.append(f'  - **Problem:** {p}')
    return '\n'.join(lines)


def changelog(dataflow, base):
    tree = Tree()
    row = versions(tree).get(dataflow, {})
    title = f'{dataflow} specification {row.get("version", "")} ({row.get("status", "")})'
    if base is None or Tree(base).read('reference/versions.csv') is None:
        changes = None
    else:
        changes = compare(load(Tree(base), dataflow), load(tree, dataflow))
    lines = [f'# {title}', '']
    if changes is None:
        lines.append('First version of the specification.')
    elif not changes:
        lines.append(f'No change to the specification since `{base}`.')
    else:
        lines.append(f'Changes since `{base}`:')
        lines.append('')
        for level in ('major', 'minor', 'patch'):
            items = [text for lvl, text in changes if lvl == level]
            if items:
                lines.append({'major': '## Breaking', 'minor': '## Added or relaxed', 'patch': '## Text'}[level])
                lines.append('')
                lines += [f'- {text}' for text in items]
                lines.append('')
    return '\n'.join(lines).rstrip() + '\n'


def new_tags():
    """The tags of the current versions that do not exist yet.

    Not only the versions changed by the last push: if a run of the workflow on main was skipped,
    the next one releases what it left out. (A version merged and replaced before any run could
    release it is not released; the next version's changelog covers its changes.)
    """
    existing = set(subprocess.run(['git', '-C', str(REPO), 'tag', '--list'], capture_output=True,
                                  text=True).stdout.split())
    return [(df, tag_name(df, row['version'])) for df, row in versions(Tree()).items()
            if tag_name(df, row['version']) not in existing]


def main(args):
    command, rest = (args[0], args[1:]) if args else ('check', [])
    if command in ('check', 'report'):
        base = rest[0] if rest else 'origin/main'
        results = report(base)
        print(markdown(results, base))
        if command == 'check' and any(p for *_, p in results):
            sys.exit(1)
    elif command == 'changelog' and len(rest) == 2:
        print(changelog(rest[0], rest[1]), end='')
    elif command == 'new-tags' and not rest:
        for df, tag in new_tags():
            print(df, tag)
    elif command == 'tag' and len(rest) == 1:
        print(tag_name(rest[0], versions(Tree())[rest[0]]['version']))
    else:
        sys.exit(__doc__)


if __name__ == '__main__':
    main(sys.argv[1:])
