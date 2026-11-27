# Field tables

The fields of the rUWWTD 2024 reporting tables, one CSV file per table. These files are the single
source of the fields:

* the documentation shows them: each field table on the table pages of
  [Spatial points](../../docs/rUWWTD2024/SpatialPoints/index.md) and
  [Article 23](../../docs/rUWWTD2024/Article23/index.md) is rendered from its CSV by the
  `{fieldtable}` directive ([docs/_ext/fieldtable.py](../../docs/_ext/fieldtable.py));
* the Reportnet 3 schema, the prefill and the quality checks can read the same files, instead of
  parsing the documentation pages.

To add, change or remove a field, edit the CSV. Do not edit the tables in the documentation: they
are generated. The text around each table (what the table is for, its rows, the class diagram)
stays in the documentation page. The content is a draft wherever the page says so.

The values of the code lists that fields use are in [reference/codelist](../codelist/README.md).

## Files

| File | Content |
| --- | --- |
| `datasets.csv` | Every field table shown in the documentation: one row per table, or per part of a table shown in several parts |
| `<dataflow>/<table>.csv` | The fields of one table, for example `Article23/Measure.csv` |
| `types.csv` | The simple types and the external vocabularies a field's type may name |
| `check.py` | Checks the files against each other and against the code lists |
| `template.py` | Makes an empty template database of a dataflow from these files (see below) |
| `validate.py` | Checks filled tables against these files and the code lists (see below) |
| `package.py` | Packs filled tables into zip files ready to upload on the Reportnet 3 portal (see below) |

Tables:

| Dataflow | Dataset | Tables |
| --- | --- | --- |
| `SpatialPoints` | | `Agglomeration`, `UWWTP`, `DischargePoint` |
| `Article23` | `DescriptiveDataset` | `MSSummary`, `SelfAssessment`, `Derogation`, `CulturalHeritageExtension`, `LessStringentTreatment`, `Measure`, `MeasureFinancing`, `UWWTP`, `Agglomeration` |
| `Article23` | `DocumentsDataset` | `dcMetadata`, `Reference`, `Document` |
| `Article23` | `PrivateDataset` | `Contact` |

## Format

All files are UTF-8, comma-separated, with a header row. An empty cell means nothing to add.

### datasets.csv

| Column | Content |
| --- | --- |
| `dataflow` | `SpatialPoints` or `Article23`, as in `codelists.csv`; also the folder of the table's CSV |
| `dataset` | The Reportnet 3 dataset of the table; empty for spatial points, which has a single dataset |
| `table` | The table name, and the name of its CSV |
| `group` | Empty for a table shown in one part. For a table shown in several parts (`MSSummary`, `Measure`), the part, one row each; the fields of the part have the same `group` |
| `order` | Position of the table, or part, in the documentation of its dataflow |
| `page` | Path of the documentation page that shows the table |
| `anchor` | Label of that page, for a cross-reference ``{ref}`art23-measure` `` |
| `caption` | Caption of the table in the documentation |
| `conditionHeader` | Header of the last column in the documentation: `Condition`, `Condition or codelist` or `Codelist` |
| `widths` | Column widths in the documentation |
| `primaryKey` | The field, or space-separated fields, that the page says identify a row. Empty where the page states none |

### `<dataflow>/<table>.csv`

One row per field, in the order shown.

| Column | Content |
| --- | --- |
| `notation` | Field name, written plain (`measureCode`); the documentation shows it as code |
| `label` | Short label |
| `definition` | What the field means |
| `type` | A simple type or an external vocabulary from `types.csv`, or a code list type from `codelists.csv` |
| `multiplicity` | Empty for a single value; `0..n` or `1..n` for a field that accepts several values, separated by commas |
| `unit` | Unit of a number, for example `p.e.`; empty if none |
| `status` | `Required`, `Conditional` or `Optional` |
| `condition` | When the field is required or allowed, and its code list; empty if nothing to add (the documentation shows a dash) |
| `group` | The part of the table the field is shown in; see `datasets.csv` |

The documentation shows the Type column as `type`, then the unit in brackets, then the
multiplicity in square brackets: `nonNegativeValue (p.e.)`, `wiseIdentifier [0..n]`.

### types.csv

| Column | Content |
| --- | --- |
| `type` | Type name, as used in the `type` column |
| `kind` | `simple` for a WISE attribute type; `external` for a vocabulary published elsewhere and not copied here |
| `dataflows` | Space-separated dataflows whose documentation defines it (the *Data types* sections of the spatial points and Article 23 pages) |
| `definition` | What a value of the type is |
| `reference` | Where the documentation defines it, or the URL of the external vocabulary |

### Markup in cells

`label`, `definition` and `condition` are documentation text and may use MyST markup, kept as it
was on the pages so that the documentation still shows the same links and code:

* a cross-reference to a page or a code list, by its label: ``{ref}`art23-cl-cost-status` ``;
* a field name or a code value, in backticks: `` `costStatus` = `unknown` ``.

The labels are those of the documentation: `datasets.csv` gives the label of each table page, and
`codelists.csv` that of each code list. A tool that writes a Reportnet 3 schema or a message from
these files should reduce the markup to plain text: ``{ref}`label` `` to the title of the target
(or the label itself), and `` `text` `` to `text`.

A cell is a single paragraph: no line breaks.

## Checks

```
python reference/schema/check.py
```

