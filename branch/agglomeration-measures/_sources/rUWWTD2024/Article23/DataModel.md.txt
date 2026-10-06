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
    UWWTP["UWWTP<br/>one row per plant"]
    Agglomeration["Agglomeration<br/>one row per agglomeration"]
    OtherInvestment
  end
  subgraph documents["Documents dataset"]
    dcMetadata
    Reference
    Document
  end
  MSSummary -- "referenceCode" --> Reference
  Derogation -- "referenceCode" --> Reference
  Reference -- "documentCode" --> Document
  dcMetadata -. "licenseDocument" .-> Document
  dcMetadata -. "metadataDocument" .-> Document
```

Only MSSummary and Derogation cite documents. The UWWTP, Agglomeration and OtherInvestment
tables have no reference fields, and the UWWTP table has no field linking a plant to an
agglomeration. The dashed links are optional: `dcMetadata` points to a document only where the
licence or further metadata is delivered as one.

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
* - {ref}`art23-uwwtp`
  - One per plant (`code` is the primary key)
  - Conditional: required where investments in treatment plants are planned
  - Measures, status, prioritisation, projected load and capacity, dates, investment and funding.
* - {ref}`art23-agglomeration`
  - One per agglomeration (`code` is the primary key)
  - Conditional: required where investments in collecting systems or individual systems are
    planned
  - Measures, status, prioritisation, projected load, completion date, investment and funding.
* - {ref}`art23-otherinvestment`
  - One or more per Member State, for example one for the whole period or one per year
  - Conditional: can remain empty if all resources are attributed to plants or agglomerations
  - Totals of investments and funding not attributed to a single plant or agglomeration.
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

According to the draft, total investment by a Member State is the sum of the investments reported
in the UWWTP, Agglomeration and OtherInvestment tables.

The draft states that UWWTP rows are linked to plants already reported under Directive
91/271/EEC, and Agglomeration rows to the list of agglomerations. The UWWTP table has no field
linking a plant to an agglomeration.
