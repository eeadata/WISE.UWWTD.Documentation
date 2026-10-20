(art23-investments)=
# Reporting measures and costs

:::{warning} Draft
This page describes the proposed measure-first model, which replaces the investment and funding
fields of the UWWTP and Agglomeration tables and the OtherInvestment table
({ref}`art23-oi-measure-model`). Nothing here is decided.
:::

## Measures first

The programme starts from measures. A measure is what the Member State plans to do to reach or
maintain compliance, or to renew existing infrastructure. Each measure has a cost, and that cost
is financed from one or more sources:

* **Measure** ({ref}`art23-measure`): one row per measure, with its type, coverage, priority,
  status, dates and investment cost.
* **MeasureObject** ({ref}`art23-measureobject`): the plants or agglomerations the measure
  concerns, if they are listed.
* **MeasureFinancing** ({ref}`art23-measurefinancing`): where the money comes from, source by
  source, and how far each part is secured.

The {ref}`art23-uwwtp` and {ref}`art23-agglomeration` tables keep only the state of each listed
plant or agglomeration: status, expected load and capacity. This follows the structure of the Water
Framework Directive 4th cycle, where a `Measure` table is the main table and costs are reported
per measure.

```{mermaid}
flowchart LR
  Measure["Measure<br/>type, priority, dates, cost"]
  MeasureObject["MeasureObject<br/>plants or agglomerations"]
  MeasureFinancing["MeasureFinancing<br/>source, status, amount"]
  UWWTP["UWWTP<br/>state of the plant"]
  Agglomeration["Agglomeration<br/>state of the agglomeration"]
  Spatial["Spatial points<br/>code, name, location"]
  MeasureObject -- "measureCode" --> Measure
  MeasureFinancing -- "measureCode" --> Measure
  MeasureObject -- "thematicIdIdentifier" --> Spatial
  UWWTP -- "thematicIdIdentifier" --> Spatial
  Agglomeration -- "thematicIdIdentifier" --> Spatial
```

## Where to report each measure

:::{list-table} Where to report measures
:header-rows: 1
:widths: 45 55

* - Measure
  - Where to report it
* - A measure at one or more identified treatment plants: a new plant, an upgrade to tertiary or
    quaternary treatment, stricter treatment following the risk assessment, energy neutrality,
    or renewal including capacity increase
  - A row in {ref}`art23-measure` with `geographicalCoverage` = `listedObjects`, and one row per
    plant in {ref}`art23-measureobject`
* - A measure in the collecting systems or individual systems of one or more identified
    agglomerations: new collecting systems, storm water overflow reduction, individual systems,
    measures resulting from an IUWMP, or renewal
  - A row in {ref}`art23-measure` with `geographicalCoverage` = `listedObjects`, and one row per
    agglomeration in {ref}`art23-measureobject`
* - A measure for the whole Member State, such as the nationwide renewal of collecting systems
  - A row in {ref}`art23-measure` with `geographicalCoverage` = `national`, no objects listed
* - A measure whose plants or agglomerations are not yet identified, for example new collecting
    systems for agglomerations below 2 000 p.e. newly covered by the Directive
  - A row in {ref}`art23-measure` with `geographicalCoverage` = `unlistedObjects`, and
    `numberOfObjects` if known
* - Contribution from producer responsibility organisations
  - For a measure: a row in {ref}`art23-measurefinancing` with `fundingSource` =
    `producerResponsibilityOrganisation`. National total: `producerResponsibilityContribution` in
    {ref}`art23-mssummary`
* - Investment plans justifying deadline extensions
  - {ref}`art23-derogation`: links to the documents. The measures themselves are reported in
    {ref}`art23-measure`.
:::

Renewal of compliant infrastructure under Article 23(1)(c) is a measure like any other, with the
measure type `renewOrReplaceCollectingSystem` or `renewOrReplaceTreatmentPlant`. It can list the
plants or agglomerations, or be national.

## Cost

* **Investment cost only.** `investmentCost` is capital expenditure. Operational and maintenance
  costs are not reported.
* **Unknown is a valid answer.** If the cost is not yet known, set `costStatus` to `unknown` and
  leave `investmentCost` empty. A Member State that knows it must upgrade ten plants in the next
  ten years but not what it will cost can say so.
* **Estimated or known.** Use `estimated` for estimates and `known` for costs from a project,
  tender or contract.
