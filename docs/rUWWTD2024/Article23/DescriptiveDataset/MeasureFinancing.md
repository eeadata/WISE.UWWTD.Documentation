(art23-measurefinancing)=
# MeasureFinancing

:::{warning} Draft
Part of the proposed measure-first model ({ref}`art23-oi-measure-model`).
:::

**Table status:** Optional. Report it for each measure whose financing is at least partly known.
A measure whose cost is unknown can have no financing rows.
**Rows:** one row per measure and source of financing. The combination of `measureCode`,
`fundingSource`, `europeanUnionFundName` and `loanName` is unique.

The table breaks the investment cost of a measure in {ref}`art23-measure` down by where the money
comes from, and says how far each part is secured. Several EU funds for one measure are several
rows, each with its own amount. The financing gap of a measure is calculated, not reported: its
`investmentCost` minus the sum of the amounts with `fundingStatus` = `secured`.

The Water Framework Directive breaks expenditure down by the institutional sector that spends the
money. Article 23(1)(d) asks instead for the sources of financing, so this table uses sources of
funds.

```{mermaid} /rUWWTD2024/Article23/mmd/Article23_MeasureFinancing_ClassDiagram.mmd
:name: Article23_MeasureFinancing_ClassDiagram
:caption: Article 23 - MeasureFinancing - draft
:align: center
```

## MeasureFinancing fields

:::{list-table} MeasureFinancing fields
:header-rows: 1
:widths: 24 16 26 12 8 14

* - Notation
  - Label
  - Definition
  - Type
  - Status
  - Condition or codelist
* - `measureCode`
  - Measure code
  - Code of the measure in {ref}`art23-measure`.
  - wiseIdentifier
  - Required
  - Must exist in
    {ref}`art23-measure`
* - `fundingSource`
  - Funding source
  - Where the money comes from.
  - FundingSource
  - Required
  - {ref}`art23-cl-funding-source`
* - `europeanUnionFundName`
  - European Union fund name
  - Name of the EU fund.
  - EUFund
  - Conditional
  - Required if `fundingSource` = `europeanUnionFund`, empty otherwise.
    {ref}`art23-cl-eu-funds`
* - `loanName`
  - Loan provider
  - Name of the lender.
  - string255
  - Optional
  - Only if `fundingSource` = `loan`
* - `fundingStatus`
  - Funding status
  - How far the money from this source is secured.
  - FundingStatus
  - Required
  - {ref}`art23-cl-funding-status`
* - `amount`
  - Amount
  - Amount expected from this source, in the currency of the measure. Leave empty if not known.
  - nonNegativeValue (million units of national currency)
  - Optional
  - –
:::

## Filling in the table

* **Several funds.** Report each fund, or each type of public funds, in its own row with its own
  amount.
* **Money not yet found.** Report the part still without a source with `fundingSource` =
  `notIdentified` and `fundingStatus` = `notIdentified`.
* **Producer responsibility.** Funding from producer responsibility organisations for a measure is
  a row with `fundingSource` = `producerResponsibilityOrganisation`. The national total is
  reported in {ref}`art23-mssummary` ({ref}`art23-oi-pro`).
* **Loans.** A loan is an optional row; its lender and amount may be left empty
  ({ref}`art23-oi-loans`).
