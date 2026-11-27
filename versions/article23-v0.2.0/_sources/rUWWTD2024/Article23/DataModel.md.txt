(art23-data-model)=
# Data model overview

:::{warning} Draft
The table structure below is the draft baseline. It is not final.
:::

The dataflow is delivered as three datasets, following the WISE convention used in the other
dataflows: a private dataset for the contact details, the descriptive dataset with the tables of
the draft reporting format, and a documents dataset holding the delivery metadata and every
document the programme refers to.

## Datasets and tables

```{mermaid} /rUWWTD2024/Article23/mmd/Article23_Datasets_Flowchart.mmd
:name: Article23_Datasets_Flowchart
:caption: Article 23 - the three datasets and their tables - draft
:align: center
```

MSSummary, the three derogation tables and Measure cite documents in their `referenceCode`
fields, such as `programmeReference`: a code pointing to a row of Reference, a place within a
document of the documents dataset. The tables of the descriptive dataset do not carry web
addresses; each document is delivered as a hyperlink or as a file uploaded to Reportnet 3
({ref}`art23-oi-documents`). The dashed link is optional: `dcMetadata` points to a document only
where the licence or further metadata is delivered as one.

Measures are the main object of the programme: each measure has one row in Measure, lists the
plants or agglomerations it concerns, and gives its sources of financing in MeasureFinancing
({ref}`art23-investments`). This is a proposal ({ref}`art23-oi-measure-model`).

(art23-spatial-links)=
## Links to the spatial points

The names and locations of treatment plants and agglomerations are not reported in this dataflow.
They are reported once, in the {ref}`spatial-points` dataflow, where each object has a code,
`thematicIdIdentifier`, and the scheme of that code, `thematicIdIdentifierScheme`: `euUWWTPCode`
for a treatment plant, `euAgglomerationCode` for an agglomeration and `euDischargePointCode` for a
discharge point ({ref}`sp-cl-scheme`).

Article 23 refers to a plant or an agglomeration only by that code. Every link between the two
dataflows is the same match: the code in the Article 23 field equals the `thematicIdIdentifier` of
a spatial points object of the expected scheme.

```{mermaid} /rUWWTD2024/Article23/mmd/Article23_SpatialLinks_Flowchart.mmd
:name: Article23_SpatialLinks_Flowchart
:caption: Article 23 - links to the spatial points, by thematicIdIdentifier and scheme - draft
:align: center
```

:::{list-table} Links from Article 23 to the spatial points
:header-rows: 1
:widths: 34 22 44

* - Article 23 field
  - Holds
  - Matched to, in the spatial points
* - `thematicIdIdentifier` in {ref}`art23-uwwtp`;
    `euUWWTPCode` in {ref}`art23-measure`
  - The code of a treatment plant
  - `thematicIdIdentifier` of a row of {ref}`sp-uwwtp` whose `thematicIdIdentifierScheme` is
    `euUWWTPCode`
* - `thematicIdIdentifier` in {ref}`art23-agglomeration`;
    `euAgglomerationCode` in {ref}`art23-measure`, {ref}`art23-culturalheritageextension` and
    {ref}`art23-lessstringenttreatment`
  - The code of an agglomeration
  - `thematicIdIdentifier` of a row of {ref}`sp-agglomeration` whose `thematicIdIdentifierScheme`
    is `euAgglomerationCode`
* - None
  - The code of a discharge point
  - {ref}`sp-dischargepoint`, scheme `euDischargePointCode`: not referred to by Article 23; the
    Article 22 reporting is expected to use it
:::

In the UWWTP and Agglomeration tables of Article 23 the field keeps the spatial points name,
`thematicIdIdentifier`, and the table says which scheme applies. Elsewhere the field is named
after its scheme, `euUWWTPCode` or `euAgglomerationCode`, and a measure may list several codes. A
code must already have been accepted in the spatial points, for the reporting country and the
right scheme ({ref}`sp-references`). Earlier reporting stays valid when an object later changes or
is retired. There is no field linking a plant to an agglomeration in Article 23.

## Tables

:::{list-table} Tables of the three datasets
:header-rows: 1
:widths: 18 18 22 42

* - Table
  - Rows
  - Table status
  - Content
* - {ref}`art23-contact` (private)
  - Preferably one per Member State; more allowed
  - Required
  - Reporting contact details.
* - {ref}`art23-mssummary`
  - One per Member State
  - Required
  - Whether a programme is required, references to it and to the prioritisation methodology,
    risk assessment and PRO contribution.
* - {ref}`art23-selfassessment`
  - One per Member State
  - Required
  - National self-assessment of compliance with Articles 3 to 8.
* - {ref}`art23-derogation`
  - One per extension provision: Articles 3(2), 6(3) and 7(4) (`derogationType` is the primary
    key)
  - Required in the first programme; afterwards only if derogation requests change
  - Whether each deadline is extended, to which year, and the numbers and documents justifying it.
* - {ref}`art23-culturalheritageextension`
  - One per agglomeration and area
  - Conditional: required in a programme update where cultural heritage makes the deadline of
    Article 3(2) or 6(3) impossible to meet
  - Agglomerations and areas concerned, adjusted deadline and justification (Article 23(1), third
    subparagraph).
* - {ref}`art23-lessstringenttreatment`
  - One per agglomeration
  - Optional
  - Agglomerations whose discharges are subject to less stringent treatment under Article 6(4),
    with the ground and the study.
* - {ref}`art23-measure`
  - One per measure (`measureCode` is the primary key)
  - Conditional: required where measures are planned
  - Type, coverage and listed plants or agglomerations, priority, status, dates and cost status
    of each measure.
* - {ref}`art23-measurefinancing`
  - One per measure and source of financing
  - Required: at least one per measure
  - Capital expenditure of each measure per cycle, by source of financing, with its funding
    status.
* - {ref}`art23-uwwtp`
  - One per plant (`thematicIdIdentifier` is the primary key)
  - Conditional: required for each plant concerned by a measure
  - Status, projected load and capacity.
* - {ref}`art23-agglomeration`
  - One per agglomeration (`thematicIdIdentifier` is the primary key)
  - Conditional: required for each agglomeration concerned by a measure
  - Status and projected load.
* - {ref}`art23-dcmetadata` (documents)
  - One per delivery
  - Required
  - Dublin Core metadata about the delivery.
* - {ref}`art23-reference` (documents)
  - One per cited place in a document
  - Conditional: required where a reporting table cites a document
  - Chapter, section or bookmark within a document.
* - {ref}`art23-document` (documents)
  - One per document
  - Conditional: required where a reporting table cites a document
  - The document itself, as a hyperlink or an uploaded file.
:::

The total investment of a Member State is the sum of `totalCapitalExpenditure1stCycle` and
`totalCapitalExpenditureAfter1stCycle` over all the rows of {ref}`art23-measurefinancing`.
