(art23-tables-fields)=
# Tables and fields

:::{warning} Draft
The tables follow the draft baseline and the proposed measure-first model
({ref}`art23-oi-measure-model`). They are not final.
:::

This page shows every table and field of the dataflow on one page: the private dataset and the
descriptive dataset. The documents dataset, which holds the delivery metadata and the documents
that fields of type `referenceCode` point to, is described in {ref}`art23-documents-dataset` and
left out here. The names and locations of plants and agglomerations are not part of this dataflow:
they come from the {ref}`spatial-points` dataflow.

```{mermaid} /rUWWTD2024/Article23/mmd/Article23_Tables_ClassDiagram.mmd
:name: Article23_Tables_ClassDiagram
:caption: Article 23 - all tables and fields, without the documents dataset - draft
:align: center
```

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
  - `article3Compliance`, `article3Compliance1000to1999`, `article4Compliance`,
    `article5ManagementPlanCount`, `article6Compliance`, `article6Compliance1000to1999`,
    `article7Compliance`, `article8Compliance`
* - {ref}`art23-derogation`
  - One per Member State
  - `article3_2DeadlineExtension`, `article3_2CompleteCollectingSystem`,
    `article3_2NonCompleteCollectingSystem`, `article3_2CompleteCollectingSystemLoad`,
    `article3_2NonCompleteCollectingSystemLoad`, `article3_2InvestmentPlanReference`,
    `article3_2ExtensionReasonReference`, `article3_2CulturalHeritage`,
    `article3_2CulturalHeritageReference`, `article6_3CulturalHeritage`,
    `article6_3CulturalHeritageReference`, `article6_3DeadlineExtension`,
    `article6_3AgglomerationsWithSecondaryTreatment`,
    `article6_3AgglomerationsWithoutSecondaryTreatment`, `article6_3LoadWithSecondaryTreatment`,
    `article6_3LoadWithoutSecondaryTreatment`, `article6_3InvestmentPlanReference`,
    `article6_3ExtensionReasonReference`, `article6_4LessStringentTreatment`,
    `article6_4LessStringentStudyReference`, `article7_4DeadlineExtension`,
    `article7_4AgglomerationsWithTertiaryTreatment`,
    `article7_4AgglomerationsWithoutTertiaryTreatment`, `article7_4InvestmentPlanReference`,
    `article7_4ExtensionReasonReference`
* - {ref}`art23-measure`
  - One per measure
  - `measureCode`, `measureName`, `measureNameLanguage`, `measureReference`, `uwwtdMeasureType`,
    `measureText`, `geographicalCoverage`, `numberOfObjects`, `prioritisation`,
    `implementationStatus`, `expectedStartYear`, `expectedCompletionYear`, `costStatus`,
    `investmentCost`, `millionUnitsOfNationalCurrency`, `remarks`
* - {ref}`art23-measureobject`
  - One per measure and plant or agglomeration
  - `measureCode`, `objectType`, `thematicIdIdentifier`
* - {ref}`art23-measurefinancing`
  - One per measure and source of financing
  - `measureCode`, `fundingSource`, `europeanUnionFundName`, `loanName`, `fundingStatus`, `amount`
* - {ref}`art23-uwwtp`
  - One per plant
  - `thematicIdIdentifier`, `status`, `expectedLoad`, `expectedCapacity`, `remarks`
* - {ref}`art23-agglomeration`
  - One per agglomeration
  - `thematicIdIdentifier`, `status`, `expectedLoad`, `expectedLoadCollected`,
    `expectedLoadIndividualSystems`, `remarks`
:::