* **Each cost once.** A cost belongs to one measure. Do not add the cost of a plant to the
  agglomeration it serves, or the reverse. The total investment of the programme is the sum of
  `investmentCost` over all measures.

## Financing

Each row of {ref}`art23-measurefinancing` gives one source of financing for a measure, with its
status and amount:

* **Several sources.** Each source, and each EU fund, is its own row with its own amount, so it is
  clear how much is expected from which fund.
* **Secured or not.** `fundingStatus` says whether the money is secured, applied for or only
  planned, or whether no source has been identified.
* **The gap.** The financing gap of a measure is calculated, not reported: `investmentCost` minus
  the sum of the amounts with `fundingStatus` = `secured`.
* **Funding is not an investment.** Financing amounts describe how a measure's cost is covered.
  They are not added to the total investment.

## Currency

As in the Water Framework Directive, amounts are reported in millions: of euro by euro area
Member States, and of national currency by the others. `millionUnitsOfNationalCurrency` gives the
currency once per measure, and applies to `investmentCost` and to the financing amounts of that
measure. A value below one million uses decimals with a full stop: 10 000 is `0.01`.

(art23-measures-wfd)=
## Reported once

Measures for urban wastewater treatment plants and collecting systems are intended to be reported
once, in this dataflow. Reporters would then no longer report them again in the programme of
measures under the Water Framework Directive. Each measure type corresponds to a WFD key type of
measure and main pressure, derived centrally, so that these measures can still be used in
assessments under that Directive ({ref}`art23-cl-measure-type-wfd`). This depends on agreement
with the Water Framework Directive reporting ({ref}`art23-oi-wfd`).

## Prioritisation

Article 23(1)(b) requires a prioritisation of investments related to:

* the size of the agglomeration; and
* the level of environmental impact of discharges of untreated urban wastewater and the related
  risks for the environment or human health.

The Directive does not link priority to the timing of completion. In the proposed model each
measure has its own `prioritisation`, High, Medium or Low, and `prioritisationReference` in
{ref}`art23-mssummary` points to the national prioritisation methodology.

:::{important}
The draft description adds that "'High' should be used for projects that are scheduled for
earlier completion relative to others". A proposal to remove this link is under consideration,
because high-priority projects can be complex and take longer to complete
({ref}`art23-oi-prioritisation`).
:::

## Dates

* Each measure has its own `expectedCompletionYear`, and optionally `expectedStartYear`. For a
  measure at a treatment plant, the completion year is the year of expected compliance.
* If the plants or agglomerations under one measure finish in different years, split the measure
  ({ref}`art23-oi-measure-granularity`).
* Whether the first programme should cover measures to 2045 or a shorter horizon is open
  ({ref}`art23-oi-reference-dates`).

## Projected loads and capacity

* `expectedLoad` in {ref}`art23-uwwtp` is the planned load entering the plant at the expected date
  of compliance. `expectedCapacity` is the planned organic design capacity in p.e. Hydraulic
  capacity is not requested.
* `expectedLoad` in {ref}`art23-agglomeration` is the expected generated load of the
  agglomeration at the expected date of compliance. `expectedLoadCollected` and
  `expectedLoadIndividualSystems` give the expected percentages collected and addressed through
  individual systems.

Articles 3(3) and 6(5) set out how the load of an agglomeration and the load entering a plant are
calculated: from the maximum average weekly load during the year, excluding unusual weather
situations. The draft does not say whether projected loads should be estimated on the same basis
({ref}`art23-oi-loads`).

(art23-measure-examples)=
## Worked examples

The codes and amounts are invented. `XX` stands for the country code, and all amounts are in
million EUR. Each row is shown as its main values.

**1. Several measures at one plant, on different dates.** Two measures, each with its own dates
and cost, both linked to the same plant.

:::{list-table}
:header-rows: 1
:widths: 22 78

* - Table
  - Row
* - Measure
  - XXM001 · `upgradeTertiaryPhosphorus` · `listedObjects` · `high` · `planned` · start 2027 ·
    completion 2030 · `known` · 12.0 · EUR
* - Measure
  - XXM002 · `upgradeQuaternary` · `listedObjects` · `medium` · `planned` · start 2035 ·
    completion 2040 · `estimated` · 30.0 · EUR
* - MeasureObject
  - XXM001 · `treatmentPlant` · XXUWWTP0101
* - MeasureObject
  - XXM002 · `treatmentPlant` · XXUWWTP0101
* - MeasureFinancing
  - XXM001 · `ownFunds` · `secured` · 6.0
