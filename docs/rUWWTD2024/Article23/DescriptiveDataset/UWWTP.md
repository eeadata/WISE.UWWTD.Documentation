(art23-uwwtp)=
# UWWTP

:::{warning} Draft
Draft baseline. Which plants must be listed and the status codelist are still under discussion
(see the open issues linked below). In the proposed measure-first model, measures, dates,
investment costs and funding are reported in {ref}`art23-measure` and its related tables, not
here ({ref}`art23-oi-measure-model`).
:::

**Table status:** Conditional. Required for each treatment plant concerned by a measure in
{ref}`art23-measureobject`.
**Rows:** one row per plant. `thematicIdIdentifier` is the primary key.

The table gives the state of each listed treatment plant: its status and its expected load and
capacity. Each row refers to a treatment plant in the {ref}`sp-uwwtp` table of the
{ref}`spatial-points` dataflow, by its `thematicIdIdentifier`. The plant's name and location are
reported there, not here. A plant reported for the first time is reported there first, and its
code must have been accepted before this table can refer to it ({ref}`sp-references`).

The draft lists plants that are currently non-compliant, face upcoming deadlines, or are at risk
of future non-compliance, for example because of capacity constraints, more stringent
requirements from the risk assessment or urban development. Whether compliant plants with planned
renewal must also be listed is open ({ref}`art23-oi-scope`). The measures planned at a plant are
reported in {ref}`art23-measure` and linked to the plant in {ref}`art23-measureobject`.

```{mermaid} /rUWWTD2024/Article23/mmd/Article23_UWWTP_ClassDiagram.mmd
:name: Article23_UWWTP_ClassDiagram
:caption: Article 23 - UWWTP - draft
:align: center
```

In {numref}`Article23_UWWTP_ClassDiagram`, `[1]` marks the Required fields and `[0..1]` the
Optional ones ({ref}`art23-requirement-status`).

## UWWTP fields

:::{list-table} UWWTP fields
:header-rows: 1
:widths: 22 16 26 10 10 16

* - Notation
  - Label
  - Definition
  - Type
  - Status
  - Condition or codelist
* - `thematicIdIdentifier`
  - Plant code
  - Code of the treatment plant, as in the spatial points dataflow. Primary key. Its identifier
    scheme is always `euUWWTPCode`, the only one used, so the scheme is not reported.
  - wiseIdentifier
  - Required
  - Accepted code of a
    treatment plant of the
    country in
    {ref}`sp-uwwtp`
* - `status`
  - Status
  - Status of the plant at the reference year.
  - PlantAgglomerationStatus
  - Required
  - {ref}`art23-cl-status`
* - `expectedLoad`
  - Expected load
  - Planned load entering the plant at the expected date of compliance.
  - nonNegativeValue (p.e.)
  - Required
  - –
* - `expectedCapacity`
  - Expected capacity
  - Planned organic design capacity of the plant.
  - nonNegativeValue (p.e.)
  - Required
  - –
* - `remarks`
  - Remarks
  - Any relevant comment on the plant.
  - string1000
  - Optional
  - –
:::

## Filling in the table

* **Measures at the plant.** Report each measure in {ref}`art23-measure` and link it to the plant
  in {ref}`art23-measureobject`. Several measures at one plant are several rows there, each with
  its own dates and cost.
* **Reference year.** The draft does not define the reference year of `status`
  ({ref}`art23-oi-reference-dates`).

## Related open issues

* {ref}`art23-oi-scope`, {ref}`art23-oi-status`, {ref}`art23-oi-listed-objects`
* {ref}`art23-oi-loads`, {ref}`art23-oi-measure-model`
