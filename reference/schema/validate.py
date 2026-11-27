"""Check filled tables of a dataflow against reference/, before packing them for Reportnet 3.

    python reference/schema/validate.py <dataflow> <input> [options]
    python reference/schema/validate.py --check

<dataflow> and <input> are those of package.py: Article23 or SpatialPoints, and a folder with one
CSV per table or a filled template database. The values are checked as package.py would write
them (trimmed, dates without a midnight time, points as GeoJSON Features).

Errors, which the portal would refuse or its validation would report:

* a column that is not a field of the table, or a table that is not in the dataflow;
* a Required field that is empty, or a [1..n] field without a value;
* a value that does not fit its type: string length, identifier, date, year, number, percentage,
  range, range of percentages, e-mail address, URL, language code, point;
* a code that is not in its code list (each value of a field with several values);
* two rows with the same key (the primaryKey of datasets.csv);
* a value that should be the key of a row of another table of the dataflow, and is not:
  measureCode in MeasureFinancing, the documentCode and referenceCode fields;
* with --spatial, an Article23 code of a treatment plant or agglomeration that is not in the
  spatial points tables given;
* a row breaking a rule of the quality checks that only uses the fields of the row: R18, an
  amount above 0 in at least one of the two expenditure fields of MeasureFinancing;
* a measure without a row in MeasureFinancing (check RF04).

Warnings: a column renamed for its case, a link or check that cannot be done because its table is
not given, a value in an Attachment field (files are added on the portal, not in the CSV), the same
value twice in one field.

Not checked: the other conditions ("Required if ..."), and the ISO 639-2 and ZoneType vocabularies
beyond the form of their codes. The report lists the conditional fields with a value to look at.

Options:
  --spatial INPUT        the SpatialPoints tables, to check the Article23 codes against them
  --country XX           the ISO 3166-1 alpha-2 code identifiers must start with
  --srid N               SRID of geometries that carry none, as for package.py
  --multi-separator S    separator between several values of one field (default ,)
  --json FILE            also write the report as JSON

Exit status 1 if there is an error. --check tests the checks on generated rows of every table.

Standard library only.
"""

import argparse
import json
import re
import sys
import tempfile
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from package import Problems, cell, dataflow_tables, match_columns, read_input  # noqa: E402
from template import CODELIST, read  # noqa: E402

IDENTIFIER_TYPES = ('wiseIdentifier', 'documentCode', 'referenceCode')
# Rules on the fields of one row, from the quality checks of the documentation:
# (dataflow, table, check, fields of which at least one is more than 0)
MORE_THAN_ZERO = [('Article23', 'MeasureFinancing', 'R18',
                   ('totalCapitalExpenditure1stCycle', 'totalCapitalExpenditureAfter1stCycle'))]
# Rules between two tables: (dataflow, check, table, key, table that has at least one row per key)
AT_LEAST_ONE_ROW = [('Article23', 'RF04', 'Measure', 'measureCode', 'MeasureFinancing')]
# Article23 fields that hold the code of a spatial points object: (table or '*', field): table
SPATIAL_LINKS = {('UWWTP', 'thematicIdIdentifier'): 'UWWTP',
                 ('Agglomeration', 'thematicIdIdentifier'): 'Agglomeration',
                 ('*', 'euUWWTPCode'): 'UWWTP',
                 ('*', 'euAgglomerationCode'): 'Agglomeration'}


def codes():
    """{type: set of its code values}, from the first code column of each code list."""
    out = {}
    for c in read(CODELIST / 'codelists.csv'):
        column = c['codeColumns'].split()[0]
        out[c['type']] = {r[column] for r in read(CODELIST / f"{c['type']}.csv")}
    return out


def number(text):
    if not re.fullmatch(r'-?\d+(\.\d+)?', text):
        return None
    return float(text)


def bound(text):
    """A bound of a range: a year, a number or a date; '' if open; None if neither."""
    if text == '':
        return ''
    if re.fullmatch(r'\d{4}-\d{2}-\d{2}', text):
        return text
    n = number(text)
    return n


