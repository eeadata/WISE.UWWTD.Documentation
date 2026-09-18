(art23-mssummary)=
# MSSummary

:::{warning} Draft
Draft baseline. The self-assessment codelists in particular are under review
({ref}`art23-oi-self-assessment`).
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
:widths: 22 16 26 10 10 16

* - Notation
  - Label
  - Definition
  - Type
  - Status
  - Condition
* - `situationAt`
  - Situation at
  - Date of the reported situation, for example the date the programme was approved or
    the date of the decision not to establish one.
  - date
  - Required
  - –
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

## Self-assessment of Articles 3 to 8

Each field records the Member State's own assessment, at national level, of compliance with one
Article in the first programme. The draft notes that detailed information may not yet be
available, so these are estimates. The draft states that compliance status is self-reported as
at 1 January 2028.

:::{list-table} MSSummary fields - self-assessment
:header-rows: 1
:widths: 26 18 24 10 8 14

* - Notation
  - Label
  - Definition
  - Type
  - Status
  - Codelist
* - `article3Compliance`
  - Article 3 compliance
  - Self-assessment of Article 3 (collecting systems).
  - ComplianceSelfAssessment_Enum
  - Required
  - {ref}`art23-cl-compliance`
* - `article4Compliance`
  - Article 4 compliance
  - Self-assessment of Article 4 (individual systems).
  - ComplianceSelfAssessment_Enum
  - Required
  - {ref}`art23-cl-compliance`
* - `article5Compliance`
  - Article 5 compliance
  - Self-assessment of Article 5 (integrated urban wastewater management plans).
  - ComplianceSelfAssessment_Enum
  - Required
  - {ref}`art23-cl-compliance`
* - `article5ManagementPlanReference`
  - Article 5 management plan reference
  - Reference to the document listing the Member State's integrated urban wastewater
    management plans.
  - referenceCode
  - Optional
  - –
* - `article6Compliance`
  - Article 6 compliance
  - Self-assessment of Article 6 (secondary treatment).
  - ComplianceSelfAssessment_Enum
  - Required
  - {ref}`art23-cl-compliance`
* - `article7Compliance`
  - Article 7 compliance
  - Self-assessment of Article 7 (tertiary treatment).
  - ComplianceSelfAssessment_Enum
  - Required
  - {ref}`art23-cl-compliance`
* - `article8Compliance`
  - Article 8 compliance
  - Self-assessment of Article 8 (quaternary treatment).
  - ComplianceSelfAssessment_Enum
  - Required
  - {ref}`art23-cl-compliance`
:::

:::{note}
Most deadlines of Articles 3 to 8 fall after 1 January 2028. The value PD (pending deadline)
reflects this. The draft does not yet state whether one or several values may be reported per
Article, how a single national value is derived from plant or agglomeration data, or when to use
"not yet transposed at national level". An alternative structure for this assessment is also
under review. See {ref}`art23-oi-self-assessment`.
:::

## Risk assessment

Article 18(1) requires Member States to identify and assess the risks caused by urban wastewater
discharges by 31 December 2027. Article 18(3) requires a summary of the identified risks and of
the measures adopted to be included in the programme.

:::{list-table} MSSummary fields - risk assessment
:header-rows: 1
:widths: 22 16 26 10 10 16

* - Notation
  - Label
  - Definition
  - Type
  - Status
  - Condition
* - `riskAssessment`
  - Risk assessment
  - Whether a risk assessment of urban wastewater discharges has been carried out in
    accordance with Article 18.
  - YesNo
  - Required
  - –
* - `riskDate`
  - Risk assessment date
  - Date of issue of the risk assessment.
  - date
  - Conditional
  - If `riskAssessment` = yes
* - `riskIdentified`
  - Risks identified
  - Whether any risks have been identified. Measures under Article 18(2) that address
    identified risks are reported with the measure codelists of the UWWTP and
    Agglomeration tables.
  - YesNo
  - Conditional
  - If `riskAssessment` = yes
* - `riskSummaryReference`
  - Risk summary reference
  - Reference to the relevant section of the river basin management plan, or to another
    official summary of the identified risks and adopted measures.
  - referenceCode
  - Conditional
  - Required if `riskAssessment` = yes
:::

The draft offers only yes or no for `riskAssessment`. How to report a risk assessment that covers
only some discharges is still open ({ref}`art23-oi-risk`).

## Producer responsibility contribution

Article 23(1)(b) asks for an estimation of the financial contribution from PROs "when available".

:::{list-table} MSSummary fields - producer responsibility contribution
:header-rows: 1
:widths: 28 18 22 12 8 14

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
* - `sufficientResources2033`
  - Sufficient resources by 2033
  - Will the planned resources, including the contribution in
    `producerResponsibilityContribution`, be sufficient to meet the requirements of the
    Directive by the end of 2033?
  - YesNo
  - Required
  - –
* - `sufficientResources2036`
  - Sufficient resources by 2036
  - As `sufficientResources2033`, by the end of 2036.
  - YesNo
  - Required
  - –
* - `sufficientResources2039`
  - Sufficient resources by 2039
  - As `sufficientResources2033`, by the end of 2039.
  - YesNo
  - Required
  - –
* - `sufficientResources2045`
  - Sufficient resources by 2045
  - As `sufficientResources2033`, by the end of 2045.
  - YesNo
  - Required
  - –
* - `otherPeriod`
  - Other period
  - Another period covered by the funds in `producerResponsibilityContribution`.
  - string255
  - Optional
  - –
* - `remarks`
  - Remarks
  - Other important information on compliance and its assessment.
  - string1000
  - Optional
  - –
:::

The years 2033, 2036, 2039 and 2045 are the interim and final deadlines of Articles 7 and 8.
The draft does not state which requirements the questions cover, which period `producerResponsibilityContribution`
refers to, or whether amounts are nominal. These points are open ({ref}`art23-oi-pro`).
