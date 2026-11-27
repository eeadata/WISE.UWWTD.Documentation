---
html_theme.sidebar_secondary.remove: true
---
(ruwwtd-2024)=
# rUWWTD - Directive (EU) 2024/3019

:::{warning} Draft - under review & revision
This documentation is under development and review. Its content is provisional and is **not the
final version**: requirements, tables, fields and codelists may change before the reporting
guidance is finalised. Do not rely on it as final reporting guidance.
:::

```{toctree}
:maxdepth: 2
:hidden:

Article23/index
SpatialPoints/index
```

Documentation of the electronic reporting under the
**revised Urban Wastewater Treatment Directive (rUWWTD)**
{cite:p}`urbanWastewaterTreatmentDirectiveRecast`.

Information will be added as it becomes available.

## Reporting obligations

::::{grid} 2
:gutter: 1 2 3 3
:::{grid-item-card} {ref}`art23`
Draft reporting guidance for national implementation programmes: purpose, timing, the six
reporting tables, field references and open issues.
:::
:::{grid-item-card} {ref}`spatial-points`
Proposal for a dataflow identifying and locating agglomerations, treatment plants and discharge
points, referred to by the Article 22 and Article 23 reporting.
:::
::::

## Data explorer

::::{grid} 1
:::{grid-item-card} {explorer}`Data explorer <index.html>`
**UNDER DEVELOPMENT**
^^^
Browse, search and download the code lists and field tables of the rUWWTD dataflows, an empty
template database of each dataflow, and the provisional prefill of the spatial points dataflow on a
map.
:::
::::

(spec-versions)=
## Versions

Each dataflow specification, its tables, fields and code lists, has a version:

* **Spatial points:** {specversion}`SpatialPoints`
* **Article 23:** {specversion}`Article23`

A version is a number such as `0.4.1`. It changes with every change to the specification, by how
much an earlier delivery is affected:

:::{list-table} When the version changes
:header-rows: 1
:widths: 18 42 40

* - Change
  - When
  - Examples
* - Major (`1.0.0` → `2.0.0`)
  - A delivery that was valid may no longer be.
  - A field, code value or table removed or renamed; a field made required; a type changed or a
    text shortened
* - Minor (`1.0.0` → `1.1.0`)
  - Everything that was valid still is.
  - A code value, an optional field or a table added; a text lengthened
* - Patch (`1.0.0` → `1.0.1`)
  - Only text changed.
  - A label, definition, note or condition corrected
:::

While a specification is a draft, its version starts with `0.`, and a breaking change only raises
the minor number. Version `1.0.0` is the first used for reporting.

Each version is a [release](https://github.com/eeadata/WISE.UWWTD.Documentation/releases) of
this repository, tagged `spatialpoints-v…` or `article23-v…`, with the list of changes, the CSV files
of the tables and code lists, and the template database of the dataflow. The documentation as it was
published with each version stays online, under `versions/<tag>/`. This site always shows the latest
version.

```{bibliography}
:filter: docname in docnames
```
