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
measure has one or more types, and one period, one priority and one investment cost. The plants or
agglomerations it concerns are listed in the measure itself, in `euUWWTPCode` or
`euAgglomerationCode`, and the sources of its financing in {ref}`art23-measurefinancing`. See
{ref}`art23-investments`.

Listing the plants or agglomerations in a multi-valued field follows the Water Framework Directive,
whose `Measure` table lists the river basin districts a measure concerns in `euRBDCode [0..n]`.
Unlike the Water Framework Directive, which does not ask for the individual water bodies, Article
23(1)(b) asks for the investments "for each agglomeration", so the objects are listed.

```{mermaid} /rUWWTD2024/Article23/mmd/Article23_Measure_ClassDiagram.mmd
:name: Article23_Measure_ClassDiagram
:caption: Article 23 - Measure - draft
:align: center
```

In {numref}`Article23_Measure_ClassDiagram`, `[1]` marks the Required fields and `[0..1]` the
Optional and Conditional ones ({ref}`art23-requirement-status`).

## Measure, type and coverage

:::{list-table} Measure fields - measure, type and coverage
:header-rows: 1
:widths: 22 16 28 12 8 14

* - Notation
  - Label
  - Definition
  - Type
  - Status
  - Condition or codelist
* - `measureCode`
  - Measure code
  - Unique, persistent code of the measure. The same measure keeps the same code in later
    updates of the programme, so that its progress can be followed. Primary key.
  - wiseIdentifier
  - Required
  - –
* - `measureName`
  - Measure name
  - The original descriptive name of the measure, or an English translation of it.
  - string255
  - Required
  - –
* - `measureNameLanguage`
  - Measure name language
  - Language of `measureName`, as a code from the ISO 639-2 vocabulary.
  - Language
  - Required
  - {ref}`sp-cl-language`
* - `measureReference`
  - Measure reference
  - Place in a document that describes the measure, where there is one.
  - referenceCode
  - Optional
  - –
* - `uwwtdMeasureType`
  - Measure type
  - Type or types of the measure, by the article of the Directive they implement. Select one or
    more, as in the draft format. All the types of a measure concern the same kind of object:
    treatment plants, or agglomerations.
  - UWWTDMeasureType [1..n]
  - Required
  - {ref}`art23-cl-measure-type`
* - `measureText`
  - Other measure description
  - Description of another appropriate measure under Article 18(2).
  - string1000
  - Conditional
  - If `uwwtdMeasureType` includes `otherMeasureArticle18_2`
* - `geographicalCoverage`
  - Geographical coverage
  - Whether the measure applies to the whole Member State, to plants or agglomerations listed in
    `euUWWTPCode` or `euAgglomerationCode`, or to plants or agglomerations not yet identified.
  - UWWTDGeographicCoverage
  - Required
  - {ref}`art23-cl-coverage`
* - `euUWWTPCode`
  - Treatment plants
  - Codes of the treatment plants the measure concerns, as in the spatial points dataflow.
    Several codes are separated by commas. The identifier scheme is always `euUWWTPCode`.
  - wiseIdentifier [0..n]
  - Conditional
  - Required if
    `geographicalCoverage` =
    `listedObjects` and the
    measure types concern
    treatment plants; empty
    otherwise. Accepted codes
    in {ref}`sp-uwwtp`
* - `euAgglomerationCode`
  - Agglomerations
  - Codes of the agglomerations the measure concerns, as in the spatial points dataflow. Several
    codes are separated by commas. The identifier scheme is always `euAgglomerationCode`.
  - wiseIdentifier [0..n]
  - Conditional
  - Required if
    `geographicalCoverage` =
    `listedObjects` and the
    measure types concern
    agglomerations; empty
    otherwise. Accepted codes
    in {ref}`sp-agglomeration`
* - `numberOfObjects`
  - Number of plants or agglomerations
  - Number of plants or agglomerations concerned, where they are not listed, for example
    "10 plants".
  - nonNegativeInteger
  - Optional
  - Only if `geographicalCoverage` = `unlistedObjects`
* - `prioritisation`
  - Prioritisation
  - Priority of the measure, related to the size of the agglomeration and the level of
    environmental impact.
  - Priority
  - Required
  - {ref}`art23-cl-priority`
:::

## Status and dates

:::{list-table} Measure fields - status and dates
:header-rows: 1
:widths: 24 16 28 12 8 12

* - Notation
  - Label
  - Definition
  - Type
  - Status
  - Condition or codelist
* - `implementationStatus`
  - Implementation status
  - Whether the measure is planned, ongoing, executed or cancelled. In the first programme most
    measures are planned or ongoing.
  - PlannedOngoingExecutedCancelled
  - Required
  - {ref}`art23-cl-implementation-status`
* - `expectedStartYear`
  - Expected start year
  - Year in which the works start, or are expected to start.
  - gYear
  - Optional
  - –
* - `expectedCompletionYear`
  - Expected completion year
  - Year in which the measure is expected to be completed. For a measure at a treatment plant,
    the year of expected compliance, meaning 12 months of compliant samples.
  - gYear
  - Required
  - –
:::

Together, `expectedStartYear` and `expectedCompletionYear` give the period that the Water Framework
Directive reports as `implementationPeriod`.

## Cost

:::{list-table} Measure fields - cost
:header-rows: 1
:widths: 26 16 26 12 8 12

* - Notation
  - Label
  - Definition
  - Type
  - Status
  - Condition or codelist
* - `costStatus`
  - Cost status
  - Whether the investment cost is known, estimated or not yet known.
  - CostStatus
  - Required
  - {ref}`art23-cl-cost-status`
* - `investmentCost`
  - Investment cost
  - Investment cost of the measure: capital expenditure only, without operational or maintenance
    costs. The equivalent of capital expenditure in the Water Framework Directive.
  - nonNegativeValue (million units of national currency)
  - Conditional
  - Required unless `costStatus` = `unknown`; empty if it is
* - `millionUnitsOfNationalCurrency`
  - Currency
  - Currency of `investmentCost` and of the amounts in {ref}`art23-measurefinancing`, which are
    all in millions of that currency. Euro area Member States use EUR.
  - CurrencyCode
  - Conditional
  - Required if `investmentCost` or a financing amount is given. {ref}`art23-cl-currency`
* - `remarks`
  - Remarks
  - Any relevant comment on the measure.
  - string1000
  - Optional
  - –
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
* **Measures not tied to listed objects.** Use `geographicalCoverage` = `national` for measures
  for the whole Member State, such as the nationwide renewal of collecting systems, and
  `unlistedObjects` where the plants or agglomerations are not yet identified.
* **Cost unknown.** Set `costStatus` to `unknown` and leave `investmentCost` empty. Saying what is
  not known is a valid answer.
* **Currency.** Amounts are in millions of national currency, as in the Water Framework Directive:
  0.01 is 10 000 units. Use a full stop as the decimal separator.

## Related open issues

* {ref}`art23-oi-measure-model`, {ref}`art23-oi-measure-granularity`,
  {ref}`art23-oi-measure-codes`, {ref}`art23-oi-wfd`, {ref}`art23-oi-currency`
* {ref}`art23-oi-prioritisation`, {ref}`art23-oi-reference-dates`, {ref}`art23-oi-costs`
