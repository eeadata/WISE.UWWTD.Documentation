# Reference data and its versions

The machine-readable definition of the rUWWTD dataflows:

| Folder or file | Content |
| --- | --- |
| [codelist/](codelist/README.md) | The code lists, one CSV file each |
| [schema/](schema/README.md) | The tables and fields of each dataflow, the simple types, and the template databases made from them |
| `versions.csv` | The version of each dataflow specification |
| `versioning.py` | Classifies changes and checks that the version follows them |

The documentation, the data explorer and the template databases are all made from these files, in
the same build, so they always agree. This page explains how the specifications are versioned.

## What has a version

Each dataflow specification has its own version: `SpatialPoints` and `Article23`. A specification
is the tables of the dataflow in `schema/`, the code lists whose `dataflow` is that dataflow in
`codelist/codelists.csv`, and the types of `schema/types.csv` it uses. A change to one dataflow
does not change the version of the other.

`versions.csv` has one row per dataflow:

| Column | Content |
| --- | --- |
| `dataflow` | `SpatialPoints` or `Article23` |
| `version` | `major.minor.patch`, such as `0.4.1` |
| `date` | The date of the version |
| `status` | `draft`, `consultation` or `adopted` |

The prefill of the spatial points is versioned apart, as releases `spatialpoints-prefill-<year>-v…`
([explorer/README.md](../explorer/README.md)); each records the specification version it follows.

## When the version changes

| Change | Level | Examples |
| --- | --- | --- |
| A delivery that was valid may no longer be | major | A table, field, code value or code list removed or renamed; a field made required, or added as required; a type changed or a string shortened; a field that took several values now taking one; a key changed |
| Everything that was valid still is | minor | A table, optional field, code value or code list added; a string lengthened; a field relaxed from required |
| Only text changed | patch | A label, definition, note, condition or caption corrected; the order of the fields |

While a specification is a draft (`0.x.y`), a breaking change raises the minor number only:
`0.4.1` → `0.5.0`. From `1.0.0`, the first version used for reporting, it raises the major number.
A larger bump than needed is always accepted.

## How a change is made

1. Change the CSV files in a branch, as usual.
2. Bump the version of the dataflow in `versions.csv`, and set the date. To see what the changes
   need:

   ```sh
   python reference/versioning.py report origin/main
   ```

3. Open a pull request. The workflow runs `versioning.py check`: it fails if a dataflow changed
   without the bump its changes need, and shows the list of changes in the summary of the run.
4. Merge. The workflow then, for each version that changed:
   * publishes a snapshot of the documentation under `versions/<tag>/`, with a banner saying which
     version it is; the current documentation stays at the root of the site;
   * creates the tag, `spatialpoints-v0.4.1` or `article23-v0.4.1`, on the merge commit;
   * creates a GitHub release with the list of changes since the previous version, the template
     database of the dataflow and a zip of the CSV files. A version whose status is not `adopted`
     is a pre-release.

Do not create these tags by hand: the workflow makes them. Pushing a tag does not run the workflow.

## Where the version shows

* The documentation: the home page of each dataflow, and the Versions section of the rUWWTD page.
* The data explorer: each code list and table.
* The template databases: the `_about` table.
* The prefill releases: `specification_version` in their `manifest.json`.
