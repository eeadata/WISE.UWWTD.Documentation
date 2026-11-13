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

(art23-cl-derogation-type)=
## Derogation type

**Type:** `DerogationType`

Used by `derogationType` in {ref}`art23-derogation` and {ref}`art23-culturalheritageextension`.

:::{codelist} DerogationType
:::

(art23-cl-derogation-status)=
## Derogation status

**Type:** `DerogationStatus`

Used by `derogationStatus` in {ref}`art23-derogation`.

:::{codelist} DerogationStatus
:::

(art23-cl-eligibility-criterion)=
## Eligibility criterion

**Type:** `EligibilityCriterion`

Used by `eligibilityCriterion` in {ref}`art23-derogation`.

:::{codelist} EligibilityCriterion
:::

(art23-cl-extension-reason)=
## Extension reason

**Type:** `ExtensionReason`

Used by `reasonType` in {ref}`art23-derogation`. Select one or both.

:::{codelist} ExtensionReason
:::

(art23-cl-less-stringent-ground)=
## Less stringent treatment ground

**Type:** `LessStringentGround`

Used by `lessStringentGround` in {ref}`art23-lessstringenttreatment`.

:::{codelist} LessStringentGround
:::

(art23-cl-compliance-share)=
## Compliance share - Articles 3 and 6, agglomerations of 2 000 p.e. and above

**Type:** `ComplianceShare`

Used by `article3Compliance` and `article6Compliance` in {ref}`art23-selfassessment`.

:::{codelist} ComplianceShare
:::

(art23-cl-compliance-share-estimated)=
## Estimated compliance share - Articles 3, 6, 7 and 8

**Type:** `ComplianceShareEstimated`

Used by `article3Compliance1000to1999`, `article6Compliance1000to1999`, `article7Compliance` and
`article8Compliance` in {ref}`art23-selfassessment`. The wider bands reflect that detailed data
may not
yet be available for these agglomerations and plants.

:::{codelist} ComplianceShareEstimated
:::

(art23-cl-risk-assessment)=
## Risk assessment

**Type:** `RiskAssessment`

Used by `riskAssessment` in {ref}`art23-mssummary`.

:::{codelist} RiskAssessment
:::

(art23-cl-contribution-period)=
## Contribution period

**Type:** `ContributionPeriod`

Used by `contributionPeriod` in {ref}`art23-mssummary`. Several values may be selected.

:::{codelist} ContributionPeriod
:::

(art23-cl-status)=
## Plant and agglomeration status

**Type:** `PlantAgglomerationStatus`

Used by the `status` field of the {ref}`art23-uwwtp` and {ref}`art23-agglomeration` tables.

:::{codelist} PlantAgglomerationStatus
:::

(art23-cl-measure-type)=
## Measure type

**Type:** `UWWTDMeasureType`

Used by the `uwwtdMeasureType` field of the {ref}`art23-measure` table. One or more values per
measure, as in the draft format, all for the same kind of object. The
codelist brings together the former treatment plant and agglomeration measure codelists; the
renewal value, which both had, is split into one value for collecting systems and one for
treatment plants. The notes give the article and the object type: a measure listing plants lists
them in `euUWWTPCode`, and a measure listing agglomerations in `euAgglomerationCode`.

The name is prefixed with `UWWTD` because the Water Framework Directive codelist `MeasureType`
classifies measures differently, by their nature (legislative, technical, economic and so on).

:::{codelist} UWWTDMeasureType
:::

(art23-cl-measure-type-wfd)=
### Correspondence with the Water Framework Directive

Measures for treatment plants and collecting systems are intended to be reported once, in this
dataflow, and not again in the programme of measures under the Water Framework Directive
({ref}`art23-oi-wfd`). So that they can still be used in assessments under that Directive, each
measure type corresponds to a WFD key type of measure (`mainKeyTypeOfMeasure`) and main pressure
(`mainPressureType`), derived centrally and not reported. The correspondence below is a proposal,
to be confirmed.

:::{codelist} UWWTDMeasureTypeWFD
:::

`P1-1` is the WFD pressure "Point - Urban waste water" and `P1-2` "Point - Storm overflows". A
measure with several types corresponds to the key types of all of them. Where those differ, how
the measure is classified under the Water Framework Directive is open ({ref}`art23-oi-wfd`).

(art23-cl-coverage)=
## Geographical coverage

**Type:** `UWWTDGeographicCoverage`

Used by `geographicalCoverage` in {ref}`art23-measure`. Prefixed with `UWWTD` because the
corresponding Water Framework Directive codelist, `WFDGeographicCoverage`, has other values.

:::{codelist} UWWTDGeographicCoverage
:::

(art23-cl-implementation-status)=
## Implementation status

**Type:** `ImplementationStatus`

Used by `implementationStatus` in {ref}`art23-measure`. The same codelist as in the Water Framework
Directive 4th cycle.

:::{codelist} ImplementationStatus
:::

(art23-cl-cost-status)=
## Cost status

**Type:** `CostStatus`

Used by `costStatus` in {ref}`art23-measure`.

:::{codelist} CostStatus
:::

(art23-cl-priority)=
## Priority

**Type:** `Priority`

Used by the `prioritisation` field of the {ref}`art23-measure` table.

:::{codelist} Priority
:::

The draft does not define the boundaries between the three levels. See {ref}`art23-investments`
and {ref}`art23-oi-prioritisation`.

(art23-cl-eu-funds)=
## EU funds

**Type:** `EUFund`

Used by `europeanUnionFundName` in {ref}`art23-measurefinancing`.

:::{codelist} EUFund
:::

(art23-cl-funding-source)=
## Funding source

**Type:** `FundingSource`

Used by `fundingSource` in {ref}`art23-measurefinancing`. It replaces the former other public fund
codelist, whose values are kept.

:::{codelist} FundingSource
:::

(art23-cl-funding-status)=
## Funding status

**Type:** `FundingStatus`

Used by `fundingStatus` in {ref}`art23-measurefinancing`.

:::{codelist} FundingStatus
:::

(art23-cl-currency)=
## Currency

**Type:** `CurrencyCode`

Used by `millionUnitsOfNationalCurrency` in {ref}`art23-measure` and {ref}`art23-mssummary`. As in
the Water Framework Directive, amounts are reported in millions of euro by euro area Member States
and in millions of national currency by the others, which use their own currency code, not a
generic code for domestic currency. The values are those of the Water Framework Directive
codelist.

:::{codelist} CurrencyCode
:::

(art23-cl-pro-basis)=
## Basis of the producer responsibility estimate

**Type:** `EstimateBasis`

Used by `producerResponsibilityEstimateBasedOn`.

:::{codelist} EstimateBasis
:::

(art23-cl-licence)=
## Licence

**Type:** `Licence`

Used by `license` in {ref}`art23-dcmetadata`.

:::{codelist} Licence
:::

fWhere a Member State publishes under another licence, report the licence document in
`licenseDocument` instead.
