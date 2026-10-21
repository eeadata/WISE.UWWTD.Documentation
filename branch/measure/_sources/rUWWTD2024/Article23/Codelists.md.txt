(art23-codelists)=
# Codelists

:::{warning} Draft
All codelists on this page are proposals, and several are under review
({ref}`art23-open-issues`).
:::

Every codelist below is named as a WISE enumeration type, given under the heading, and gives for
each value the notation to report, a short label and a definition, following
{ref}`art23-notation`.

Each codelist field takes one value unless its type is marked `[0..n]`.

(art23-cl-deadline-ext)=
## Deadline extension - Articles 3(2) and 6(3)

**Type:** `DeadlineExtension`

Used by `article3_2DeadlineExtension` and `article6_3DeadlineExtension`.

:::{list-table} Proposed deadline extension values - Articles 3(2) and 6(3)
:header-rows: 1
:widths: 20 20 32 28

* - Notation
  - Label
  - Definition
  - Notes
* - `noDerogation`
  - No derogation
  - No extension of the deadline is requested.
  - Report this value where the deadline is met without an extension.
* - `oneYear`
  - 1 year
  - The deadline is extended by one whole year.
  - One value per whole year, from `oneYear` to `fourteenYears`.
* - `twoYears`
  - 2 years
  - The deadline is extended by two whole years.
  - –
* - `...`
  - ...
  - Values continue for each whole year.
  - `threeYears` to `thirteenYears` follow the same pattern.
* - `fourteenYears`
  - 14 years
  - The deadline is extended by fourteen whole years.
  - Available to Bulgaria, Croatia and Romania only.
:::

Under the Directive, the maximum extension is 8 or 10 years depending on the situation on
1 January 2025, or 12 or 14 years for Bulgaria, Croatia and Romania.

(art23-cl-deadline-ext-7-4)=
## Deadline extension - Article 7(4)

**Type:** `DeadlineExtensionArticle7_4`

Used by `article7_4DeadlineExtension`.

:::{list-table} Proposed deadline extension values - Article 7(4)
:header-rows: 1
:widths: 20 20 32 28

* - Notation
  - Label
  - Definition
  - Notes
* - `noDerogation`
  - No derogation
  - No extension of the deadline is requested.
  - –
* - `oneYear`
  - 1 year
  - The deadline is extended by one whole year.
  - One value per whole year, from `oneYear` to `eightYears`.
* - `...`
  - ...
  - Values continue for each whole year.
  - `twoYears` to `sevenYears` follow the same pattern.
* - `eightYears`
  - 8 years
  - The deadline is extended by eight whole years.
  - The maximum extension under Article 7(4).
:::

(art23-cl-compliance-share)=
## Compliance share - Articles 3 and 6, agglomerations of 2 000 p.e. and above

**Type:** `ComplianceShare`

Used by `article3Compliance` and `article6Compliance` in {ref}`art23-selfassessment`.

:::{list-table} Proposed compliance share values
:header-rows: 1
:widths: 22 20 34 24

* - Notation
  - Label
  - Definition
  - Notes
* - `lessThan50`
  - Less than 50%
  - Fewer than half of the agglomerations comply.
  - –
* - `from50to75`
  - 50-75%
  - Between 50 % and 75 % of the agglomerations comply.
  - –
* - `from76to85`
  - 76-85%
  - Between 76 % and 85 % of the agglomerations comply.
  - –
* - `from86to95`
  - 86-95%
  - Between 86 % and 95 % of the agglomerations comply.
  - –
* - `from96to99`
  - 96-99%
  - Between 96 % and 99 % of the agglomerations comply.
  - –
* - `full`
  - 100%
  - All agglomerations comply.
  - –
:::

(art23-cl-compliance-share-estimated)=
## Estimated compliance share - Articles 3, 6, 7 and 8

**Type:** `ComplianceShareEstimated`

Used by `article3Compliance1000to1999`, `article6Compliance1000to1999`, `article7Compliance` and
`article8Compliance` in {ref}`art23-selfassessment`. The wider bands reflect that detailed data
may not
yet be available for these agglomerations and plants.

:::{list-table} Proposed estimated compliance share values
:header-rows: 1
:widths: 22 20 34 24

* - Notation
  - Label
  - Definition
  - Notes
* - `none`
  - 0%
  - None comply.
  - –
* - `from1to25`
  - 1-25%
  - Up to a quarter comply.
  - –
