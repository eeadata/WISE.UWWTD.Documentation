(art23-agglomeration)=
# Agglomeration

:::{warning} Draft
Draft baseline. Which agglomerations must be listed, the status and measure codelists and the
funding fields are still under discussion (see the open issues linked below).
:::

**Table status:** Conditional. Required where investments are planned in collecting systems or
individual systems.
**Rows:** one row per agglomeration. `code` is the primary key.

The table gives an overview of measures for collecting systems, individual systems and integrated
urban wastewater management plans, their cost and their funding sources. Rows are linked to the
list of agglomerations.

The draft lists agglomerations that are currently non-compliant, face upcoming deadlines, or are
at risk of future non-compliance, for example because of load increases, insufficient collecting
system capacity or the need to manage urban runoff. Whether compliant agglomerations with planned
renewal investments must also be listed is open ({ref}`art23-oi-scope`). See also
{ref}`art23-investments`.

## Agglomeration, status and measures

:::{list-table} Agglomeration fields - agglomeration, status and measures
:header-rows: 1
:widths: 22 16 26 10 10 16

* - Notation
  - Label
  - Definition
  - Type
  - Status
  - Condition or codelist
* - `code`
  - Agglomeration code
  - Unique code of the agglomeration, as specified by the Member State. Primary key.
  - wiseIdentifier
  - Required
  - –
* - `name`
  - Agglomeration name
  - Name of the agglomeration.
  - string255
  - Required
  - –
* - `status`
  - Status
  - Status of the agglomeration at the reference year.
  - Status_Enum
  - Required
  - {ref}`art23-cl-status`
* - `measures`
  - Measures
  - Measures to achieve compliance for collecting systems, individual systems and
    integrated urban wastewater management plans.
  - AgglomerationMeasure_Enum
  - Required
  - {ref}`art23-cl-agg-measures`
* - `prioritisation`
  - Prioritisation
  - Priority of the investment, related to the size of the agglomeration and the level of
    environmental impact.
  - Priority_Enum
  - Required
  - {ref}`art23-cl-priority`
:::

Unlike the plant `measure` field, the draft does not say explicitly whether several values can be
selected in `measures` ({ref}`art23-oi-multiple-measures`).

## Load and completion date

:::{list-table} Agglomeration fields - load and completion date
:header-rows: 1
:widths: 26 16 26 10 10 12

* - Notation
  - Label
  - Definition
  - Type
  - Status
  - Condition
* - `completionDate`
  - Completion date
  - Expected completion date of the collecting system or individual system works.
  - date
  - Required
  - –
* - `expectedLoad`
  - Expected load
  - Expected generated load of the agglomeration at the expected date of compliance.
  - nonNegativeValue (p.e.)
  - Required
  - –
* - `expectedLoadCollected`
  - Expected load collected
  - Expected percentage of the generated load collected through collecting systems at the
    expected date of compliance.
  - Percentage
  - Optional
  - –
* - `expectedLoadIndividualSystems`
  - Expected load in individual systems
  - Expected percentage of the generated load addressed through individual systems at the
    expected date of compliance.
  - Percentage
  - Optional
  - –
:::

## Investment and funding

:::{list-table} Agglomeration fields - investment and funding
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
  - Forecast investment cost for the collecting system or individual system.
  - nonNegativeValue (million EUR)
  - Required
  - –
* - `europeanUnionFund`
  - European Union fund
  - Planned EU funds to complete the collecting system or individual system. Report 0 if
    none.
  - nonNegativeValue (million EUR)
  - Required
  - –
* - `europeanUnionFundName`
  - European Union fund name
  - Name of the EU fund planned.
  - EUFund_Enum
  - Conditional
  - If `europeanUnionFund` > 0. {ref}`art23-cl-eu-funds`
* - `otherPublicFund`
  - Other public fund
  - Planned other public funds to complete the collecting system or individual system.
    Report 0 if none.
  - nonNegativeValue (million EUR)
  - Required
  - –
* - `otherPublicFundSpecification`
  - Other public fund specification
  - Type of other public funds.
  - OtherPublicFund_Enum
  - Conditional
  - Required if `otherPublicFund` > 0. {ref}`art23-cl-public-funds`
* - `loan`
  - Loan
  - Amount of loan planned to complete the collecting system or individual system. Report
    0 if none.
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
  - Any relevant comment on the collecting system or individual system.
  - string1000
  - Optional
  - –
:::

The Agglomeration table has no field for funding from producer responsibility organisations.

## Filling in the table

* **Collecting system and individual systems in the same agglomeration.** The agglomeration has
  one row, so `investment` holds the forecast cost of all measures reported for it. Use
  `expectedLoadCollected` and `expectedLoadIndividualSystems` to show the expected split of the
  load. Whether investments should be split by type is open
  ({ref}`art23-oi-multiple-measures`).
* **Treatment plant costs.** Report these in the {ref}`art23-uwwtp` table, not in `investment`.
* **Zero versus unknown.** 0 means none planned. See {ref}`art23-investments-zero-unknown`.

## Related open issues

* {ref}`art23-oi-scope`, {ref}`art23-oi-status`, {ref}`art23-oi-prioritisation`
* {ref}`art23-oi-measures` - individual systems in the measure codelist, and what Article 5
  compliance means at agglomeration level.
* {ref}`art23-oi-multiple-funds`, {ref}`art23-oi-unknown`, {ref}`art23-oi-loans`
* {ref}`art23-oi-loads`, {ref}`art23-oi-dates`
