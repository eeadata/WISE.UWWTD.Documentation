(art23-otherinvestment)=
# OtherInvestment

:::{warning} Draft
Draft baseline. The meaning of the reference period is still to be clarified
({ref}`art23-oi-otherinvestment`).
:::

**Table status:** Conditional. Use it for investments that cannot be reported in the UWWTP or
Agglomeration tables because they are not attributed to a single plant or agglomeration. If all
planned resources are attributed to specific plants or agglomerations, leave the table empty.
**Rows:** one or more per Member State, for example one row for the whole period or one row per
year.

The preferred way to report investments is against individual plants and agglomerations. Use this
table for resources that, when the programme is approved, are allocated only within general
frameworks. For example, the draft suggests using it for total investment in collecting systems
and treatment plants for agglomerations below 2 000 p.e. that are newly covered by the Directive.

Total investment by the Member State is the sum of the investments reported in the UWWTP,
Agglomeration and OtherInvestment tables. Do not repeat here anything already reported in those
tables.

```{mermaid} /rUWWTD2024/Article23/mmd/Article23_OtherInvestment_ClassDiagram.mmd
:name: Article23_OtherInvestment_ClassDiagram
:caption: Article 23 - OtherInvestment - draft
:align: center
```

In {numref}`Article23_OtherInvestment_ClassDiagram`, `[1]` marks the Required fields and `[0..1]` the
Optional and Conditional ones ({ref}`art23-requirement-status`).

## OtherInvestment fields

The descriptions of the four investment fields follow the wording of Article 23(1)(b), for
investments required to implement the Directive, and Article 23(1)(c), for renewal, upgrade or
replacement.

:::{list-table} OtherInvestment fields
:header-rows: 1
:widths: 30 18 22 12 8 14

* - Notation
  - Label
  - Definition
  - Type
  - Status
  - Condition or codelist
* - `startYear`
  - Start year
  - First year of the reference period of the reported investments.
  - gYear
  - Required
  - –
* - `endYear`
  - End year
  - Last year of the reference period of the reported investments.
  - gYear
  - Required
  - –
* - `collectingSystemNewInvestment`
  - Collecting systems - new infrastructure
  - Investments in new collecting systems required to implement the Directive
    (Article 23(1)(b)), not reported in the Agglomeration table. Report 0 if none.
  - nonNegativeValue (million EUR)
  - Required
  - –
* - `collectingSystemRenewalInvestment`
  - Collecting systems - renewal
  - Investments in collecting systems needed to renew, upgrade or replace existing
    infrastructure (Article 23(1)(c)), not reported in the Agglomeration table. Report 0
    if none.
  - nonNegativeValue (million EUR)
  - Required
  - –
* - `treatmentPlantNewInvestment`
  - Treatment plants - new infrastructure
  - Investments in new treatment plants required to implement the Directive
    (Article 23(1)(b)), not reported in the UWWTP table. Report 0 if none.
  - nonNegativeValue (million EUR)
  - Required
  - –
* - `treatmentPlantRenewalInvestment`
  - Treatment plants - renewal
  - Investments in treatment plants needed to renew, upgrade or replace existing
    infrastructure (Article 23(1)(c)), not reported in the UWWTP table. Report 0 if none.
  - nonNegativeValue (million EUR)
  - Required
  - –
* - `europeanUnionFunds`
  - European Union funds
  - Current or expected EU funds covering the investments above. Report 0 if none.
  - nonNegativeValue (million EUR)
  - Required
  - –
* - `europeanUnionFundsName`
  - European Union funds name
  - Name of the EU funds.
  - EUFund_Enum
  - Conditional
  - Required if `europeanUnionFunds` > 0. {ref}`art23-cl-eu-funds`
* - `otherPublicFunds`
  - Other public funds
  - Current or expected other public funds. Report 0
    if none.
  - nonNegativeValue (million EUR)
  - Required
  - –
* - `otherPublicFundSpecification`
  - Other public fund specification
  - Type of other public funds.
  - OtherPublicFund_Enum
  - Conditional
  - Required if `otherPublicFunds` > 0. {ref}`art23-cl-public-funds`
* - `remarks`
  - Remarks
  - Other remarks.
  - string1000
  - Optional
  - –
:::

This table has no fields for loans or for funding from producer responsibility organisations.

## Filling in the table

* **Several rows.** If you report one row per year or per period, make sure the same investment
  is not counted in more than one row.
* **Reference period.** The draft does not define which period `startYear` and `endYear` should
  cover, for example the six years of the programme or the period to 2045
  ({ref}`art23-oi-otherinvestment`).