* - MeasureFinancing
  - XXM001 · `europeanUnionFund` · `europeanRegionalDevelopmentFund` · `appliedFor` · 6.0
* - MeasureFinancing
  - XXM002 · `producerResponsibilityOrganisation` · `planned` · 24.0
* - MeasureFinancing
  - XXM002 · `ownFunds` · `planned` · 6.0
:::

**2. It costs 1 000, 500 is secured, the rest is applied for or not yet found.** The gap is
1 000 − 500 = 500, of which 300 is applied for.

:::{list-table}
:header-rows: 1
:widths: 22 78

* - Table
  - Row
* - Measure
  - XXM010 · `upgradeTertiaryNitrogenPhosphorus` · `listedObjects` · `high` · `planned` ·
    completion 2039 · `estimated` · 1 000.0 · EUR
* - MeasureObject
  - XXM010 · `treatmentPlant` · XXUWWTP0201, and one row per further plant concerned
* - MeasureFinancing
  - XXM010 · `ownFunds` · `secured` · 500.0
* - MeasureFinancing
  - XXM010 · `europeanUnionFund` · `cohesionFund` · `appliedFor` · 300.0
* - MeasureFinancing
  - XXM010 · `notIdentified` · `notIdentified` · 200.0
:::

**3. Ten plants to upgrade in ten years, cost not known.** The Member State reports what it knows
and says what it does not. There are no financing rows.

:::{list-table}
:header-rows: 1
:widths: 22 78

* - Table
  - Row
* - Measure
  - XXM020 · `upgradeTertiaryNitrogen` · `unlistedObjects` · `numberOfObjects` 10 · `medium` ·
    `planned` · completion 2036 · `unknown` · no cost
:::

**4. National renewal of collecting systems.** A measure for the whole Member State, with no
objects listed. It replaces the renewal total of the former OtherInvestment table.

:::{list-table}
:header-rows: 1
:widths: 22 78

* - Table
  - Row
* - Measure
  - XXM030 · `renewOrReplaceCollectingSystem` · `national` · `medium` · `ongoing` · start 2027 ·
    completion 2035 · `estimated` · 450.0 · EUR
* - MeasureFinancing
  - XXM030 · `ownFunds` · `planned` · 300.0
* - MeasureFinancing
  - XXM030 · `municipal` · `planned` · 150.0
:::

**5. One measure, several agglomerations, two EU funds.** Each fund is its own row with its own
amount.

:::{list-table}
:header-rows: 1
:widths: 22 78

* - Table
  - Row
* - Measure
  - XXM040 · `newCollectingSystemArticle3_1` · `listedObjects` · `high` · `planned` · start 2028 ·
    completion 2033 · `known` · 9.0 · EUR
* - MeasureObject
  - XXM040 · `agglomeration` · XXAGG0301, XXAGG0302 and XXAGG0303, one row each
* - MeasureFinancing
  - XXM040 · `europeanUnionFund` · `europeanRegionalDevelopmentFund` · `secured` · 4.0
* - MeasureFinancing
  - XXM040 · `europeanUnionFund` · `justTransitionFund` · `secured` · 2.0
* - MeasureFinancing
  - XXM040 · `regional` · `secured` · 3.0
:::

**6. A collecting system and individual systems in one agglomeration.** Two measures, one type
each, both linked to the agglomeration.

:::{list-table}
:header-rows: 1
:widths: 22 78

* - Table
  - Row
* - Measure
  - XXM050 · `newCollectingSystemArticle3_1` · `listedObjects` · `high` · `planned` ·
    completion 2032 · `estimated` · 5.0 · EUR
* - Measure
  - XXM051 · `individualSystemsArticle4` · `listedObjects` · `medium` · `planned` ·
    completion 2034 · `estimated` · 0.8 · EUR
* - MeasureObject
  - XXM050 · `agglomeration` · XXAGG0401
* - MeasureObject
  - XXM051 · `agglomeration` · XXAGG0401
:::

## From the draft fields to the measure model

:::{list-table} Where the draft investment fields go
:header-rows: 1
:widths: 45 55

* - Draft fields
  - In the measure model
* - `treatmentPlantMeasure`, `agglomerationMeasure`
  - `uwwtdMeasureType` in {ref}`art23-measure`, one type per measure
* - `measureText`
  - `measureText` in {ref}`art23-measure`
* - `prioritisation` of plants and agglomerations
  - `prioritisation` in {ref}`art23-measure`