* - `from26to50`
  - 26-50%
  - Between a quarter and a half comply.
  - –
* - `from51to75`
  - 51-75%
  - Between a half and three quarters comply.
  - –
* - `from76to100`
  - 76-100%
  - More than three quarters comply.
  - –
:::

(art23-cl-risk-assessment)=
## Risk assessment

**Type:** `RiskAssessment`

Used by `riskAssessment` in {ref}`art23-mssummary`.

:::{list-table} Proposed risk assessment values
:header-rows: 1
:widths: 20 20 36 24

* - Notation
  - Label
  - Definition
  - Notes
* - `yes`
  - Yes
  - A risk assessment has been carried out in accordance with Article 18.
  - The date, the identified risks and the summary are then required.
* - `partially`
  - Partially
  - A risk assessment covers only some urban wastewater discharges.
  - –
* - `no`
  - No
  - No risk assessment has been carried out.
  - –
:::

(art23-cl-contribution-period)=
## Contribution period

**Type:** `ContributionPeriod`

Used by `contributionPeriod` in {ref}`art23-mssummary`. Several values may be selected.

:::{list-table} Proposed contribution period values
:header-rows: 1
:widths: 20 20 36 24

* - Notation
  - Label
  - Definition
  - Notes
* - `endOf2033`
  - End of 2033
  - The planned resources cover the requirements due by the end of 2033.
  - Interim deadline of Articles 8(1) and 8(4).
* - `endOf2036`
  - End of 2036
  - The planned resources cover the requirements due by the end of 2036.
  - Interim deadline of Article 8(4).
* - `endOf2039`
  - End of 2039
  - The planned resources cover the requirements due by the end of 2039.
  - Interim deadline of Articles 8(1) and 8(4).
* - `endOf2045`
  - End of 2045
  - The planned resources cover the requirements due by the end of 2045.
  - Final deadline of Articles 8(1) and 8(4).
* - `other`
  - Other
  - Another period, explained in `contributionPeriodOther`.
  - –
:::

(art23-cl-status)=
## Plant and agglomeration status

**Type:** `PlantAgglomerationStatus`

Used by the `status` field of the {ref}`art23-uwwtp` and {ref}`art23-agglomeration` tables.

:::{list-table} Proposed status values
:header-rows: 1
:widths: 26 22 32 20

* - Notation
  - Label
  - Definition
  - Notes
* - `compliant`
  - Compliant (C)
  - Articles 3 to 8 compliant; Article 18 requirements fulfilled or not applicable.
  - –
* - `nonCompliant`
  - Non-compliant (NC)
  - Articles 3 to 8 non-compliant; Article 18 requirements fulfilled or not applicable.
  - –
* - `pendingDeadline`
  - Pending deadline (PD)
  - Pending deadline: time remains for submission of the application.
  - –
* - `compliantArticle18NotMet`
  - Compliant, Article 18 not met (C+A18)
  - Articles 3 to 8 compliant; more stringent Article 18 requirements not met.
  - –
* - `nonCompliantArticle18NotMet`
  - Non-compliant, Article 18 not met (NC+A18)
  - Articles 3 to 8 non-compliant; more stringent Article 18 requirements not met.
  - –
:::

(art23-cl-measure-type)=
## Measure type

**Type:** `UWWTDMeasureType`

Used by the `uwwtdMeasureType` field of the {ref}`art23-measure` table. One or more values per
measure, as in the draft format, all for the same kind of object. The
codelist brings together the former treatment plant and agglomeration measure codelists; the
renewal value, which both had, is split into one value for collecting systems and one for
treatment plants. The notes give the article and the object type: a measure listing plants or
agglomerations in {ref}`art23-measureobject` must list objects of that type.

The name is prefixed with `UWWTD` because the Water Framework Directive codelist `MeasureType`
classifies measures differently, by their nature (legislative, technical, economic and so on).

:::{list-table} Proposed measure types
:header-rows: 1
:widths: 30 24 26 20

* - Notation
  - Label
  - Definition
  - Notes
* - `newCollectingSystemArticle3_1`
  - New collecting systems, 2 000 p.e. and above
  - New collecting systems in agglomerations of 2 000 p.e. and above.
  - Article 3(1). Agglomeration.
* - `newCollectingSystemArticle3_2`
  - New collecting systems, 1 000 to 1 999 p.e.
  - New collecting systems in agglomerations of 1 000 to 1 999 p.e.
  - Article 3(2). Agglomeration.
