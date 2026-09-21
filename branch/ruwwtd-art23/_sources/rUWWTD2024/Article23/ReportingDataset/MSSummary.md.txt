(art23-mssummary)=
# MSSummary

:::{warning} Draft
Draft baseline. The self-assessment fields were revised after the country consultation and are
still under review ({ref}`art23-oi-self-assessment`).
:::

**Table status:** Required.
**Rows:** one row per Member State.

The table gives an overview of the programme: whether one is required, references to it and to
the prioritisation methodology, a national self-assessment of compliance with Articles 3 to 8, the
Article 18 risk assessment, and the estimated contribution from producer responsibility
organisations (PROs).

According to the draft, a Member State that is fully compliant with Articles 3 to 8 does not need
to report the more detailed tables.

```{mermaid} /rUWWTD2024/Article23/mmd/Article23_MSSummary_ClassDiagram.mmd
:name: Article23_MSSummary_ClassDiagram
:caption: Article 23 - MSSummary - draft
:align: center
```

In {numref}`Article23_MSSummary_ClassDiagram`, `[1]` marks the Required fields and `[0..1]` the
Optional and Conditional ones ({ref}`art23-requirement-status`).

## Programme and references

:::{list-table} MSSummary fields - programme and references
:header-rows: 1
:widths: 22 16 26 12 10 14

* - Notation
  - Label
  - Definition
  - Type
  - Status
  - Condition
* - `situationAt`
  - Situation at
  - Date of the reported situation, for example the date the programme was approved or the
    date of the decision not to establish one.
  - date
  - Required
  - Between 2026 and 2045
* - `programmeObligation`
  - Programme obligation
  - Whether the Member State is obliged to provide a national implementation programme.
  - YesNo
  - Required
  - –
* - `programmeReference`
  - Programme reference
  - Reference to the national implementation programme in the documents dataset.
  - referenceCode
  - Conditional
  - Required if `programmeObligation` = yes
* - `prioritisationReference`
  - Prioritisation reference
  - Reference to the methodology used to prioritise investments.
  - referenceCode
  - Conditional
  - Required if `programmeObligation` = yes
:::

The programme is updated at least every six years, unless the Member State is fully compliant
with Articles 3 to 8.

## Self-assessment of Articles 3 to 8

Each field records the Member State's own assessment, at national level, of compliance with one
Article in the first programme. The draft notes that detailed information may not yet be
available, so Articles 3 and 6 are assessed as the share of compliant agglomerations in
percentage ranges, Article 4 as a yes or no answer, Article 5 as a count of agglomerations, and
Articles 7 and 8 as the share of compliant treatment plants of 150 000 p.e. and above.

Articles 3 and 6 are assessed separately for the two size bands, because the deadlines differ:
agglomerations of 2 000 p.e. and above, and agglomerations of 1 000 to 1 999 p.e.

:::{list-table} MSSummary fields - self-assessment
:header-rows: 1
:widths: 26 18 22 14 8 12

* - Notation
  - Label
  - Definition
  - Type
  - Status
  - Codelist
* - `article3Compliance`
  - Article 3 compliance
  - Share of agglomerations of 2 000 p.e. and above that comply with Article 3 (collecting
    systems).
  - ComplianceShare_Enum
  - Required
  - {ref}`art23-cl-compliance-share`
* - `article3Compliance1000to1999`
  - Article 3 compliance, 1 000 to 1 999 p.e.
  - Estimated share of agglomerations of 1 000 to 1 999 p.e. that comply with Article 3.
  - ComplianceShareEstimated_Enum
  - Required
  - {ref}`art23-cl-compliance-share-estimated`
* - `article4Compliance`
  - Article 4 compliance
  - Whether a system of authorisation and control of individual systems has been introduced in
    accordance with the Directive.
  - YesNo
  - Required
  - –
* - `article5ManagementPlanCount`
  - Article 5 management plans
  - Number of agglomerations of 100 000 p.e. and above that already have an integrated urban
    wastewater management plan.
  - nonNegativeValue
  - Required
  - –
* - `article5ManagementPlanReference`
  - Article 5 management plan reference
  - Reference to the document listing the Member State's integrated urban wastewater
    management plans.
  - referenceCode
  - Optional
  - –
* - `article6Compliance`
  - Article 6 compliance
  - Share of agglomerations of 2 000 p.e. and above that comply with Article 6 (secondary
    treatment).
  - ComplianceShare_Enum
  - Required
  - {ref}`art23-cl-compliance-share`
