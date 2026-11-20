(art23-measurefinancing)=
# MeasureFinancing

:::{warning} Draft
Part of the proposed measure-first model ({ref}`art23-oi-measure-model`).
:::

**Table status:** Conditional. Required for each measure in {ref}`art23-measure` whose
`costStatus` is `known` or `estimated`: such a measure has at least one row. A measure whose cost is
unknown has no rows.
**Rows:** one row per measure and source of financing. The combination of `measureCode`,
`fundingSource`, `europeanUnionFundName` and `loanName` is unique.

The table gives the capital expenditure of each measure in {ref}`art23-measure`, source by source
and cycle by cycle, and says how far each part is secured. Several EU funds for one measure are
several rows, each with its own expenditure. The cost of a measure is the sum of both expenditure
fields over its rows. The financing gap of a measure is calculated, not reported: the sum of the
expenditure of its rows whose `fundingStatus` is not `secured`.

The table follows the `ExpenditurePerMeasurePerSector` table of the Water Framework Directive 4th
cycle, which gives the capital expenditure of each measure per cycle, in one row per institutional
sector. Article 23(1)(d) asks for the sources of financing, so this table has one row per source of
funds instead of per institutional sector.

```{mermaid} /rUWWTD2024/Article23/mmd/Article23_MeasureFinancing_ClassDiagram.mmd
:name: Article23_MeasureFinancing_ClassDiagram
:caption: Article 23 - MeasureFinancing - draft
:align: center
```

## MeasureFinancing fields

:::{fieldtable} Article23/MeasureFinancing
:::

## Filling in the table

* **Several funds.** Report each fund, or each type of public funds, in its own row with its own
  expenditure.
* **The whole cost.** The rows of a measure together give its whole capital expenditure from 2028.
  Report the part still without a source with `fundingSource` = `notIdentified` and
  `fundingStatus` = `notIdentified`. Where no source is known yet, the measure has one such row
  with all its expenditure.
* **Splitting by cycle.** Give the expenditure expected in 2028 to 2033 in
  `totalCapitalExpenditure1stCycle`, and what follows from 2034 in
  `totalCapitalExpenditureAfter1stCycle`, each where the `implementationPeriod` of the measure falls
  in that period. Where the yearly profile of a source is not known, split it between the cycles in
  the same proportion as the measure, or spread it evenly over the years of `implementationPeriod`.
  For an ongoing measure, report only what is spent from 2028.
* **Currency.** Expenditure is in millions of national currency, as in the Water Framework
  Directive: 0.01 is 10 000 units. Use a full stop as the decimal separator, and the same
  `millionUnitsOfNationalCurrency` in every row.
* **Producer responsibility.** Funding from producer responsibility organisations for a measure is
  a row with `fundingSource` = `producerResponsibilityOrganisation`. The national total is
  reported in {ref}`art23-mssummary` ({ref}`art23-oi-pro`).
* **Loans.** A loan is an optional row; its lender may be left empty ({ref}`art23-oi-loans`).