def type_problem(field, value, args):
    """Why one value does not fit the type of its field, or None."""
    typ = field['type']
    m = re.fullmatch(r'string(\d*)', typ)
    if m:
        limit = int(m.group(1) or 4000)
        return f'{len(value)} characters, more than {limit}' if len(value) > limit else None
    if typ in IDENTIFIER_TYPES:
        if len(value) > 42:
            return f'{len(value)} characters, more than 42'
        if not re.fullmatch(r'[A-Z]{2}\S*', value):
            return 'an identifier starts with the two capital letters of the country, without spaces'
        if args.country and not value.startswith(args.country):
            return f'does not start with {args.country}'
        return None
    if typ == 'date':
        return None  # cell() has checked it
    if typ == 'point':
        return None  # cell() has converted it, or reported why not
    if typ == 'gYear':
        return None if re.fullmatch(r'[1-9]\d{3}', value) else 'not a year yyyy'
    if typ == 'integer':
        return None if re.fullmatch(r'-?\d+', value) else 'not a whole number'
    if typ == 'nonNegativeInteger':
        return None if re.fullmatch(r'\d+', value) else 'not a whole number of 0 or more'
    if typ == 'nonNegativeValue':
        n = number(value)
        return None if n is not None and n >= 0 else 'not a number of 0 or more (decimal point: .)'
    if typ == 'Percentage':
        n = number(value)
        return None if n is not None and 0 <= n <= 100 else 'not a number from 0 to 100'
    if typ == 'range':
        m = re.fullmatch(r'([\[(])([^,]*),([^,]*)([\])])', value)
        if not m:
            return 'not a range such as [2028,2033] or [,2036]'
        low, high = bound(m.group(2).strip()), bound(m.group(3).strip())
        if low is None or high is None:
            return 'a bound is not a year, a number or a date'
        if low != '' and high != '' and type(low) is type(high) and low > high:
            return 'the lower bound is above the upper bound'
        return None
    if typ == 'PercentageRange':
        m = re.fullmatch(r'([\[(])\s*(\d+(?:\.\d+)?)\s*,\s*(\d+(?:\.\d+)?)\s*([\])])', value)
        if not m:
            return 'not a range of percentages with both bounds, such as [76,85]'
        low, high = float(m.group(2)), float(m.group(3))
        if not (0 <= low <= high <= 100):
            return 'the bounds must be from 0 to 100, the lower first'
        return None
    if typ == 'Email':
        if len(value) > 250:
            return 'more than 250 characters'
        return None if re.fullmatch(r'[^@\s]+@[^@\s]+\.[^@\s]+', value) else 'not an e-mail address'
    if typ in ('URL', 'url'):
        if typ == 'URL' and len(value) > 2100:
            return 'more than 2100 characters'
        return None if re.fullmatch(r'https?://\S+', value) else 'not a URL starting with http:// or https://'
    if typ == 'Language':
        return None if re.fullmatch(r'[a-z]{3}', value) else 'not a three-letter ISO 639-2 code'
    if typ in ('ZoneType', 'Attachment'):
        return None
    raise KeyError(f"no check for type {typ} of {field['notation']}")


def load(dataflow, source, args, problems):
    """{table: [{field: value as written}]}, with the input's row numbers."""
    tables, fields = dataflow_tables(dataflow)
    found = read_input(source, tables, problems)
    out = {}
    for table, (columns, rows) in found.items():
        index = match_columns(table, columns, fields[table], problems)
        records = []
        for r, row in enumerate(rows, start=2):
            if len(row) > len(columns):
                problems.error(f'{table} row {r}', 'more values than columns')
            rec = {'_row': r}
            for f in fields[table]:
                i = index.get(f['notation'])
                v = row[i] if i is not None and i < len(row) else None
                rec[f['notation']] = cell(f, v, args, f"{table}.{f['notation']} row {r}", problems)
            if any(v for k, v in rec.items() if k != '_row'):
                records.append(rec)
        out[table] = records
    return tables, fields, out