* - `article6Compliance1000to1999`
  - Article 6 compliance, 1 000 to 1 999 p.e.
  - Estimated share of agglomerations of 1 000 to 1 999 p.e. that comply with Article 6.
  - ComplianceShareEstimated_Enum
  - Required
  - {ref}`art23-cl-compliance-share-estimated`
* - `article7Compliance`
  - Article 7 compliance
  - Share of treatment plants of 150 000 p.e. and above that meet the Article 7 tertiary
    treatment requirements.
  - ComplianceShareEstimated_Enum
  - Required
  - {ref}`art23-cl-compliance-share-estimated`
* - `article8Compliance`
  - Article 8 compliance
  - Share of treatment plants of 150 000 p.e. and above that meet the Article 8 quaternary
    treatment requirements.
  - ComplianceShareEstimated_Enum
  - Required
  - {ref}`art23-cl-compliance-share-estimated`
:::

:::{note}
Most deadlines of Articles 3 to 8 fall after 1 January 2028, so the first programme records an
expected position rather than a settled one. How a single national share is derived from plant or
agglomeration data is not stated. See {ref}`art23-oi-self-assessment`.
:::

## Risk assessment

Article 18(1) requires Member States to identify and assess the risks caused by urban wastewater
discharges by 31 December 2027. Article 18(3) requires a summary of the identified risks and of
the measures adopted to be included in the programme.

:::{list-table} MSSummary fields - risk assessment
:header-rows: 1
:widths: 22 16 26 12 10 14

* - Notation
  - Label
  - Definition
  - Type
  - Status
  - Condition or codelist
* - `riskAssessment`
  - Risk assessment
  - Whether a risk assessment of urban wastewater discharges has been carried out in
    accordance with Article 18.
  - RiskAssessment_Enum
  - Required
  - {ref}`art23-cl-risk-assessment`
* - `riskDate`
  - Risk assessment date
  - Date of issue of the risk assessment.
  - date
  - Conditional
  - Required if `riskAssessment` = `yes`
* - `riskIdentified`
  - Risks identified
  - Whether any risks have been identified. Measures under Article 18(2) that address
    identified risks are reported with the measure codelists of the UWWTP and Agglomeration
    tables.
  - YesNo
  - Conditional
  - Required if `riskAssessment` = `yes`
* - `riskSummaryReference`
  - Risk summary reference
  - Reference to the relevant section of the river basin management plan, or to another
    official summary of the identified risks and adopted measures.
  - referenceCode
  - Conditional
  - Required if `riskAssessment` = `yes`
:::

A risk assessment covering only some discharges is reported as `partially`. How the three
conditional fields apply in that case is open ({ref}`art23-oi-risk`).

## Producer responsibility contribution

Article 23(1)(b) asks for an estimation of the financial contribution from PROs "when available".
In the first programme a Member State may estimate the contribution for the whole period or for
the period of an interim target, and assign it to that period.

:::{list-table} MSSummary fields - producer responsibility contribution
:header-rows: 1
:widths: 28 18 22 12 8 12

* - Notation
  - Label
  - Definition
  - Type
  - Status
  - Condition or codelist
* - `producerResponsibilityContribution`
  - Producer responsibility contribution
  - Estimated financial contribution from producer responsibility organisations, total at
    national level.
  - nonNegativeValue (million EUR)
  - Required
  - –
* - `producerResponsibilityEstimateBasedOn`
  - Estimate based on
  - Basis of the estimate.
  - EstimateBasis_Enum
  - Required
  - {ref}`art23-cl-pro-basis`
* - `contributionPeriod`
  - Contribution period
  - Period or periods by which the planned resources, including the contribution in
    `producerResponsibilityContribution`, are expected to be sufficient to meet the
    requirements of the Directive. Select one or more.
  - ContributionPeriod_Enum [0..n]
  - Optional
  - {ref}`art23-cl-contribution-period`
* - `contributionPeriodOther`
  - Other contribution period
  - Explanation of the period, where `contributionPeriod` includes `other`.
  - string1000
  - Conditional
  - Required if `contributionPeriod` includes `other`
* - `remarks`
  - Remarks
  - Other important information on compliance and its assessment.
  - string1000
  - Optional
  - –
:::

The years 2033, 2036, 2039 and 2045 are the interim and final deadlines of Articles 7 and 8. A
Member State that has estimated its contribution over a longer period, such as 2028 to 2045, or
that works to a different budgetary cycle, selects `other` and describes the period in
`contributionPeriodOther`.