* - `stormWaterOverflowReduction`
  - Measures to reduce storm water overflows
  - Measures to reduce storm water overflows from collecting systems, so that they meet Part A
    of Annex I.
  - Article 3(4). Agglomeration.
* - `individualSystemsArticle4`
  - Measures for individual systems
  - Measures for individual systems used where a collecting system is not established.
  - Article 4. Agglomeration.
* - `managementPlanMeasures`
  - Measures resulting from a management plan
  - Measures resulting from an integrated urban wastewater management plan.
  - Article 5 and Annex V. Agglomeration.
* - `newCollectingSystemRiskBased`
  - New collecting systems, below 1 000 p.e.
  - New collecting systems in agglomerations below 1 000 p.e., on the basis of the risk
    assessment.
  - Article 18(2)(b). Agglomeration.
* - `renewOrReplaceCollectingSystem`
  - Renew or replace existing collecting systems
  - Renewal or replacement of existing collecting system infrastructure.
  - Article 23(1)(c). Agglomeration.
* - `newPlantArticle6_1`
  - New plant, agglomerations of 2 000 p.e. and above
  - A new treatment plant providing secondary treatment.
  - Article 6(1). Treatment plant.
* - `newPlantArticle6_3`
  - New plant, agglomerations of 1 000 to 1 999 p.e.
  - A new treatment plant providing secondary treatment.
  - Article 6(3). Treatment plant.
* - `upgradeTertiaryNitrogen`
  - Upgrade to tertiary treatment (N)
  - Upgrade to tertiary treatment for nitrogen.
  - Article 7(1), 7(3). Treatment plant.
* - `upgradeTertiaryPhosphorus`
  - Upgrade to tertiary treatment (P)
  - Upgrade to tertiary treatment for phosphorus.
  - Article 7(1), 7(3). Treatment plant.
* - `upgradeTertiaryNitrogenPhosphorus`
  - Upgrade to tertiary treatment (N+P)
  - Upgrade to tertiary treatment for both nitrogen and phosphorus.
  - Article 7(1), 7(3). Treatment plant.
* - `upgradeQuaternary`
  - Upgrade to quaternary treatment
  - Upgrade to quaternary treatment for micropollutants.
  - Article 8(1), 8(4). Treatment plant.
* - `energyNeutrality`
  - Energy neutrality
  - Measures to meet the renewable energy targets.
  - Article 11(2). Treatment plant.
* - `secondaryTreatmentRiskBased`
  - Secondary treatment, agglomerations below 1 000 p.e.
  - Applying secondary treatment on the basis of the risk assessment.
  - Article 18(2)(c). Treatment plant.
* - `tertiaryTreatmentRiskBased`
  - Tertiary treatment, agglomerations below 10 000 p.e.
  - Applying tertiary treatment on the basis of the risk assessment.
  - Article 18(2)(d). Treatment plant.
* - `quaternaryTreatmentRiskBased`
  - Quaternary treatment, agglomerations below 10 000 p.e.
  - Applying quaternary treatment on the basis of the risk assessment.
  - Article 18(2)(e). Treatment plant.
* - `stricterTreatmentRiskBased`
  - Stricter treatment requirements
  - Applying stricter requirements for treatment on the basis of the risk assessment.
  - Article 18(2)(g). Treatment plant.
* - `otherMeasureArticle18_2`
  - Other appropriate measure
  - Another appropriate measure under Article 18(2). Describe it in `measureText`.
  - Article 18(2). Either.
* - `renewOrReplaceTreatmentPlant`
  - Renew or replace existing treatment plants
  - Renewal or replacement of an existing treatment plant, including capacity increase.
  - Article 23(1)(c). Treatment plant.
:::

(art23-cl-measure-type-wfd)=
### Correspondence with the Water Framework Directive

Measures for treatment plants and collecting systems are intended to be reported once, in this
dataflow, and not again in the programme of measures under the Water Framework Directive
({ref}`art23-oi-wfd`). So that they can still be used in assessments under that Directive, each
measure type corresponds to a WFD key type of measure (`mainKeyTypeOfMeasure`) and main pressure
(`mainPressureType`), derived centrally and not reported. The correspondence below is a proposal,
to be confirmed.

:::{list-table} Proposed correspondence with WFD key types of measures
:header-rows: 1
:widths: 34 22 22 22