def values(field, text, args):
    if not field['multiplicity']:
        return [text] if text else []
    return [v for v in (p.strip() for p in text.split(args.multi_separator)) if v]


def validate(dataflow, source, args):
    problems = Problems()
    tables, fields, data = load(dataflow, source, args, problems)
    lists = codes()
    review = defaultdict(set)  # conditional fields with a value, to look at

    for table, records in data.items():
        for f in fields[table]:
            name = f['notation']
            for rec in records:
                where = f"{table}.{name} row {rec['_row']}"
                vals = values(f, rec[name], args)
                if not vals:
                    if f['status'] == 'Required' or f['multiplicity'] == '1..n':
                        problems.error(where, 'Required, empty')
                    continue
                if f['status'] == 'Conditional':
                    review[table].add(name)
                if f['type'] == 'Attachment':
                    problems.warn(where, 'a file is added on the portal, not in the CSV')
                    continue
                if len(set(vals)) < len(vals):
                    problems.warn(where, 'the same value twice')
                for v in vals:
                    if f['type'] in lists:
                        if v not in lists[f['type']]:
                            problems.error(where, f'{v!r} is not a code of {f["type"]}')
                    else:
                        why = type_problem(f, v, args)
                        if why:
                            problems.error(where, f'{v!r}: {why}' if len(v) <= 60 else why)

    # Rules on one row
    for flow, table, rule, names in MORE_THAN_ZERO:
        if flow != dataflow or table not in data:
            continue
        for rec in data[table]:
            amounts = [number(rec[n]) for n in names if rec[n]]
            if None in amounts:
                continue  # not a number: reported above
            if not any(a > 0 for a in amounts):
                problems.error(f"{table} row {rec['_row']}",
                               f"{' or '.join(names)}: none is more than 0 (check {rule})")

    # Rules between two tables: (dataflow, check, table, its key, table with at least one row for it)
    for flow, rule, table, key, other in AT_LEAST_ONE_ROW:
        if flow != dataflow or not data.get(table):
            continue
        if other not in data:
            problems.warn(table, f'check {rule} not done: no {other} table given')
            continue
        present = {rec[key] for rec in data[other]}
        for rec in data[table]:
            if rec[key] and rec[key] not in present:
                problems.error(f"{table} row {rec['_row']}",
                               f'{rec[key]!r} has no row in {other} (check {rule})')

    # Keys
    keys = {}
    for table, records in data.items():
        key = tables[table]['primaryKey'].split()
        if not key:
            continue
        seen = {}
        for rec in records:
            k = tuple(rec[n] for n in key)
            if any(k):
                if k in seen:
                    problems.error(f"{table} row {rec['_row']}",
                                   f"same key ({', '.join(key)}) as row {seen[k]}: {', '.join(k)}")
                seen.setdefault(k, rec['_row'])
        keys[table] = {k[0] for k in seen} if len(key) == 1 else None

    # Links between tables of the dataflow, as in template.py
    single = [d['primaryKey'] for d in tables.values() if d['primaryKey'] and ' ' not in d['primaryKey']]
    targets = {d['primaryKey']: t for t, d in tables.items()
               if d['primaryKey'] in single and single.count(d['primaryKey']) == 1}
    by_type = {'documentCode': 'Document', 'referenceCode': 'Reference'}
    for table, records in data.items():
        for f in fields[table]:
            target = targets.get(f['notation'])
            if target in (None, table):
                target = by_type.get(f['type']) if by_type.get(f['type']) in tables else None
            if target in (None, table) or not any(rec[f['notation']] for rec in records):
                continue
            if target not in data:
                problems.warn(f"{table}.{f['notation']}", f'not checked: no {target} table given')
                continue
            for rec in records:
                for v in values(f, rec[f['notation']], args):
                    if v not in keys[target]:
                        problems.error(f"{table}.{f['notation']} row {rec['_row']}",
                                       f'{v!r} is not a {tables[target]["primaryKey"]} of {target}')

    # Links to the spatial points dataflow
    if args.spatial and dataflow == 'Article23':
        sp = Problems()
        _, _, spatial = load('SpatialPoints', args.spatial, args, sp)
        known = {t: {r['thematicIdIdentifier'] for r in spatial.get(t, [])} for t in ('UWWTP', 'Agglomeration')}
        for table, records in data.items():
            for f in fields[table]:
                target = SPATIAL_LINKS.get((table, f['notation'])) or SPATIAL_LINKS.get(('*', f['notation']))
                if not target:
                    continue
                if target not in spatial:
                    problems.warn(f"{table}.{f['notation']}", f'not checked: no spatial points {target} table')
                    continue
                for rec in records:
                    for v in values(f, rec[f['notation']], args):
                        if v not in known[target]:
                            problems.error(f"{table}.{f['notation']} row {rec['_row']}",
                                           f'{v!r} is not in the spatial points {target} table')

    return problems, {t: len(r) for t, r in data.items()}, {t: sorted(v) for t, v in review.items()}


