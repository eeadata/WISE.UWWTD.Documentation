(art23-tables-fields)=
# Tables and fields

:::{warning} Draft
The tables follow the draft baseline and the proposed measure-first model
({ref}`art23-oi-measure-model`). They are not final.
:::

This page shows every table and field of the dataflow on one page: the private dataset and the
descriptive dataset. The documents dataset, which holds the delivery metadata and the documents
that fields of type `referenceCode` point to, is described in {ref}`art23-documents-dataset` and
left out here.

The names and locations of plants and agglomerations are not part of this dataflow: they come from
the {ref}`spatial-points` dataflow. In the diagrams below, the spatial points tables are shown in
green, with the two fields an Article 23 code is matched against: `thematicIdIdentifier`, and its
scheme. A dashed arrow is such a link, labelled with the Article 23 field that holds the code
({ref}`art23-spatial-links`).

`[1]` marks a Required field, `[0..1]` an Optional or Conditional one, and `[0..n]` a field that
accepts several values ({ref}`art23-requirement-status`). Each table name links to its page, which
gives the definition, condition and codelist of every field.

## Private dataset

:::{list-table} Private dataset
:header-rows: 1
:widths: 18 20 62

* - Table
  - Rows
  - Fields
* - {ref}`art23-contact`
  - Preferably one per Member State
  - `name`, `institution`, `phone`, `email`
:::

## Descriptive dataset

```{mermaid} /rUWWTD2024/Article23/mmd/Article23_Tables_Programme_ClassDiagram.mmd
:name: Article23_Tables_Programme_ClassDiagram
:caption: Article 23 - programme and self-assessment - draft
:align: center
```

```{mermaid} /rUWWTD2024/Article23/mmd/Article23_Tables_Derogations_ClassDiagram.mmd
:name: Article23_Tables_Derogations_ClassDiagram
:caption: Article 23 - derogations, with the link to the spatial points - draft
:align: center
```

```{mermaid} /rUWWTD2024/Article23/mmd/Article23_Tables_Measures_ClassDiagram.mmd
:name: Article23_Tables_Measures_ClassDiagram
:caption: Article 23 - measures, costs, plants and agglomerations - draft
:align: center
```

:::{list-table} Descriptive dataset
:header-rows: 1
:widths: 18 20 62

* - Table
  - Rows
  - Fields
* - {ref}`art23-mssummary`
  - One per Member State
  - `situationAt`, `programmeObligation`, `programmeReference`, `prioritisationReference`,
    `article5ManagementPlanReference`, `riskAssessment`, `riskDate`, `riskIdentified`,
    `riskSummaryReference`, `producerResponsibilityContribution`,
    `millionUnitsOfNationalCurrency`, `producerResponsibilityEstimateBasedOn`,
    `contributionPeriod`, `contributionPeriodOther`, `remarks`
* - {ref}`art23-selfassessment`
  - One per Member State
  - `article3Compliance2000andAbove`, `article3Compliance1000to1999`, `article4Compliance`,
    `article5ManagementPlanCount`, `article6Compliance2000andAbove`,
    `article6Compliance1000to1999`, `article7Compliance`, `article8Compliance`
* - {ref}`art23-derogation`
  - One per extension provision
  - `derogationType`, `derogationStatus`, `extendedDeadlineYear`, `eligibilityCriterion`,
    `agglomerationsNotMeeting`, `agglomerationsMeeting`, `loadNotMeeting`, `loadMeeting`,
    `reasonType`, `reasonReference`, `investmentPlanReference`
* - {ref}`art23-culturalheritageextension`
  - One per agglomeration and area
  - `euAgglomerationCode`, `areaDescription`, `derogationType`, `adjustedDeadlineYear`,
    `justificationReference`
* - {ref}`art23-lessstringenttreatment`
  - One per agglomeration
  - `euAgglomerationCode`, `lessStringentGround`, `studyReference`
* - {ref}`art23-measure`
  - One per measure
  - `measureCode`, `measureName`, `measureNameLanguage`, `measureReference`, `uwwtdMeasureType`,
    `measureText`, `geographicalCoverage`, `euUWWTPCode`, `euAgglomerationCode`,
    `prioritisation`, `implementationStatus`, `implementationPeriod`,
    `costStatus`, `remarks`
* - {ref}`art23-measurefinancing`
  - One per measure and source of financing
  - `measureCode`, `fundingSource`, `europeanUnionFundName`, `loanName`, `fundingStatus`,
    `totalCapitalExpenditure1stCycle`, `totalCapitalExpenditureAfter1stCycle`,
    `millionUnitsOfNationalCurrency`
* - {ref}`art23-uwwtp`
  - One per plant
  - `thematicIdIdentifier`, `status`, `expectedLoad`, `expectedCapacity`, `remarks`
* - {ref}`art23-agglomeration`
  - One per agglomeration
  - `thematicIdIdentifier`, `status`, `expectedLoad`, `expectedLoadCollected`,
    `expectedLoadIndividualSystems`, `remarks`
:::