* - Measure type
  - WFD key type of measure
  - WFD main pressure
  - Notes
* - `newCollectingSystemArticle3_1`
  - `G`
  - `P1-1`
  - Measure to control point source discharges.
* - `newCollectingSystemArticle3_2`
  - `G`
  - `P1-1`
  - Measure to control point source discharges.
* - `stormWaterOverflowReduction`
  - `G`
  - `P1-2`
  - Measure to control point source discharges.
* - `individualSystemsArticle4`
  - `G`
  - `P1-1`
  - Measure to control point source discharges.
* - `managementPlanMeasures`
  - `G`
  - `P1-2`
  - Measure to control point source discharges.
* - `newCollectingSystemRiskBased`
  - `G`
  - `P1-1`
  - Measure to control point source discharges.
* - `renewOrReplaceCollectingSystem`
  - `G`
  - `P1-1`
  - Measure to control point source discharges.
* - `newPlantArticle6_1`
  - `X01`
  - `P1-1`
  - Construction or upgrades of wastewater treatment plants.
* - `newPlantArticle6_3`
  - `X01`
  - `P1-1`
  - Construction or upgrades of wastewater treatment plants.
* - `upgradeTertiaryNitrogen`
  - `X01`
  - `P1-1`
  - Construction or upgrades of wastewater treatment plants.
* - `upgradeTertiaryPhosphorus`
  - `X01`
  - `P1-1`
  - Construction or upgrades of wastewater treatment plants.
* - `upgradeTertiaryNitrogenPhosphorus`
  - `X01`
  - `P1-1`
  - Construction or upgrades of wastewater treatment plants.
* - `upgradeQuaternary`
  - `X01`
  - `P1-1`
  - Construction or upgrades of wastewater treatment plants.
* - `energyNeutrality`
  - –
  - –
  - No direct equivalent; to be decided.
* - `secondaryTreatmentRiskBased`
  - `X01`
  - `P1-1`
  - Construction or upgrades of wastewater treatment plants.
* - `tertiaryTreatmentRiskBased`
  - `X01`
  - `P1-1`
  - Construction or upgrades of wastewater treatment plants.
* - `quaternaryTreatmentRiskBased`
  - `X01`
  - `P1-1`
  - Construction or upgrades of wastewater treatment plants.
* - `stricterTreatmentRiskBased`
  - `X01`
  - `P1-1`
  - Construction or upgrades of wastewater treatment plants.
* - `otherMeasureArticle18_2`
  - –
  - –
  - No direct equivalent; to be decided.
* - `renewOrReplaceTreatmentPlant`
  - `X01`
  - `P1-1`
  - Construction or upgrades of wastewater treatment plants.
:::

`P1-1` is the WFD pressure "Point - Urban waste water" and `P1-2` "Point - Storm overflows". A
measure with several types corresponds to the key types of all of them. Where those differ, how
the measure is classified under the Water Framework Directive is open ({ref}`art23-oi-wfd`).

(art23-cl-coverage)=
## Geographical coverage

**Type:** `UWWTDGeographicCoverage`

Used by `geographicalCoverage` in {ref}`art23-measure`. Prefixed with `UWWTD` because the
corresponding Water Framework Directive codelist, `WFDGeographicCoverage`, has other values.

:::{list-table} Proposed geographical coverage values
:header-rows: 1
:widths: 24 22 34 20

* - Notation
  - Label
  - Definition
  - Notes
* - `national`
  - National
  - The measure applies to the whole Member State; no plants or agglomerations are listed.
  - No rows in {ref}`art23-measureobject`.
* - `listedObjects`
  - Listed plants or agglomerations
  - The measure applies to the plants or agglomerations listed in {ref}`art23-measureobject`.
  - At least one row in {ref}`art23-measureobject`.
* - `unlistedObjects`
  - Plants or agglomerations not yet identified
  - The measure applies to plants or agglomerations that are not yet identified.
  - Give `numberOfObjects` if known.
:::

(art23-cl-implementation-status)=
## Implementation status

**Type:** `PlannedOngoingExecutedCancelled`

Used by `implementationStatus` in {ref}`art23-measure`. The same codelist as in the Water Framework
Directive 4th cycle.

:::{list-table} Implementation status values
:header-rows: 1
:widths: 24 22 34 20

* - Notation
  - Label
  - Definition
  - Notes
