(art23-measure)=
# Measure

:::{warning} Draft
Proposal for a measure-first model, replacing the investment and funding fields of the UWWTP and
Agglomeration tables and the OtherInvestment table. It follows the structure of the Water
Framework Directive 4th-cycle `Measure` table where that makes sense ({ref}`art23-oi-measure-model`).
:::

**Table status:** Conditional. Required where the programme plans measures in collecting systems,
individual systems or treatment plants, or the renewal of existing infrastructure.
**Rows:** one row per measure. `measureCode` is the primary key.

A measure is something the Member State plans to do to reach or maintain compliance with the
Directive, or to renew, upgrade or replace existing infrastructure: for example, a new collecting
system, an upgrade to tertiary treatment, or the renewal of collecting systems nationwide. Each
measure has one or more types, and one period, one priority and one capital expenditure,
split between the 1st cycle and after it. The plants it
concerns are listed in the measure itself, in `euUWWTPCode`, and the agglomerations in
`euAgglomerationCode`; the sources of its financing are given in {ref}`art23-measurefinancing`.
See {ref}`art23-investments`.

Listing the plants or agglomerations in a multi-valued field follows the Water Framework Directive,
whose `Measure` table lists the river basin districts a measure concerns in `euRBDCode [0..n]`.
Unlike the Water Framework Directive, which does not ask for the individual water bodies, Article
23(1)(b) asks for "the identification and planning of investments required to implement this
Directive for each agglomeration". Every measure with listed objects therefore names its
agglomerations, including a measure at a treatment plant, which also names the agglomerations the
plant serves.

```{mermaid} /rUWWTD2024/Article23/mmd/Article23_Measure_ClassDiagram.mmd
:name: Article23_Measure_ClassDiagram
:caption: Article 23 - Measure - draft
:align: center
```

In {numref}`Article23_Measure_ClassDiagram`, `[1]` marks the Required fields and `[0..1]` the
Optional and Conditional ones ({ref}`art23-requirement-status`).

## Measure, type and coverage

:::{fieldtable} Article23/Measure
:group: measure-type-and-coverage
:::

## Status and dates

:::{fieldtable} Article23/Measure
:group: status-and-dates
:::

The field is the same as `implementationPeriod` in the Water Framework Directive measures.

## Cost

:::{fieldtable} Article23/Measure
:group: cost
:::

## Filling in the table

* **Several types, one measure.** A project with one budget and one completion year that covers
  several types, for example an upgrade to tertiary and to quaternary treatment under one
  contract, is one measure with all its types. Its cost is given once and is not split between the
  types. Projects with their own dates or costs are separate measures.
* **Several measures at one plant.** Report each measure as its own row, each with the plant's
  code in `euUWWTPCode`. Each keeps its own dates and cost.
* **One measure, several plants or agglomerations.** List all their codes in the one field,
  separated by commas. The cost is given once, for the whole measure.
* **A measure at a treatment plant.** List the plant in `euUWWTPCode` and the agglomerations it
  serves in `euAgglomerationCode`. The cost is given once and is not divided between the
  agglomerations.
* **National measures.** `geographicalCoverage` = `national` is only for the renewal of existing
  infrastructure under Article 23(1)(c), such as the nationwide renewal of collecting systems,
  which the Directive does not ask for per agglomeration.
* **Plants and agglomerations are always listed.** Article 23(1)(b) asks for the investments for
  each agglomeration, so every measure other than a national renewal measure lists the
  agglomerations it concerns, and the plants for a measure at treatment plants. Where the order
  or the cost of the work is not yet known, the measure is still reported against them.
* **Indicative cost.** Article 23(1)(b) asks for an indicative financial estimation, so a rough
  estimate is enough and is reported as `estimated`. Where not even a rough estimate can be given
  yet, set `costStatus` to `unknown` and leave both expenditure fields empty. This raises a
  warning, and the cost should be estimated in the next update.
* **Splitting by cycle.** Give the capital expenditure expected in 2028 to 2033 in
  `totalCapitalExpenditure1stCycle`, and what follows from 2034 in
  `totalCapitalExpenditureAfter1stCycle`. Where the yearly profile is not known, spread the cost
  evenly over the years of `implementationPeriod`. For an ongoing measure, report only what is
  spent from 2028. The cost of the measure is the sum of the two fields.
* **Currency.** Amounts are in millions of national currency, as in the Water Framework Directive:
  0.01 is 10 000 units. Use a full stop as the decimal separator.

## Related open issues

* {ref}`art23-oi-measure-model`, {ref}`art23-oi-measure-granularity`,
  {ref}`art23-oi-measure-codes`, {ref}`art23-oi-wfd`, {ref}`art23-oi-currency`
* {ref}`art23-oi-prioritisation`, {ref}`art23-oi-reference-dates`, {ref}`art23-oi-costs`