* - `expectedYearStartWork`
  - `expectedStartYear` in {ref}`art23-measure`
* - `expectedYearPerformance`, `completionDate`
  - `expectedCompletionYear` in {ref}`art23-measure`
* - `investment` of plants and agglomerations
  - `investmentCost` in {ref}`art23-measure`
* - `europeanUnionFund`, `europeanUnionFundName`
  - A {ref}`art23-measurefinancing` row with `fundingSource` = `europeanUnionFund` and
    `europeanUnionFundName`
* - `otherPublicFund`, `otherPublicFundSpecification`
  - A {ref}`art23-measurefinancing` row with `fundingSource` = `nationalFederal`, `regional`,
    `municipal` or `otherPublicFunds`
* - `loan`, `loanName`
  - A {ref}`art23-measurefinancing` row with `fundingSource` = `loan`, and `loanName`
* - `producerResponsibilityFund`
  - A {ref}`art23-measurefinancing` row with `fundingSource` =
    `producerResponsibilityOrganisation`
* - OtherInvestment: `collectingSystemNewInvestment`, `treatmentPlantNewInvestment`
  - Measures with `geographicalCoverage` = `national` or `unlistedObjects` and a new-infrastructure
    measure type
* - OtherInvestment: `collectingSystemRenewalInvestment`, `treatmentPlantRenewalInvestment`
  - Measures of type `renewOrReplaceCollectingSystem` or `renewOrReplaceTreatmentPlant`, usually
    `national`
* - OtherInvestment: `startYear`, `endYear`
  - `expectedStartYear` and `expectedCompletionYear` of each measure
* - All amounts in million EUR
  - Millions of national currency, with `millionUnitsOfNationalCurrency`
:::

(art23-quality-checks)=
## Quality checks

:::{list-table} Proposed quality checks for the measure tables
:header-rows: 1
:widths: 10 22 54 14

* - Code
  - Table
  - Check
  - Severity
* - TU01
  - Measure
  - `measureCode` is unique
  - Blocker
* - TU02
  - MeasureObject
  - The combination of `measureCode`, `objectType` and `thematicIdIdentifier` is unique
  - Blocker
* - TU03
  - MeasureFinancing
  - The combination of `measureCode`, `fundingSource`, `europeanUnionFundName` and `loanName` is
    unique
  - Blocker
* - RF01
  - MeasureObject, MeasureFinancing
  - `measureCode` exists in Measure
  - Blocker
* - RF02
  - MeasureObject
  - `thematicIdIdentifier` is accepted in the spatial points dataflow for the reporting country,
    as an agglomeration or a treatment plant following `objectType`; a retired code raises a
    warning ({ref}`sp-references`)
  - Blocker
* - RF03
  - MeasureObject
  - Each listed plant or agglomeration has a row in UWWTP or Agglomeration
  - Error
* - R01
  - Measure
  - `geographicalCoverage` = `listedObjects` has at least one MeasureObject row
  - Error
* - R02
  - Measure
  - `geographicalCoverage` = `national` or `unlistedObjects` has no MeasureObject rows
  - Error
* - R03
  - MeasureObject
  - `objectType` matches the object type of the measure type
  - Error
* - R04
  - Measure
  - `costStatus` = `unknown` if and only if `investmentCost` is empty
  - Error
* - R05
  - Measure
  - `uwwtdMeasureType` = `otherMeasureArticle18_2` requires `measureText`
  - Error
* - R06
  - MeasureFinancing
  - `fundingSource` = `europeanUnionFund` if and only if `europeanUnionFundName` is given
  - Error
* - R07
  - MeasureFinancing
  - The sum of the amounts of a measure does not exceed its `investmentCost`
  - Warning
* - R08
  - Measure
  - `expectedStartYear` is not after `expectedCompletionYear`, and both are between 2027 and 2045
  - Warning
* - R09
  - Measure
  - `numberOfObjects` is given only with `geographicalCoverage` = `unlistedObjects`
  - Error
* - R10
  - MeasureFinancing
  - `fundingSource` = `notIdentified` requires `fundingStatus` = `notIdentified`
  - Error
* - R11
  - MeasureFinancing
  - `loanName` is given only with `fundingSource` = `loan`
  - Error
* - R12
  - Measure, MSSummary
  - `millionUnitsOfNationalCurrency` is given wherever an amount is, and is `EUR` for euro area
    Member States
  - Error
:::
