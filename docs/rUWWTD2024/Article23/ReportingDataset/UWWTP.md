(art23-uwwtp)=
# UWWTP

:::{warning} Draft
Draft baseline. Which plants must be listed, the status codelist, prioritisation and the
funding fields are still under discussion (see the open issues linked below).
:::

**Table status:** Conditional. Required where investments are planned in urban wastewater
treatment plants to implement the Directive, or to renew, upgrade or replace existing
infrastructure.
**Rows:** one row per plant. `code` is the primary key.

The table is used to monitor planned investments in treatment plants, the measures they fund and
their funding sources. According to the draft, rows are linked to the plants already reported
under Directive 91/271/EEC.

The draft lists plants that are currently non-compliant, face upcoming deadlines, or are at risk
of future non-compliance, for example because of capacity constraints, more stringent
requirements from the risk assessment or urban development. Whether compliant plants with planned
renewal investments must also be listed is open ({ref}`art23-oi-scope`). See also
{ref}`art23-investments`.

```{mermaid} /rUWWTD2024/Article23/mmd/Article23_UWWTP_ClassDiagram.mmd
:name: Article23_UWWTP_ClassDiagram
:caption: Article 23 - UWWTP - draft
:align: center
```

In {numref}`Article23_UWWTP_ClassDiagram`, `[1]` marks the Required fields, `[0..1]` the Optional
and Conditional ones, and `[1..n]` the measure field, which accepts several values
({ref}`art23-requirement-status`).

## Plant, status and measures

:::{list-table} UWWTP fields - plant, status and measures
:header-rows: 1
:widths: 22 16 26 10 10 16

* - Notation
  - Label
  - Definition
  - Type
  - Status
  - Condition or codelist
* - `code`
  - Plant code
  - Unique code of the treatment plant. Primary key.
  - wiseIdentifier
  - Required
  - –
* - `name`
  - Plant name
  - Name of the treatment plant.
  - string255
  - Required
  - –
* - `status`
  - Status
  - Status of the plant at the reference year.
  - Status_Enum
  - Required
  - {ref}`art23-cl-status`
* - `measure`
  - Measure
  - Measure or measures needed at the plant. Select one or more.
  - TreatmentPlantMeasure_Enum
  - Required
  - {ref}`art23-cl-uww-measures`
* - `measureText`
  - Other measure description
  - Description of another appropriate measure under Article 18(2).
  - string1000
  - Conditional
  - If `measure` includes `otherMeasureArticle18_2`
* - `prioritisation`
  - Prioritisation
  - Priority of the investment, related to the size of the agglomeration and the level of
    environmental impact.
  - Priority_Enum
  - Required
  - {ref}`art23-cl-priority`
:::

## Load, capacity and dates

:::{list-table} UWWTP fields - load, capacity and dates
:header-rows: 1
:widths: 24 16 26 12 10 12

* - Notation
  - Label
  - Definition
  - Type
  - Status
  - Condition
* - `expectedLoad`
  - Expected load
  - Planned load entering the plant at the expected date of compliance.
  - nonNegativeValue (p.e.)
  - Required
  - –
* - `expectedCapacity`
  - Expected capacity
  - Planned organic design capacity of the plant.
  - nonNegativeValue (p.e.)
  - Required
  - –
* - `expectedYearStartWork`
  - Expected year of start of work
  - Year, or expected year, in which construction works start.
  - gYear
  - Required
  - –
* - `expectedYearPerformance`
  - Expected year of performance
  - Expected year of compliance, meaning 12 months of compliant samples.
  - gYear
  - Required
  - –
:::

## Investment and funding

:::{list-table} UWWTP fields - investment and funding
:header-rows: 1
:widths: 26 16 24 12 8 14

* - Notation
  - Label
  - Definition
  - Type
  - Status
  - Condition or codelist
* - `investment`
  - Investment
  - Forecast investment cost needed for the plant.
  - nonNegativeValue (million EUR)
  - Required
  - –
* - `europeanUnionFund`
  - European Union fund
  - Planned EU funding. Report 0 if no EU funding is planned.
  - nonNegativeValue (million EUR)
  - Required
  - –
* - `europeanUnionFundName`
  - European Union fund name
  - Name of the EU fund planned for the plant.
  - EUFund_Enum
  - Conditional
  - If `europeanUnionFund` > 0. {ref}`art23-cl-eu-funds`
* - `producerResponsibilityFund`
  - Producer responsibility fund
  - Planned funding from producer responsibility organisations.
  - nonNegativeValue (million EUR)
  - Optional
  - –
* - `otherPublicFund`
  - Other public fund
  - Amount of other public funds planned to complete the plant (see note).
  - nonNegativeValue (million EUR)
  - Required
  - –
* - `otherPublicFundSpecification`
  - Other public fund specification
  - Type of other public funds.
  - OtherPublicFund_Enum
  - Conditional
  - If `otherPublicFund` > 0. {ref}`art23-cl-public-funds`
* - `loan`
  - Loan
  - Amount of loan planned to complete the plant.
  - nonNegativeValue (million EUR)
  - Required
  - –
* - `loanName`
  - Loan provider
  - Name of the entity planned to provide the loan.
  - string255
  - Conditional
  - If `loan` > 0
* - `remarks`
  - Remarks
  - Remarks on investments in the plant.
  - string1000
  - Optional
  - –
:::

The draft describes `otherPublicFund` as the "amount of funds planned to complete the UWWTP". The
field name and the related specification codelist show that it is meant for other public funds.
Unlike the corresponding Agglomeration fields, `otherPublicFund` and `loan` do not repeat the
instruction to report 0 if none.

## Filling in the table

* **Several measures at one plant.** You can select several measures, but each plant has one row
  with one set of dates and one investment total. How to report measures with different dates is
  open ({ref}`art23-oi-multiple-measures`).
* **Zero versus unknown.** 0 means none planned. See {ref}`art23-investments-zero-unknown`.
* **Reference year.** The draft does not define the reference year of `status`
  ({ref}`art23-oi-reference-dates`).

## Related open issues

* {ref}`art23-oi-scope`, {ref}`art23-oi-status`, {ref}`art23-oi-prioritisation`
* {ref}`art23-oi-multiple-funds`, {ref}`art23-oi-unknown`, {ref}`art23-oi-loans`
* {ref}`art23-oi-loads`, {ref}`art23-oi-dates`, {ref}`art23-oi-measures`