It fails (exit status 1) and lists the problems if a table in `datasets.csv` has no CSV, a CSV is
not in `datasets.csv`, a type is in neither `types.csv` nor `codelists.csv`, a status is not one of
the three, a notation is repeated, a `primaryKey` field does not exist, a `group` does not match, or
a page does not show its table with the directive. The documentation build runs the same checks
and reports them as warnings.

## Template databases

```
python reference/schema/template.py Article23 rUWWTD_Article23_template.sqlite
python reference/schema/template.py SpatialPoints rUWWTD_SpatialPoints_template.gpkg
```

`template.py` makes an empty database of a dataflow from these files and the code lists, to load
data into and check it. The data explorer publishes both, and the workflow checks that they can
be built (`template.py --check`). Each has:

* one empty table per reporting table, with its fields in order, `NOT NULL` for the Required
  fields, the key stated in `datasets.csv`, and `CHECK` constraints from the types: lengths, dates,
  values of 0 or more, percentages, years and ranges;
* one table per code list, `cl_<Type>`, filled from `reference/codelist`, and a foreign key to it
  from each field of that type. A field with several values (`[0..n]`) holds them as text,
  separated by commas, without a foreign key;
* foreign keys between reporting tables, where a field holds the key of another table of the
  dataflow (`measureCode` in MeasureFinancing; `documentCode` and `referenceCode` fields);
* `Metadata`: the tables and fields in the layout of the `Metadata` table of the Water Framework
  Directive documentation (`tableName`, `columnName`, `columnPosition`, `columnDataType`,
  `multiplicity`, `description`, `objectType`, `dataflowCode`), with `label`, `status`,
  `condition`, `unit` and `documentation` added;
* `_about`: the dataflow, the commit it was made from, and how to use it.

The spatial points template is a GeoPackage: its tables have a point geometry in ETRS89
(EPSG:4258), and it opens in QGIS. Because a GeoPackage table needs an integer key of its own
(`fid`), the stated key is `UNIQUE` there. The Article 23 template is a plain SQLite database.

SQLite checks foreign keys only when they are enabled on each connection
(`PRAGMA foreign_keys = ON`). Conditions ("Required if ...") are not enforced; they are left to the
quality checks.

## Checking filled tables

```sh
python reference/schema/validate.py Article23 <input> --spatial <spatial-input> --country XX
python reference/schema/validate.py SpatialPoints <input> --country XX
```

`validate.py` checks filled tables before they are packed. `<input>` is as for `package.py`
below, and the values are checked as `package.py` would write them. It reports, with the table,
field and rows:

* errors: an unknown table or column; a Required field empty; a value that does not fit its type
  (length, identifier, date, year, number, percentage, range, e-mail address, URL, language code,
  point); a code not in its code list, for each value of a field with several values; two rows
  with the same key; a `measureCode`, `documentCode` or `referenceCode` that is not the key of a
  row of its table; with `--spatial`, a treatment plant or agglomeration code of Article 23 that is
  not in the spatial points tables given; with `--country`, an identifier of another country;
* warnings: a column renamed for its case, a link that cannot be checked because its table is not
  given, a value in an `Attachment` field (files are added on the portal), a value given twice;
* the Conditional fields that have a value, to check by hand: the conditions are text and are not
  checked, nor are the ISO 639-2 and ZoneType vocabularies beyond the form of their codes.

It exits with status 1 if there is an error. `--json <file>` also writes the report as JSON.
`validate.py --check`, run by the workflow, fills every table with a valid row, which must pass,
then plants mistakes, which must be found. It fails when a field has a type it has no check for.

## Zip files for Reportnet 3

```sh
python reference/schema/package.py Article23 <input> <out-dir>
python reference/schema/package.py SpatialPoints <input> <out-dir> --srid 4258
```

`package.py` turns filled tables into the files a reporter uploads on the Reportnet 3 portal.
`<input>` is a folder with one CSV per table, named after the table (`Measure.csv`), or a template
database with its tables filled. `<out-dir>` receives:

* one zip per Reportnet 3 dataset that has a filled table: `Article23_DescriptiveDataset.zip`,
  `Article23_DocumentsDataset.zip`, `Article23_PrivateDataset.zip`, `SpatialPoints.zip`;
* `manifest.json`: the tables and rows packed, the version of the specification, the warnings, and
  what is left to check.

Each zip holds one CSV per filled table, named after the table, UTF-8, comma-separated. Its header
is exactly the table's fields, in order, as Reportnet 3 requires: a column missing from the input
is added empty, with a warning if the field is Required, and an unknown column is an error. Dates
are written `yyyy-mm-dd`; several values of a field, separated by commas. A point is written as
the GeoJSON Feature that Reportnet 3 stores, with its SRID in `properties.srid`; it may be given as
GeoJSON, WKT, EWKT or a GeoPackage geometry, and `--srid` (4258 or 4326) gives the SRID of a value
that carries none. `--delimiter` and `--multi-separator` change the separators.

On an error it writes nothing and exits with status 1. It does not check code values, keys or
conditions: run `validate.py` first; the portal's validation checks the conditions.
`package.py --check`, run by the workflow, packs every table and reads the zips back.

## Adding a table

Add its CSV, a row in `datasets.csv` (one per part, if it is shown in parts), and a directive on
its page:

```
:::{fieldtable} Article23/Measure
:::
```

or, for one part of a table:

```
:::{fieldtable} Article23/Measure
:group: cost
:::
```

## Versions

The specification of each dataflow, its tables here and its code lists, has a version in
`reference/versions.csv`. A change here needs a version bump, which the workflow checks, and a merged
version is tagged and released automatically. See [reference/README.md](../README.md).