* - `planned`
  - Planned
  - The measure is planned and has not started.
  - –
* - `ongoing`
  - Ongoing
  - The measure has started and is not yet completed.
  - –
* - `executed`
  - Executed
  - The measure has been completed.
  - Used in later programmes.
* - `cancelled`
  - Cancelled
  - The measure has been cancelled.
  - Used in later programmes.
:::

(art23-cl-cost-status)=
## Cost status

**Type:** `CostStatus`

Used by `costStatus` in {ref}`art23-measure`.

:::{list-table} Proposed cost status values
:header-rows: 1
:widths: 24 22 34 20

* - Notation
  - Label
  - Definition
  - Notes
* - `known`
  - Known
  - The cost comes from a project, tender or contract.
  - –
* - `estimated`
  - Estimated
  - The cost is an estimate.
  - –
* - `unknown`
  - Unknown
  - The cost is not yet known.
  - `investmentCost` stays empty.
:::

(art23-cl-object-type)=
## Object type

**Type:** `MeasureObjectType`

Used by `objectType` in {ref}`art23-measureobject`.

:::{list-table} Proposed object type values
:header-rows: 1
:widths: 24 22 34 20

* - Notation
  - Label
  - Definition
  - Notes
* - `agglomeration`
  - Agglomeration
  - The object is an agglomeration.
  - Code from {ref}`sp-agglomeration`.
* - `treatmentPlant`
  - Treatment plant
  - The object is an urban wastewater treatment plant.
  - Code from {ref}`sp-uwwtp`.
:::

(art23-cl-priority)=
## Priority

**Type:** `Priority`

Used by the `prioritisation` field of the {ref}`art23-measure` table.

:::{list-table} Proposed priority values
:header-rows: 1
:widths: 20 20 32 28

* - Notation
  - Label
  - Definition
  - Notes
* - `high`
  - High
  - High priority measure.
  - Related to the size of the agglomeration and the level of environmental impact.
* - `medium`
  - Medium
  - Medium priority measure.
  - –
* - `low`
  - Low
  - Low priority measure.
  - –
:::

The draft does not define the boundaries between the three levels. See {ref}`art23-investments`
and {ref}`art23-oi-prioritisation`.

(art23-cl-eu-funds)=
## EU funds

**Type:** `EUFund`

Used by `europeanUnionFundName` in {ref}`art23-measurefinancing`.

:::{list-table} Proposed EU fund values
:header-rows: 1
:widths: 34 30 24 12

* - Notation
  - Label
  - Definition
  - Notes
* - `europeanAgriculturalFundForRuralDevelopment`
  - European Agricultural Fund for Rural Development
  - Funding under the European Agricultural Fund for Rural Development.
  - –
* - `europeanRegionalDevelopmentFund`
  - European Regional Development Fund
  - Funding under the European Regional Development Fund.
  - –
* - `interreg`
  - Interreg
  - Funding under the Interreg programmes.
  - –
* - `cohesionFund`
  - Cohesion Fund
  - Funding under the Cohesion Fund.
  - –
* - `justTransitionFund`
  - Just Transition Fund
  - Funding under the Just Transition Fund.
  - –
* - `recoveryAndResilienceFacility`
  - Recovery and Resilience Facility
  - Funding under the Recovery and Resilience Facility.
  - –
* - `horizonEurope`
  - Horizon Europe
  - Funding under Horizon Europe.
  - –
* - `investEuFund`
  - InvestEU fund
  - Funding under the InvestEU fund.
  - –
* - `europeanInvestmentBank`
  - European Investment Bank
  - Funding from the European Investment Bank.
  - –
* - `otherEuropeanUnionFunds`
  - Other EU funds
  - Any other Union fund not listed above.
  - –
:::

(art23-cl-funding-source)=
## Funding source

**Type:** `FundingSource`

Used by `fundingSource` in {ref}`art23-measurefinancing`. It replaces the former other public fund
codelist, whose values are kept.

:::{list-table} Proposed funding source values
:header-rows: 1
:widths: 30 22 30 18

* - Notation
  - Label
  - Definition
  - Notes
* - `ownFunds`
  - Own funds
  - Funds of the operator, including tariffs, under the polluter-pays or user-pays principle.
  - –
* - `producerResponsibilityOrganisation`
  - Producer responsibility
  - Funding from producer responsibility organisations.
  - –
