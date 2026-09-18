(art23-investments)=
# Reporting investments

:::{warning} Draft
This page explains how the draft tables fit together. Where the draft does not answer a
question, this is said and the open issue is linked. No rules have been added beyond the draft.
:::

## Where to report each investment

:::{list-table} Where to report investments in the draft format
:header-rows: 1
:widths: 45 55

* - Investment
  - Where to report it
* - Measures at an identified treatment plant: a new plant, an upgrade to tertiary or quaternary
    treatment, stricter treatment following the risk assessment, or renewal including capacity
    increase
  - The plant's row in {ref}`art23-uwwtp`: measures in `measure`, cost in `investment`
* - Measures in the collecting system or individual systems of an identified agglomeration: new
    collecting systems, storm water overflow reduction, measures resulting from an IUWMP, or
    renewal
  - The agglomeration's row in {ref}`art23-agglomeration`: measures in `measures`, cost in
    `investment`
* - New collecting systems or plants required by the Directive but not yet attributed to a
    specific agglomeration or plant
  - {ref}`art23-otherinvestment`: `collectingSystemNewInvestment`, `treatmentPlantNewInvestment`
* - Renewal, upgrade or replacement of existing infrastructure not reported against a listed plant
    or agglomeration
  - {ref}`art23-otherinvestment`: `collectingSystemRenewalInvestment`, `treatmentPlantRenewalInvestment`
* - Contribution from producer responsibility organisations
  - {ref}`art23-mssummary`: `producerResponsibilityContribution` (national total); optionally `producerResponsibilityFund` per
    plant
* - Investment plans justifying deadline extensions
  - {ref}`art23-derogation`: links to the documents. The investments themselves are reported in
    the investment tables.
:::

## Compliant infrastructure and renewal

Article 23(1)(c) requires an estimate of the investments needed to renew, upgrade or replace
existing urban wastewater infrastructure in general, including collecting systems. In the draft:

* the measure code `23(1c)` covers renewal and replacement at plants (including capacity increase)
  and in collecting systems;
* plants and agglomerations are listed individually when they are non-compliant, face an upcoming
  deadline or are at risk of future non-compliance;
* renewal investments that are not reported against a listed plant or agglomeration are reported
  as totals in `collectingSystemRenewalInvestment` and `treatmentPlantRenewalInvestment`.

So renewal investments for compliant infrastructure are included either way: in the row of a
listed plant or agglomeration, or in the OtherInvestment totals. Whether compliant plants and
agglomerations with renewal investments must be listed individually is still to be decided
({ref}`art23-oi-scope`).

## Avoiding double counting

The draft defines total investment as the sum of the UWWTP, Agglomeration and OtherInvestment
tables. To keep that total correct, report each investment only once:

* Report treatment plant costs in `investment` and collecting system or individual system costs in
  `investment`. Do not add the cost of a plant to the agglomeration it serves, or the reverse.
* OtherInvestment amounts must exclude anything already reported in the UWWTP or Agglomeration
  tables.
* If OtherInvestment has several rows, for example one per year, do not include the same
  investment in more than one row.
* The Derogation table contains no amounts. Investments for agglomerations covered by an extension
  are reported in the investment tables like any other investment.
* Funding amounts (EU funds, other public funds, loans, PRO funding) describe how an investment is
  financed. They are not additional investments.

The draft does not state whether the funding amounts of a row must add up to its investment, or
how `producerResponsibilityFund` relates to the national `producerResponsibilityContribution` ({ref}`art23-oi-multiple-funds`,
{ref}`art23-oi-pro`). It has no field for financing from user charges.

## Several measures or investments at one plant or agglomeration

Each plant and each agglomeration has one row, because `code` is the primary key of both
  tables.
Each row has one investment amount, one amount per funding source and one set of dates:

* `measure` accepts several measures, so `investment` holds the forecast cost of all measures
  reported for the plant;
* `investment` holds the forecast cost of all collecting system and individual system measures
  reported for the agglomeration;
* `expectedYearStartWork` and `expectedYearPerformance` each take one year; `completionDate`
  takes one date.

The draft does not say which date to report when measures have different start or completion
dates. You can describe the separate measures and their dates in `remarks`. A decision on how
multiple measures and dates should be reported is pending ({ref}`art23-oi-multiple-measures`).

## Funding sources

Each investment table has a separate amount for each type of funding:

:::{list-table} Funding fields by table
:header-rows: 1
:widths: 25 25 25 25

* - Funding source
  - UWWTP
  - Agglomeration
  - OtherInvestment
* - EU funds
  - `europeanUnionFund`, `europeanUnionFundName`
  - `europeanUnionFund`, `europeanUnionFundName`
  - `europeanUnionFunds`, `europeanUnionFundsName`
