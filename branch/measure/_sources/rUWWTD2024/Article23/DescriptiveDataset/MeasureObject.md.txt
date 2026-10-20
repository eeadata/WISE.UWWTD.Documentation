(art23-measureobject)=
# MeasureObject

:::{warning} Draft
Part of the proposed measure-first model ({ref}`art23-oi-measure-model`).
:::

**Table status:** Conditional. Required for every measure with `geographicalCoverage` =
`listedObjects`.
**Rows:** one row per measure and plant or agglomeration. The combination of `measureCode`,
`objectType` and `thematicIdIdentifier` is unique.

The table links each measure in {ref}`art23-measure` to the treatment plants or agglomerations it
concerns. A measure can concern one plant, several plants, or several agglomerations. Plants and
agglomerations are identified by their code in the {ref}`spatial-points` dataflow, which must
already have been accepted there ({ref}`sp-references`).

Unlike the Water Framework Directive, which does not ask for the individual water bodies a measure
concerns, Article 23 needs the plants and agglomerations, since the programme is planned per
agglomeration.

```{mermaid} /rUWWTD2024/Article23/mmd/Article23_MeasureObject_ClassDiagram.mmd
:name: Article23_MeasureObject_ClassDiagram
:caption: Article 23 - MeasureObject - draft
:align: center
```

## MeasureObject fields

:::{list-table} MeasureObject fields
:header-rows: 1
:widths: 22 16 28 12 8 14

* - Notation
  - Label
  - Definition
  - Type
  - Status
  - Condition or codelist
* - `measureCode`
  - Measure code
  - Code of the measure in {ref}`art23-measure`.
  - wiseIdentifier
  - Required
  - Must exist in
    {ref}`art23-measure`
* - `objectType`
  - Object type
  - Whether the object is a treatment plant or an agglomeration. It must match the object type of
    the measure type ({ref}`art23-cl-measure-type`).
  - MeasureObjectType
  - Required
  - {ref}`art23-cl-object-type`
* - `thematicIdIdentifier`
  - Plant or agglomeration code
  - Code of the treatment plant or agglomeration, as in the spatial points dataflow. Its scheme is
    `euUWWTPCode` or `euAgglomerationCode`, following `objectType`, so it is not reported.
  - wiseIdentifier
  - Required
  - Accepted code of the
    country in
    {ref}`sp-uwwtp` or
    {ref}`sp-agglomeration`
:::

## Filling in the table

* **One measure, several objects.** Add one row per plant or agglomeration.
* **One object, several measures.** Add one row per measure.
* **Plants and agglomerations finishing in different years.** A measure has one completion year.
  If the objects under one measure finish in different years, split the measure
  ({ref}`art23-oi-measure-granularity`).
* **State of the object.** The status, expected load and capacity of each listed plant or
  agglomeration are reported in {ref}`art23-uwwtp` and {ref}`art23-agglomeration`
  ({ref}`art23-oi-listed-objects`).
