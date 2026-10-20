(art23-data-model)=
# Data model overview

:::{warning} Draft
The table structure below is the draft baseline. It is not final.
:::

The dataflow is delivered as three datasets, following the WISE convention used in the other
dataflows: a private dataset for the contact details, the descriptive dataset with the tables of
the draft reporting format, and a documents dataset holding the delivery metadata and every
document the programme refers to.

```{mermaid}
flowchart LR
  subgraph private["Private dataset"]
    Contact
  end
  subgraph descriptive["Descriptive dataset"]
    MSSummary
    SelfAssessment
    Derogation
    Measure["Measure<br/>one row per measure"]
    MeasureObject
    MeasureFinancing
    UWWTP["UWWTP<br/>one row per plant"]
    Agglomeration["Agglomeration<br/>one row per agglomeration"]
  end
  subgraph documents["Documents dataset"]
    dcMetadata
    Reference
    Document
  end
  MSSummary -- "referenceCode" --> Reference
  Derogation -- "referenceCode" --> Reference
  Measure -. "measureReference" .-> Reference
  MeasureObject -- "measureCode" --> Measure
  MeasureFinancing -- "measureCode" --> Measure
  Reference -- "documentCode" --> Document
  dcMetadata -. "licenseDocument" .-> Document
  dcMetadata -. "metadataDocument" .-> Document
  subgraph spatial["Spatial points dataflow"]
    SpUWWTP["UWWTP<br/>name and location"]
    SpAgglomeration["Agglomeration<br/>name and location"]
  end
  UWWTP -- "thematicIdIdentifier" --> SpUWWTP
  Agglomeration -- "thematicIdIdentifier" --> SpAgglomeration
  MeasureObject -- "thematicIdIdentifier" --> SpUWWTP
  MeasureObject -- "thematicIdIdentifier" --> SpAgglomeration
```

The names and locations of treatment plants and agglomerations are not reported in this dataflow.
They are reported in the separate {ref}`spatial-points` dataflow, and the UWWTP, Agglomeration and
MeasureObject tables refer to them by `thematicIdIdentifier`. A code must already have been
accepted there, for the reporting country and the right object type ({ref}`sp-references`).
Earlier reporting stays valid when an object later changes or is retired.

MSSummary and Derogation cite documents, and a measure may do so in `measureReference`. The UWWTP
and Agglomeration tables have no reference fields, and there is no field linking a plant to an
agglomeration. The dashed links are optional: `dcMetadata` points to a document only where the
licence or further metadata is delivered as one.

Measures are the main object of the programme: each measure has one row in Measure, lists the
plants or agglomerations it concerns in MeasureObject, and gives its sources of financing in
MeasureFinancing ({ref}`art23-investments`). This is a proposal ({ref}`art23-oi-measure-model`).

The tables of the descriptive dataset do not carry web addresses. Fields such as
`programmeReference` hold a `referenceCode` pointing into the documents dataset, which resolves to
a document delivered as a hyperlink or as a file uploaded to Reportnet 3
({ref}`art23-oi-documents`).

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
  - One per Member State
  - Required in the first programme; afterwards only if derogation requests change
  - Deadline extensions under Articles 3(2), 6(3), 7(4) and 23(1), and less stringent treatment
    under Article 6(4).
* - {ref}`art23-measure`
  - One per measure (`measureCode` is the primary key)
  - Conditional: required where measures are planned
  - Type, coverage, priority, status, dates and investment cost of each measure.
* - {ref}`art23-measureobject`
  - One per measure and plant or agglomeration
  - Conditional: required for measures with listed plants or agglomerations
  - The plants or agglomerations a measure concerns.
* - {ref}`art23-measurefinancing`
  - One per measure and source of financing
  - Optional
  - Source, funding status and amount of the financing of each measure.
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

The total investment of a Member State is the sum of `investmentCost` over all measures.
