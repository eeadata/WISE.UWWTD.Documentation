(art23-culturalheritageextension)=
# CulturalHeritageExtension

:::{warning} Draft
Legal conditions on this page are taken from Directive (EU) 2024/3019. The table is a proposal,
and field design is not final ({ref}`art23-oi-derogation`).
:::

**Table status:** Conditional. Required in a programme update where a Member State establishes
that preserving cultural heritage makes a deadline impossible to meet. Not part of the first
programme.
**Rows:** one row per agglomeration and area concerned.

Under the third subparagraph of Article 23(1), a Member State that establishes, during the
implementation of its programme, that the need to preserve cultural heritage makes it impossible
to meet the deadline of Article 3(2) or 6(3), or both, in specific areas must update its programme.
The update contains a list of the agglomerations with the areas concerned, a detailed
justification and an adjusted timeline to finalise the required infrastructure in those areas.
Extensions are area-specific, kept as short as possible, and may not exceed 8 years. The updated
programme is submitted by 31 December of the year of the update.

The table holds that list: each row is an agglomeration, an area within it, the deadlines
concerned and the adjusted timeline. Since the Directive places this in an update made during
implementation, the first programme does not ask about it.

```{mermaid} /rUWWTD2024/Article23/mmd/Article23_CulturalHeritageExtension_ClassDiagram.mmd
:name: Article23_CulturalHeritageExtension_ClassDiagram
:caption: Article 23 - CulturalHeritageExtension - draft
:align: center
```

In {numref}`Article23_CulturalHeritageExtension_ClassDiagram`, `[1]` marks the Required fields
and `[1..n]` a Required field that accepts several values ({ref}`art23-requirement-status`).

## CulturalHeritageExtension fields

:::{list-table} CulturalHeritageExtension fields
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
  - Code of the agglomeration concerned, as accepted in the {ref}`spatial-points` dataflow.
  - wiseIdentifier
  - Required
  - –
* - `areaDescription`
  - Area concerned
  - Description of the area within the agglomeration where the deadline cannot be met.
  - string1000
  - Required
  - –
* - `derogationType`
  - Deadline concerned
  - The deadline or deadlines that cannot be met in the area. Select one or both.
  - DerogationType [1..n]
  - Required
  - {ref}`art23-cl-derogation-type`; `article3_2`, `article6_3` or both
* - `adjustedDeadlineYear`
  - Adjusted deadline
  - The year by the end of which the required infrastructure will be finalised in the area.
  - gYear
  - Required
  - –
* - `justificationReference`
  - Justification reference
  - Reference to the detailed justification.
  - referenceCode
  - Required
  - –
:::

## Quality checks

:::{list-table} Proposed quality checks for the CulturalHeritageExtension table
:header-rows: 1
:widths: 10 70 20

* - Code
  - Rule
  - Severity
* - C01
  - `euAgglomerationCode` is an accepted agglomeration of the reporting country in the spatial
    points dataflow ({ref}`sp-references`)
  - Blocker
* - C02
  - `derogationType` is `article3_2` or `article6_3`
  - Error
* - C03
  - `adjustedDeadlineYear` is after 2035 and not more than 8 years after the deadline it extends
  - Error
:::

Whether the 8 years run from the deadline of 31 December 2035 or from a deadline already extended
under Article 3(2) or 6(3) is open ({ref}`art23-oi-derogation`).