* - `nationalFederal`
  - National-federal
  - Funds from the national or federal budget.
  - –
* - `regional`
  - Regional
  - Funds from a regional authority.
  - –
* - `municipal`
  - Municipal
  - Funds from a municipal authority.
  - –
* - `otherPublicFunds`
  - Other public funds
  - Public funds from another source.
  - –
* - `europeanUnionFund`
  - EU fund
  - Funding from a Union fund.
  - Name the fund in `europeanUnionFundName`.
* - `loan`
  - Loan
  - A loan from a public or private lender.
  - Lender optional in `loanName`.
* - `privateFunds`
  - Private funds
  - Private funding other than a loan.
  - –
* - `notIdentified`
  - Not identified
  - The source of this part of the cost is not yet identified.
  - Use with `fundingStatus` = `notIdentified`.
:::

(art23-cl-funding-status)=
## Funding status

**Type:** `FundingStatus`

Used by `fundingStatus` in {ref}`art23-measurefinancing`.

:::{list-table} Proposed funding status values
:header-rows: 1
:widths: 24 22 34 20

* - Notation
  - Label
  - Definition
  - Notes
* - `secured`
  - Secured
  - The money is granted or committed.
  - Counts towards the financing of the measure.
* - `appliedFor`
  - Applied for
  - An application for the money has been made.
  - –
* - `planned`
  - Planned
  - The Member State plans to use this source.
  - –
* - `notIdentified`
  - Not identified
  - No source has been identified yet.
  - –
:::

(art23-cl-currency)=
## Currency

**Type:** `CurrencyCode`

Used by `millionUnitsOfNationalCurrency` in {ref}`art23-measure` and {ref}`art23-mssummary`. As in
the Water Framework Directive, amounts are reported in millions of euro by euro area Member States
and in millions of national currency by the others, which use their own currency code, not a
generic code for domestic currency. The values are those of the Water Framework Directive
codelist.

:::{list-table} Currency values
:header-rows: 1
:widths: 20 30 30 20

* - Notation
  - Label
  - Definition
  - Notes
* - `EUR`
  - Euro
  - Euro.
  - Euro area Member States.
* - `CZK`
  - Czech koruna
  - Czech koruna.
  - –
* - `DKK`
  - Danish krone
  - Danish krone.
  - –
* - `HUF`
  - Hungarian forint
  - Hungarian forint.
  - –
* - `PLN`
  - Polish zloty
  - Polish zloty.
  - –
* - `RON`
  - Romanian leu
  - Romanian leu.
  - –
* - `SEK`
  - Swedish krona
  - Swedish krona.
  - –
* - `NOK`
  - Norwegian krone
  - Norwegian krone.
  - –
* - `ISK`
  - Icelandic krona
  - Icelandic krona.
  - –
:::

(art23-cl-pro-basis)=
## Basis of the producer responsibility estimate

**Type:** `EstimateBasis`

Used by `producerResponsibilityEstimateBasedOn`.

:::{list-table} Proposed basis of estimate values
:header-rows: 1
:widths: 24 22 34 20

* - Notation
  - Label
  - Definition
  - Notes
* - `agreedFinancialPlan`
  - Agreed financial plan
  - Based on financial plans agreed between the Member State and the producer
    responsibility organisations during the recognition procedure.
  - –
* - `memberStateEstimate`
  - Member State estimate
  - An estimate by the Member State, where agreed financial plans are not yet available.
  - –
:::

(art23-cl-licence)=
## Licence

**Type:** `Licence`

Used by `license` in {ref}`art23-dcmetadata`.

:::{list-table} Proposed licence values
:header-rows: 1
:widths: 20 22 34 24

* - Notation
  - Label
  - Definition
  - Notes
* - `CC0`
  - CC0 1.0
  - Creative Commons public domain dedication.
  - Used across the WISE dataflows.
* - `CC_BY_4_0`
  - CC BY 4.0
  - Creative Commons Attribution 4.0 International.
  - Used across the WISE dataflows.
* - `exactMatch_CC_BY_4_0`
  - Exact match of CC BY 4.0
  - A national licence whose terms match CC BY 4.0.
  - –
* - `narrowMatch_CC_BY_4_0`
  - Narrow match of CC BY 4.0
  - A national licence that is more restrictive than CC BY 4.0.
  - –
:::

Where a Member State publishes under another licence, report the licence document in
`licenseDocument` instead.
