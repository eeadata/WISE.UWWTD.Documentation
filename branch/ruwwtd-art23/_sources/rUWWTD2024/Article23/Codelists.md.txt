(art23-codelists)=
# Codelists

:::{warning} Draft
All codelists on this page are proposals from the draft guidance. The labels are
reproduced from the draft, with spacing and hyphens made consistent. The draft does not define the
codes to be entered in the reporting template, and several labels are under review
({ref}`art23-open-issues`).
:::

Every codelist below is named as a WISE enumeration type, given under the heading, and gives for
each value the notation to report, a short label and a definition, following
{ref}`art23-notation`. The notations are proposals: the draft guidance
lists labels only and does not define the codes to be entered in the reporting template.

Only the plant `measure` field is explicitly described as allowing more than one value. For the
other codelists, the draft does not say whether several values may be selected.

(art23-cl-deadline-ext)=
## Deadline extension - Articles 3(2) and 6(3)

**Type:** `DeadlineExtension_Enum`

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
1 January 2025, or 12 or 14 years for Bulgaria, Croatia and Romania. The draft lists the values as
plain years; the notations above are proposals ({ref}`art23-notation`).

(art23-cl-deadline-ext-7-4)=
## Deadline extension - Article 7(4)

**Type:** `DeadlineExtensionArticle7_4_Enum`

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

(art23-cl-compliance)=
## National self-assessment - Articles 3 to 8

**Type:** `ComplianceSelfAssessment_Enum`

Used by `article3Compliance` to `article8Compliance` in {ref}`art23-mssummary`. For the meaning of C, NC and
PD, see {ref}`art23-status-values`.

:::{list-table} Proposed self-assessment values
:header-rows: 1
:widths: 22 78

* - Notation
  - Proposed values
* - `article3Compliance`
  - C (compliant); NC - Agglomerations over 2000 p.e. not compliant; NC - Not yet transposed at
    national level; PD - Agglomerations below 2000 p.e. not defined; PD - Agglomerations below
    2000 p.e.
* - `article4Compliance`
  - C (compliant); NC - Not yet transposed at national level; PD - IS registry absence;
    PD - More than 2% of load addressed by IS; PD - Technological inadequacy of existing IS
* - `article5Compliance`
  - C (compliant); NC - Not yet transposed at national level; PD - IUWMP not yet established for
    drainage areas of aggl. of 100 000 p.e. and above (Art 5); PD - IUWMP not yet established for
    drainage areas of aggl. referred to in Art 5(2)
* - `article6Compliance`
  - C (compliant); NC - Not yet transposed at national level; NC - Agglomerations over 2000 p.e.
    not compliant; PD - Agglomerations below 2000 p.e. not defined; PD - Agglomerations below
    2000 p.e. not compliant
* - `article7Compliance`
  - C (compliant); NC - Not yet transposed at national level; PD - Agglomerations over
    150 000 p.e. not compliant; PD - Areas sensitive to eutrophication not yet identified (Art 7);
    PD - Agglomerations Art. 7(3) not compliant; PD - Extended deadlines (Art 7(6))
* - `article8Compliance`
  - C (compliant); NC - Not yet transposed at national level; PD - Treatment plants >= 150 000 p.e.
    without 4T; PD - Areas at risk for micropollutants not yet identified; PD - Intermediate
    requirement reached only (Art 8); PD - Contribution from the EPR not set/gathered (Art 9)
:::

The last `article3Compliance` value is incomplete in the draft. Known wording issues are listed under
{ref}`art23-oi-self-assessment`.

(art23-cl-status)=
## Plant and agglomeration status

**Type:** `Status_Enum`

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
  - The draft writes this value as C.
* - `nonCompliant`
  - Non-compliant (NC)
  - Articles 3 to 8 non-compliant; Article 18 requirements fulfilled or not applicable.
  - The draft writes this value as NC.
* - `pendingDeadline`
  - Pending deadline (PD)
  - Pending deadline: time remains for submission of the application.
  - The draft writes this value as PD.
* - `compliantArticle18NotMet`
  - Compliant, Article 18 not met (C+A18)
  - Articles 3 to 8 compliant; more stringent Article 18 requirements not met.
  - The draft writes this value as C+A18.
* - `nonCompliantArticle18NotMet`
  - Non-compliant, Article 18 not met (NC+A18)
  - Articles 3 to 8 non-compliant; more stringent Article 18 requirements not met.
  - The draft writes this value as NC+A18.
:::

(art23-cl-uww-measures)=
## Treatment plant measures

**Type:** `TreatmentPlantMeasure_Enum`

Used by the `measure` field of the {ref}`art23-uwwtp` table. Select one or more values.

:::{list-table} Proposed treatment plant measures
:header-rows: 1
:widths: 30 24 26 20

* - Notation
  - Label
  - Definition
  - Notes
* - `newPlantArticle6_3`
  - New plant, agglomerations of 1 000 to 1 999 p.e.
  - A new treatment plant providing secondary treatment.
  - Article 6(3).
* - `newPlantArticle6_1`
  - New plant, agglomerations of 2 000 p.e. and above
  - A new treatment plant providing secondary treatment.
  - Article 6(1).
* - `upgradeTertiaryNitrogen`
  - Upgrade to tertiary treatment (N)
  - Upgrade to tertiary treatment for nitrogen.
  - Article 7(1) for plants of 150 000 p.e. and above; Article 7(3) for
    agglomerations of 10 000 p.e. and above discharging into sensitive areas.
