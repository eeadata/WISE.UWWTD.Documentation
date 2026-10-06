(art23-selfassessment)=
# SelfAssessment

:::{warning} Draft
Draft baseline. The self-assessment fields were revised after the country consultation and are
still under review ({ref}`art23-oi-self-assessment`).
:::

**Table status:** Required.
**Rows:** one row per Member State.

The table records the Member State's own assessment, at national level, of compliance with
Articles 3 to 8 at the time of the first programme. According to the draft, a Member State that
is fully compliant with those Articles does not need to report the more detailed investment
tables.

```{mermaid} /rUWWTD2024/Article23/mmd/Article23_SelfAssessment_ClassDiagram.mmd
:name: Article23_SelfAssessment_ClassDiagram
:caption: Article 23 - SelfAssessment - draft
:align: center
```

In {numref}`Article23_SelfAssessment_ClassDiagram`, `[1]` marks the Required fields
({ref}`art23-requirement-status`). The reference to the published management plans is reported in
{ref}`art23-mssummary`.

## Self-assessment fields

Each field records the Member State's own assessment, at national level, of compliance with one
Article in the first programme. The draft notes that detailed information may not yet be
available, so Articles 3 and 6 are assessed as the share of compliant agglomerations in
percentage ranges, Article 4 as a yes or no answer, Article 5 as a count of agglomerations, and
Articles 7 and 8 as the share of compliant treatment plants of 150 000 p.e. and above.

Articles 3 and 6 are assessed separately for the two size bands, because the deadlines differ:
agglomerations of 2 000 p.e. and above, and agglomerations of 1 000 to 1 999 p.e.

:::{list-table} SelfAssessment fields
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
