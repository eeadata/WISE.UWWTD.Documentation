# Notes for AI agents

This repository documents the reporting under the Urban Waste Water Treatment Directive: the
compliance algorithm of Directive 91/271/EEC, and the electronic reporting of the revised Directive
(EU) 2024/3019 (rUWWTD). For the rUWWTD it defines two Reportnet 3 dataflows:

* `SpatialPoints`: the agglomerations, treatment plants and discharge points;
* `Article23`: the national implementation programmes.

Both are drafts. Their field names, code lists and conditions can still change.

## Where things are

| Path | Content |
| --- | --- |
| `reference/schema/` | The tables and fields of each dataflow, one CSV per table. See its [README](reference/schema/README.md) |
| `reference/schema/datasets.csv` | Every table: its dataflow, Reportnet 3 dataset, page and key |
| `reference/codelist/` | The code lists, one CSV each; `codelists.csv` lists them. See its [README](reference/codelist/README.md) |
| `reference/versions.csv` | The version of each dataflow specification. See [reference/README.md](reference/README.md) |
| `docs/` | The documentation (Sphinx, MyST Markdown). `docs/rUWWTD2024/` for the rUWWTD |
| `docs/_ext/` | Sphinx extensions that render the field tables and code lists from `reference/` |
| `explorer/` | The data explorer (Observable Framework). See its [README](explorer/README.md) |
| `temp/`, `prefill/` | Ignored by git. Working files, and any Member State data |

## Rules

* **`reference/` is the single source.** The field tables and code lists in the documentation, the
  explorer and the template databases are all generated from its CSV files. To change a field or a
  code, edit the CSV, never the generated tables in `docs/`.
* **A change in `reference/` needs a version bump** in `reference/versions.csv`, at the level that
  `python reference/versioning.py report origin/main` says. Do not create version tags: the
  workflow makes them.
* **Read the definitions from the CSV files**, not from the documentation pages. Cells in `label`,
  `definition` and `condition` hold MyST markup: reduce ``{ref}`label` `` to the title of its
  target and `` `text` `` to `text` when you need plain text.
* **Keep Member State data out of git.** Prefills and filled tables go in `temp/` or outside the
  repository.
* **`docs/rUWWTD2024/*/OpenIssues.md` are internal working notes.** They are left out of the
  published build. Do not link to them from other pages.

## Commands

Python 3; the scripts in `reference/` use the standard library only.

```sh
python reference/schema/check.py               # the CSV files agree with each other
python reference/schema/template.py --check    # the template databases can be built
python reference/schema/package.py --check     # tables pack into Reportnet 3 zip files
python reference/schema/validate.py --check    # the checks of filled tables work
python reference/versioning.py report origin/main
pip install -r docs/requirements.txt
sphinx-build -n --keep-going -b html docs _build/html
```

The workflow runs the first five and the Sphinx build on every pull request. Run them after a
change, and fix the warnings the Sphinx build gives on the pages you changed.

## Preparing data for Reportnet 3

An agent can turn data from a source, such as a national website, a report or a spreadsheet, into
files ready to upload. It prepares the files only. A person uploads them on the Reportnet 3 portal
(<https://reportnet.europa.eu>), checks the result of the portal's validation, and releases the
data. Do not upload through the Reportnet 3 API.

### The structure of the files

`python reference/schema/package.py <dataflow> <input> <out-dir>` writes them from a folder of
table CSVs or a filled template database, and follows the rules below. See
[reference/schema/README.md](reference/schema/README.md#zip-files-for-reportnet-3).

* **One zip per Reportnet 3 dataset.** The `dataset` column of `datasets.csv` names it. `Article23`
  has three: `DescriptiveDataset`, `DocumentsDataset` and `PrivateDataset`. `SpatialPoints` has
  one, with an empty `dataset`.
* **One CSV per table in the zip**, named after the table: `Measure.csv`. A table shown in several
  parts in the documentation (rows with a `group` in `datasets.csv`) is still one CSV.
* **The header is exactly the table's field list:** every `notation` of `<dataflow>/<table>.csv`,
  in that order and with that spelling. Reportnet 3 refuses a file with a column missing, a column
  added, or a name spelled differently, and cancels the import with "Import files contain incorrect
  headers". Add a field you have no value for as an empty column.
* **UTF-8**, one row per record, quoted as needed.
* **Values:**
  - a code: the `notation` of its code list in `reference/codelist/<type>.csv`, never the label;
  - a date: `yyyy-mm-dd`, without a time;
  - a number: a full stop as decimal separator, without thousands separators or units;
  - no value: an empty cell;
  - several values in a field with a multiplicity (`0..n`, `1..n`): one cell, the values separated
    by commas, the cell quoted;
  - a geometry (`geometry` in `SpatialPoints`): a GeoJSON Feature that carries its coordinate
    system in `properties.srid`, on one line in the cell, for example:

    ```json
    {"type": "Feature", "geometry": {"type": "Point", "coordinates": [10.0000, 50.0000]},
     "properties": {"srid": "4326"}}
    ```

    Coordinates are longitude then latitude. Reportnet 3 accepts WKT or a bare GeoJSON geometry
    without an error, but stores the field empty.
* **Keys:** the `primaryKey` of `datasets.csv` is unique within its table. A field that holds the
  key of another table (`measureCode` in `MeasureFinancing`, the `documentCode` and `referenceCode`
  fields) must match a row of that table, in the same delivery.

### Filling the tables from a source

* Take values from the source; do not guess. Leave a field empty when the source does not give it,
  even a Required one, and list it for the person who reports.
* Map the source's terms to code list values by their definitions. When no value fits, leave the
  field empty and say why; do not add a code.
* Record where each value came from (a page, a document, a table of the source) in a working file
  next to the tables, not in the reported fields, unless a field asks for a reference.
* Keep the codes of objects that already exist: the `euUWWTPCode` and `euAgglomerationCode` of the
  spatial points dataflow are used by Article 23.
* Check the tables before packing them:
  `python reference/schema/validate.py <dataflow> <input> --country XX`, with
  `--spatial <spatial-input>` for Article 23. It finds missing Required values, wrong types,
  unknown codes, repeated keys and broken links between tables. It does not check the conditions
  ("Required if ..."): it lists the Conditional fields that have a value, to read against the
  `condition` column. Fix the errors in the source mapping, not by inventing values.
* Pack them with `package.py`, and hand the zips and `manifest.json` to the person who reports.

### Not yet confirmed

The Reportnet 3 dataflows of the rUWWTD are not designed yet, so the following has not been tried
on them. Check it on the portal, and correct this section, before relying on it:

* the field delimiter the portal's import expects for these dataflows (the files above use commas);
* the separator Reportnet 3 expects between several values of one field;
* that the portal imports a zip of all the tables of a dataset at once.

## Writing

* Plain English, short sentences, present tense; the style of the existing pages.
* Markdown: lines of 100 characters at most, no blank line above a heading (`.markdownlint.jsonc`).
* Say that a draft is a draft; do not present proposals as adopted requirements.