* - Other public funds
  - `otherPublicFund`, `otherPublicFundSpecification`
  - `otherPublicFund`, `otherPublicFundSpecification`
  - `otherPublicFunds`, `otherPublicFundSpecification`
* - Loans
  - `loan`, `loanName`
  - `loan`, `loanName`
  - –
* - Producer responsibility organisations
  - `producerResponsibilityFund` (optional)
  - –
  - –
:::

The draft does not state whether more than one EU fund or more than one type of other public funds
can be named in a row. One proposal is to allow a list of fund names with a single total amount,
without splitting the amount between funds. This is not yet decided
({ref}`art23-oi-multiple-funds`).

(art23-investments-zero-unknown)=
## Zero versus unknown

* **0 means none planned.** The draft says to report 0 if there is none for `europeanUnionFund`,
  `europeanUnionFund`, `otherPublicFund`, `loan`, `collectingSystemNewInvestment`, `collectingSystemRenewalInvestment`, `treatmentPlantNewInvestment`, `treatmentPlantRenewalInvestment`,
  `europeanUnionFunds` and `otherPublicFunds`. When an amount is 0, the related fund name or specification is
  not required.
* **There is no "unknown" value.** Because 0 is read as "none planned", it should not be used to
  mean "not known". How to report a required amount that is not yet known is an open question.
  An explicit "unknown" option has been proposed ({ref}`art23-oi-unknown`).
* **Amounts known only as totals.** Where investments are known only as totals and not by plant or
  agglomeration, the draft allows them to be reported in {ref}`art23-otherinvestment`.
* **Optional fields.** An optional field such as `producerResponsibilityFund` can be left empty. The draft does
  not say whether an empty optional amount means zero or unknown.
* Use `remarks` to explain estimates and their uncertainty.

## Loans

The `loan` fields are Required in the draft, and the lender's name is required when the
amount is above 0. There is no loan field in OtherInvestment. Article 23(1)(d) refers to sources
of public financing. The draft does not define "loan", for example whether it covers public and
private lenders, and the EU fund codelist includes the European Investment Bank. Whether the loan
fields should be optional, and how they relate to the other funding fields, is still to be decided
({ref}`art23-oi-loans`).

## Prioritisation

Article 23(1)(b) requires a prioritisation of investments related to:

* the size of the agglomeration; and
* the level of environmental impact of discharges of untreated urban wastewater and the related
  risks for the environment or human health.

The Directive does not link priority to the timing of completion.

In the draft, the `prioritisation` fields take the values High, Medium or Low,
and `prioritisationReference` points to the national prioritisation methodology. The draft
description adds that "'High' should be used for projects that are scheduled for earlier
completion relative to others".

:::{important}
A proposal to remove this link between high priority and earlier completion is under
consideration, because high-priority projects can be complex and take longer to complete. It has
not been decided ({ref}`art23-oi-prioritisation`). Describe how priorities are set in the
methodology linked in `prioritisationReference`.
:::

## Reporting periods and dates

The draft uses several reference dates. They are listed in {ref}`art23-timing`. For investments:

* `expectedYearStartWork` and `expectedYearPerformance` are expected years, and
  `completionDate` is an expected date;
* OtherInvestment rows cover the period from `startYear` to `endYear`;
* the draft does not say whether investment amounts should cover the whole implementation period
  to 2045 or a shorter horizon, such as the six years until the next update
  ({ref}`art23-oi-reference-dates`).

## Projected loads and capacity

* `expectedLoad` is the planned load entering the plant at the expected date of compliance, that
  is the year in `expectedYearPerformance`, not necessarily 2045.
* `expectedCapacity` is the planned organic design capacity in p.e. Hydraulic capacity is not
  requested.
* `expectedLoad` is the expected generated load of the agglomeration at the expected date of
  compliance. `expectedLoadCollected` and `expectedLoadIndividualSystems` give the expected percentages collected and
  addressed through individual systems.

Articles 3(3) and 6(5) set out how the load of an agglomeration and the load entering a plant are
calculated: from the maximum average weekly load during the year, excluding unusual weather
situations. The draft does not say whether projected loads should be estimated on the same basis
({ref}`art23-oi-loads`).

## When to use OtherInvestment

Use {ref}`art23-otherinvestment` when an investment cannot be attributed to a single plant or
agglomeration. The draft gives these cases:

* investments in collecting systems and treatment plants for agglomerations below 2 000 p.e.
  newly covered by the Directive, where individual agglomerations or plants are not yet known;
* resources that, when the programme is approved, are allocated only within general frameworks.

Otherwise, report investments against individual plants and agglomerations. If everything is
attributed, leave the table empty.