* - `upgradeTertiaryPhosphorus`
  - Upgrade to tertiary treatment (P)
  - Upgrade to tertiary treatment for phosphorus.
  - Articles 7(1) and 7(3), as above.
* - `upgradeTertiaryNitrogenPhosphorus`
  - Upgrade to tertiary treatment (N+P)
  - Upgrade to tertiary treatment for both nitrogen and phosphorus.
  - Articles 7(1) and 7(3), as above.
* - `upgradeQuaternary`
  - Upgrade to quaternary treatment
  - Upgrade to quaternary treatment for micropollutants.
  - Article 8(1) for plants of 150 000 p.e. and above; Article 8(4) for
    agglomerations of 10 000 p.e. and above discharging into risk areas.
* - `energyNeutrality`
  - Energy neutrality
  - Measures to meet the renewable energy targets.
  - Article 11(2), for plants of 10 000 p.e. and above.
* - `secondaryTreatmentRiskBased`
  - Secondary treatment, agglomerations below 1 000 p.e.
  - Applying secondary treatment on the basis of the risk assessment.
  - Article 18(2)(c).
* - `tertiaryTreatmentRiskBased`
  - Tertiary treatment, agglomerations below 10 000 p.e.
  - Applying tertiary treatment on the basis of the risk assessment.
  - Article 18(2)(d).
* - `quaternaryTreatmentRiskBased`
  - Quaternary treatment, agglomerations below 10 000 p.e.
  - Applying quaternary treatment on the basis of the risk assessment.
  - Article 18(2)(e).
* - `stricterTreatmentRiskBased`
  - Stricter treatment requirements
  - Applying stricter requirements for treatment on the basis of the risk assessment.
  - Article 18(2)(g).
* - `otherMeasureArticle18_2`
  - Other appropriate measure
  - Another appropriate measure under Article 18(2).
  - Article 18(2). Describe the measure in `measureText`.
* - `renewOrReplaceArticle23_1c`
  - Renew or replace existing infrastructure
  - Renewal or replacement of existing infrastructure, including capacity increase.
  - Article 23(1)(c).
:::

(art23-cl-agg-measures)=
## Agglomeration measures

**Type:** `AgglomerationMeasure_Enum`

Used by the `measures` field of the {ref}`art23-agglomeration` table.

:::{list-table} Proposed agglomeration measures
:header-rows: 1
:widths: 30 24 26 20

* - Notation
  - Label
  - Definition
  - Notes
* - `newCollectingSystemArticle3_2`
  - New collecting systems, 1 000 to 1 999 p.e.
  - New collecting systems in agglomerations of 1 000 to 1 999 p.e.
  - Article 3(2).
* - `newCollectingSystemArticle3_1`
  - New collecting systems, 2 000 p.e. and above
  - New collecting systems in agglomerations of 2 000 p.e. and above.
  - Article 3(1).
* - `stormWaterOverflowReduction`
  - Measures to reduce storm water overflows
  - Measures to reduce storm water overflows from collecting systems.
  - Article 3(4): collecting systems must meet Part A of Annex I.
* - `managementPlanMeasures`
  - Measures resulting from a management plan
  - Measures resulting from an integrated urban wastewater management plan.
  - Article 5 and Annex V.
* - `newCollectingSystemRiskBased`
  - New collecting systems, below 1 000 p.e.
  - New collecting systems in agglomerations below 1 000 p.e., on the basis of the risk
    assessment.
  - Article 18(2)(b).
* - `renewOrReplaceArticle23_1c`
  - Renew or replace existing infrastructure
  - Renewal or replacement of existing collecting system infrastructure.
  - Article 23(1)(c).
:::

(art23-cl-priority)=
## Priority

**Type:** `Priority_Enum`

Used by the `prioritisation` field of the {ref}`art23-uwwtp` and {ref}`art23-agglomeration`
tables.

:::{list-table} Proposed priority values
:header-rows: 1
:widths: 20 20 32 28

* - Notation
  - Label
  - Definition
  - Notes
* - `high`
  - High
  - High priority investment.
  - Related to the size of the agglomeration and the level of environmental impact.
* - `medium`
  - Medium
  - Medium priority investment.
  - –
* - `low`
  - Low
  - Low priority investment.
  - –
:::

The draft does not define the boundaries between the three levels. See {ref}`art23-investments`
and {ref}`art23-oi-prioritisation`.

(art23-cl-eu-funds)=
## EU funds

**Type:** `EUFund_Enum`

Used by the `europeanUnionFundName` and `europeanUnionFundsName` fields.

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
  - The draft calls this the Resilience Recovery Facility.
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

(art23-cl-public-funds)=
## Other public funds

**Type:** `OtherPublicFund_Enum`

Used by the `otherPublicFundSpecification` field.

:::{list-table} Proposed other public fund values
:header-rows: 1
:widths: 24 22 34 20

* - Notation
  - Label
  - Definition
  - Notes
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
:::

(art23-cl-pro-basis)=
## Basis of the producer responsibility estimate

**Type:** `EstimateBasis_Enum`

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

**Type:** `Licence_Enum`

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
:::

Where a Member State publishes under another licence, report the licence document in
`licenseDocument` instead.
