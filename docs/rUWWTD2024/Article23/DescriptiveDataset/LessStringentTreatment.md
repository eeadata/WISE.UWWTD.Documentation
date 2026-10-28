(art23-lessstringenttreatment)=
# LessStringentTreatment

:::{warning} Draft
Legal conditions on this page are taken from Directive (EU) 2024/3019. Whether this table belongs
in the Article 23 dataflow is open ({ref}`art23-oi-derogation`).
:::

**Table status:** Optional.
**Rows:** one row per agglomeration whose discharges are subject to less stringent treatment.

Under Article 6(4), discharges may be subject to less stringent treatment than secondary treatment
until 31 December 2045 where they go into high mountain waters above 1 500 m, into certain deep
marine waters in less-populated outermost regions, or come from agglomerations of 1 000 to
1 999 p.e. in cold climates. The Member State must provide the Commission with detailed studies
showing that the discharges do not adversely affect the environment and human health.

This is not a deadline extension. It applies to particular discharges, runs to a fixed date, and
the Directive ties it to studies provided to the Commission, not to the programme: Article 23(1)(e)
names only Articles 6(3) and 7(4). The table is therefore Optional, so that a Member State can
provide the studies through this dataflow.

```{mermaid} /rUWWTD2024/Article23/mmd/Article23_LessStringentTreatment_ClassDiagram.mmd
:name: Article23_LessStringentTreatment_ClassDiagram
:caption: Article 23 - LessStringentTreatment - draft
:align: center
```

In {numref}`Article23_LessStringentTreatment_ClassDiagram`, `[1]` marks the Required fields
({ref}`art23-requirement-status`).

## LessStringentTreatment fields

:::{list-table} LessStringentTreatment fields
:header-rows: 1
:widths: 24 16 28 12 8 12

* - Notation
  - Label
  - Definition
  - Type
  - Status
  - Condition or codelist
* - `euAgglomerationCode`
  - Agglomeration
  - Code of the agglomeration whose discharges are subject to less stringent treatment, as
    accepted in the {ref}`spatial-points` dataflow.
  - wiseIdentifier
  - Required
  - –
* - `lessStringentGround`
  - Ground
  - The situation of Article 6(4) that applies.
  - LessStringentGround
  - Required
  - {ref}`art23-cl-less-stringent-ground`
* - `studyReference`
  - Study reference
  - Reference to the detailed study showing that the discharges do not adversely affect the
    environment and human health.
  - referenceCode
  - Required
  - –
:::

The draft had a Required yes/no for the whole Member State and one link to a study. Listing the
agglomerations makes it possible to see which discharges are concerned and on which ground.