# --- Report ---------------------------------------------------------------------------------------

def grouped(messages):
    """'Table.field: text' lines, with the rows of the same problem gathered."""
    groups = defaultdict(list)
    for m in messages:
        where, text = m.split(': ', 1)
        place, _, row = where.partition(' row ')
        groups[(place, text)].append(row)
    lines = []
    for (place, text), rows in groups.items():
        rows = [r for r in rows if r]
        shown = ', '.join(rows[:8]) + (f' and {len(rows) - 8} more' if len(rows) > 8 else '')
        lines.append(f'{place}: {text}' + (f' (row{"s" if len(rows) > 1 else ""} {shown})' if rows else ''))
    return lines


def report(dataflow, problems, counts, review, args):
    print(f'{dataflow}: ' + (', '.join(f'{t} ({n})' for t, n in counts.items()) or 'no filled table'))
    for kind, messages in (('error', problems.errors), ('warning', problems.warnings)):
        for line in grouped(messages):
            print(f'{kind}: {line}')
    for table, names in review.items():
        print(f"conditional, check by hand: {table}: {', '.join(names)}")
    print(f'{len(problems.errors)} error(s), {len(problems.warnings)} warning(s)')
    if args.json:
        Path(args.json).write_text(json.dumps({
            'dataflow': dataflow, 'rows': counts, 'errors': problems.errors,
            'warnings': problems.warnings, 'conditionalToCheck': review,
        }, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')


# --- Self-check -----------------------------------------------------------------------------------

SAMPLES = {'date': '2026-01-01', 'point': 'POINT (10.5 50.25)', 'integer': '-1',
           'nonNegativeInteger': '1', 'nonNegativeValue': '1.5', 'Percentage': '50', 'gYear': '2030',
           'range': '[2028,2033]', 'PercentageRange': '[76,85]', 'Email': 'someone@example.org', 'url': 'https://example.org',
           'URL': 'https://example.org', 'Language': 'eng', 'ZoneType': 'x', 'Attachment': ''}


def sample(field, lists):
    typ = field['type']
    if typ in lists:
        return sorted(lists[typ])[0]
    if typ in IDENTIFIER_TYPES:
        return 'XX0001'
    if re.fullmatch(r'string\d*', typ):
        return 'x'
    if typ not in SAMPLES:
        raise SystemExit(f"validate.py has no check for type {typ} ({field['notation']}): add one")
    return SAMPLES[typ]


def check():
    """Every table filled with one valid row passes; each kind of mistake is found."""
    import csv
    lists = codes()
    args = argparse.Namespace(spatial=None, country='XX', srid='4326', multi_separator=',', json=None,
                              delimiter=',')

    def write(folder, dataflow, edit=None):
        folder.mkdir(parents=True)
        tables, fields = dataflow_tables(dataflow)
        for t in tables:
            rows = [{f['notation']: sample(f, lists) for f in fields[t]}]
            if edit:
                edit(t, rows)
            with open(folder / f'{t}.csv', 'w', encoding='utf-8', newline='') as fh:
                w = csv.DictWriter(fh, [f['notation'] for f in fields[t]])
                w.writeheader()
                w.writerows(rows)

    def mistakes(t, rows):
        if t == 'Measure':
            rows[0]['measureName'] = ''                   # Required, empty
            rows[0]['costStatus'] = 'nonsense'            # not a code
            rows.append(dict(rows[0]))                    # same key
        if t == 'MeasureFinancing':
            rows[0]['measureCode'] = 'XX0002'             # no such measure
            rows[0]['totalCapitalExpenditure1stCycle'] = '0'
            rows[0]['totalCapitalExpenditureAfter1stCycle'] = ''   # no amount above 0
        if t == 'MSSummary':
            rows[0]['situationAt'] = '30/06/2026'         # not a date
        if t == 'SelfAssessment':
            rows[0]['article3Compliance'] = '[90,110]'    # above 100
        if t == 'Contact':
            rows[0]['email'] = 'nobody'                   # not an e-mail address
        if t == 'Derogation':
            rows[0]['reasonReference'] = 'XX0009'         # no such reference
        if t == 'UWWTP':
            rows[0]['thematicIdIdentifier'] = 'FR0001'    # not of the country

    expected = ['Measure.measureName: Required, empty', "Measure.costStatus: 'nonsense' is not a code",
                'Measure row 3: same key', "MeasureFinancing.measureCode: 'XX0002' is not a measureCode",
                "MSSummary.situationAt: '30/06/2026' is not a date",
                "MeasureFinancing: none is more than 0 (check R18)",
                "Measure row 3: 'XX0001' has no row in MeasureFinancing (check RF04)",
                "SelfAssessment.article3Compliance: '[90,110]': the bounds must be from 0 to 100",
                "Contact.email: 'nobody': not an e-mail address",
                "Derogation.reasonReference: 'XX0009' is not a referenceCode",
                "UWWTP.thematicIdIdentifier: 'FR0001': does not start with XX"]
    with tempfile.TemporaryDirectory() as tmp:
        for dataflow in ('Article23', 'SpatialPoints'):
            write(Path(tmp) / dataflow, dataflow)
            problems, counts, _ = validate(dataflow, Path(tmp) / dataflow, args)
            if problems.errors:
                raise SystemExit(f'{dataflow}: valid rows refused:\n' + '\n'.join(problems.errors))
            print(f'{dataflow}: {len(counts)} tables with a valid row pass')
        write(Path(tmp) / 'bad', 'Article23', mistakes)
        problems, _, _ = validate('Article23', Path(tmp) / 'bad', args)
        for e in expected:
            if not any(m.replace(' row 2', '').startswith(e.split(':')[0]) and e.split(': ', 1)[1] in m
                       for m in problems.errors):
                raise SystemExit(f'not found: {e}\n' + '\n'.join(problems.errors))
        print(f'Article23: {len(problems.errors)} planted mistakes found')
        spatial_args = argparse.Namespace(**{**vars(args), 'spatial': Path(tmp) / 'SpatialPoints'})
        problems, _, _ = validate('Article23', Path(tmp) / 'Article23', spatial_args)
        if problems.errors:
            raise SystemExit('codes in the spatial points refused:\n' + '\n'.join(problems.errors))
        print('Article23: codes found in the spatial points tables')


def main():
    if sys.argv[1:] == ['--check']:
        check()
        return 0
    p = argparse.ArgumentParser(usage=__doc__)
    p.add_argument('dataflow', choices=['Article23', 'SpatialPoints'])
    p.add_argument('input')
    p.add_argument('--spatial')
    p.add_argument('--country')
    p.add_argument('--srid', choices=['4258', '4326'])
    p.add_argument('--multi-separator', default=',')
    p.add_argument('--json')
    args = p.parse_args()
    if args.country and not re.fullmatch(r'[A-Z]{2}', args.country):
        p.error('--country is two capital letters, such as FR')
    problems, counts, review = validate(args.dataflow, args.input, args)
    report(args.dataflow, problems, counts, review, args)
    return 1 if problems.errors else 0


if __name__ == '__main__':
    sys.exit(main())
