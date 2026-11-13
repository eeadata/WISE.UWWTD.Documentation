(art23-open-issues)=
# Open issues and proposed changes

:::{warning} Nothing on this page is decided
These questions were raised in the May 2026 consultation on the draft guidance, or found when
comparing the draft with its Figure 1 and with the Directive. None has been resolved. Until a
decision is published, the draft baseline described in this section applies. Proposals
listed here are not reporting requirements.
:::

(art23-oi-scope)=
## OI-01 Which plants and agglomerations to list

**Baseline.** Only plants and agglomerations that are non-compliant, face upcoming deadlines or are
at risk of future non-compliance are listed. The same draft makes the UWWTP table mandatory where
renewal investments are planned, and includes a renewal measure code.

**Question.** Must compliant plants and agglomerations with planned renewal, upgrade or
replacement be listed individually, or reported in national measures without listing them?
Article 23(1)(b) refers to investments for each agglomeration, and Article 23(1)(c) to existing
infrastructure in general.

**Under consideration.** Covering all plants and agglomerations, or listing only those needing
investment to reach or maintain compliance, with other renewal reported as national measures
({ref}`art23-oi-measure-model`).

(art23-oi-self-assessment)=
## OI-02 Self-assessment of Articles 3 to 8

**Baseline.** After the country consultation the self-assessment was restructured: Articles 3 and
6 are reported as the share of compliant agglomerations in percentage ranges, split between
agglomerations of 2 000 p.e. and above and those of 1 000 to 1 999 p.e.; Article 4 is a yes or no
answer on whether a system of authorisation and control of individual systems exists; Article 5 is
a count of agglomerations of 100 000 p.e. and above that already have an integrated urban
wastewater management plan; Articles 7 and 8 are the share of compliant treatment plants of
150 000 p.e. and above.

**Questions.**

* Is the share counted by number of agglomerations or by population equivalent?
* Articles 3 and 6 use six percentage bands for the larger agglomerations and five for the
  smaller ones, and Articles 7 and 8 use the five-band list. Should one set of bands be used
  throughout?
* How is a single national share derived where a Member State holds only plant-level data?
* Should the basis of each value be recorded, for example calculated or estimated?

(art23-oi-status)=
## OI-03 Plant and agglomeration status

**Baseline.** The plant and agglomeration `status` fields share one codelist that combines
Articles 3 to 8 with
Article 18.

**Questions.**

* Should plant status refer only to Articles 6 to 8, and agglomeration status to Articles 3 to 5?
* What does "pending deadline (time for submission of application)" mean?
* When is C used if only non-compliant cases are listed?
* How are agglomerations using individual systems under Article 4 reported?
* Should Article 18 be recorded separately?

(art23-oi-reference-dates)=
## OI-04 Reference date and investment horizon of the first programme

**Baseline.** Several dates are used: the situation date (`situationAt`), compliance "as at
1 January 2028", derogation figures on 1 January 2025, and an undefined "reference year" for plant
and agglomeration status.

**Questions.** Which period should the first programme's information describe, and may data
collected for earlier reporting under Directive 91/271/EEC be reused? Should investment amounts
cover the whole implementation period to 2045 or a shorter horizon?

**Proposed answer.** Align with the Water Framework Directive cycles ({ref}`art23-cycles`).
Capital expenditure is reported for the 1st cycle, 2028 to 2033, and in one amount for the period
after it, to 2045, so that the whole investment to compliance is covered. Expenditure before 2028
is not reported.

(art23-oi-prioritisation)=
## OI-05 Prioritisation

**Baseline.** High, Medium or Low, with "'High' should be used for projects that are scheduled
for earlier completion relative to others".

**Proposed change.** Remove the link between high priority and earlier completion, because
high-priority projects can take longer. The legal criteria are the size of the agglomeration and
the level of environmental impact and related risks.

**Other questions.** Definitions for comparability, the level at which priority is assessed, and
whether the field could be optional in the first programme.

(art23-oi-multiple-measures)=
## OI-06 Several measures and dates per plant or agglomeration

**Baseline.** One row per plant or agglomeration, with one investment total and one set of dates.
`treatmentPlantMeasure` accepts several measures. `agglomerationMeasure` does not say.

**Question.** How should measures with different dates, or collecting system and individual system
investments in the same agglomeration, be reported?

**Proposed answer.** In the measure model, each measure is its own row with its own dates and
cost, linked to the plant or agglomeration ({ref}`art23-oi-measure-model`).

(art23-oi-multiple-funds)=
## OI-07 Several funds in one row

**Baseline.** One fund name or specification per row. The draft does not state whether several
can be given, or whether funding amounts must add up to the investment.

**Under consideration.** Allowing several fund names with one total amount and no split between
funds.

**Proposed answer.** In the measure model, each source of financing, and each EU fund, is its own
row in MeasureFinancing with its own amount, so the multi-select question no longer arises
({ref}`art23-oi-measure-model`).

(art23-oi-unknown)=
## OI-08 Unknown amounts and uncertain costs

**Baseline.** Amounts are required, and 0 means none. There is no "unknown" value.

**Under consideration.** Adding an "unknown" option, allowing more flexibility where costs cannot
yet be estimated, and using OtherInvestment for aggregated estimates. A minimum threshold for
reporting investments was also suggested.

**Proposed answer.** Article 23(1)(b) asks for an indicative financial estimation, so a rough
estimate is reported as `costStatus` = `estimated`. In the measure model, `costStatus` =
`unknown` with empty expenditure fields remains possible as an exception, where not even a rough
estimate can be given, but raises a warning (check R16). No minimum threshold applies
({ref}`art23-oi-measure-model`).

(art23-oi-loans)=
## OI-09 Loan fields

**Baseline.** The `loan` fields of both investment tables are Required. Lender names are
required when the amount is
above 0.

**Questions.** What is the legal basis and purpose, given that Article 23(1)(d) refers to public
financing? Does "loan" cover public and private lenders? How do loans relate to the EU fund
codelist, which includes the European Investment Bank?

**Under consideration.** Making the loan fields optional.

**Proposed answer.** In the measure model, a loan is an optional source of financing in
MeasureFinancing, with an optional lender name and amount.

(art23-oi-pro)=
## OI-10 Producer responsibility contribution

**Questions.** Which period does `producerResponsibilityContribution` cover, and is the amount
nominal? Which
requirements does `contributionPeriod` refer to, and should it be Required now that it replaces
four Required questions?
How does PRO funding reported for individual measures, with `fundingSource` =
`producerResponsibilityOrganisation`, relate to the national total?

**Proposed answer, unknown estimates.** Article 23(1)(b) asks for the contribution "when
available". `producerResponsibilityEstimateBasedOn` stays Required and has the value
`notAvailable`; the amount and its currency are then left empty (check R15). This also covers the
first programme, when the PROs may not yet be recognised.

(art23-oi-costs)=
## OI-11 Nominal or annualised costs

**Question.** Are amounts (the capital expenditure, the financing amounts and
`producerResponsibilityContribution`) nominal or annualised? If annualised, which assumptions
should be reported?

(art23-oi-loads)=
## OI-12 Projected loads and capacity

**Questions.** Is the expected load estimated for the expected date of compliance of the measure
or for a fixed year? On what basis is it calculated? What does the expected collected share refer
to when new connections extend the area served by a plant?

(art23-oi-dates)=
## OI-13 Start and completion dates

**Question.** The plant fields are reported as years (`expectedYearStartWork`,
`expectedYearPerformance`). Where planning is uncertain, is an expected year enough for
`completionDate` as well?

**Proposed answer.** In the measure model, every measure has an `implementationPeriod`, a range
of years as in the Water Framework Directive. The completion year is required and the start year
may be left open.

(art23-oi-measures)=
## OI-14 Measure codelists

**Questions.**

* What does compliance with Article 5 mean at agglomeration level?
* Should energy neutrality, a plant-level code, be reported per plant?
* Should small plants selected under Article 18(2) be listed?
* What codes will be used in the template?

**Proposed answer.** In the measure model, the two measure codelists are merged into
`UWWTDMeasureType`, which stays multiple choice as in the draft. It includes individual systems
under Article 4, and
separate renewal values for collecting systems and treatment plants
({ref}`art23-cl-measure-type`).

(art23-oi-derogation)=
## OI-15 Derogation details

**Baseline.** One row per Member State with 25 fields, repeating the same questions for each
provision. The extension is a number of whole years. Cultural heritage is a Required yes/no for
Articles 3(2) and 6(3) with one link, and Article 6(4) a Required yes/no with one study link. For
Article 3(2), either the numbers of agglomerations or the loads are required, so the number
lacking collecting systems can be left out; for Article 6(3), all four numbers are required.

**Proposal.** Three tables, following the suggestions to separate type, rationale and period and
to derive the checks from the legal conditions:

* {ref}`art23-derogation`: one row per provision, Articles 3(2), 6(3) and 7(4), also where no
  extension is requested. The extended deadline is a year, checked against the maximum that
  follows from the reported shares. The number of agglomerations not meeting the requirement is
  always required, as the Directive lists it; the other numbers only for the criterion the Member
  State relies on, agglomerations or load.
* {ref}`art23-culturalheritageextension`: one row per agglomeration and area, in programme updates
  only. The Directive places these extensions in an update made during implementation, with a
  list of agglomerations and an adjusted timeline, which a national yes/no cannot hold.
* {ref}`art23-lessstringenttreatment`: one row per agglomeration, Optional. Less stringent
  treatment is not a deadline extension, and Article 23(1)(e) names only Articles 6(3) and 7(4).

**Questions.**

* What counts as a complete collecting system, including where individual systems are used?
* How are agglomerations served by one plant each treated?
* Does the cultural heritage maximum of 8 years run from 31 December 2035, or from a deadline
  already extended under Article 3(2) or 6(3)?
* Does Article 6(4) belong in the Article 23 dataflow, or should the studies be provided to the
  Commission another way? At which level should it be reported ({ref}`art23-oi-less-sensitive`)?
* What content is expected in the linked plans and justifications?

(art23-oi-risk)=
## OI-16 Risk assessment fields

**Questions.** How should a risk assessment that covers only some discharges be reported? Is a
link to the river basin management plan appropriate, and can it be prefilled?

(art23-oi-naming)=
## OI-17 Field names, data types and statuses

**Baseline.** Figure 1 of the draft guidance and its field tables differ in several places, in
field names, data types and requirement statuses. The field tables are followed in this
documentation.

**Proposals.**

* Use one set of identifiers and types: url for link fields, and consistent capitalisation of
  EU.
* Decide whether `expectedLoadCollected` and `expectedLoadIndividualSystems` are optional or
  conditional.
* Adopt notations that write acronyms out in full and do not repeat the table name, as used in
  this documentation ({ref}`art23-notation`), instead of the draft's `uww`, `agg`, `con`, `inv`
  and `pro` prefixes.
* Add a short label for every field.

(art23-oi-otherinvestment)=
## OI-18 OtherInvestment reference period

**Question.** Which period do `startYear` and `endYear` describe, for example the
programme's six years, individual years, or the period to 2045?

**Proposed answer.** In the measure model, the OtherInvestment table is removed. Its amounts become
national renewal measures, or measures for listed plants or agglomerations, each with its own
years ({ref}`art23-oi-measure-model`).

(art23-oi-confidentiality)=
## OI-19 Publication of cost estimates

**Question.** Will investment estimates per plant or agglomeration be made public? Some estimates
may be commercially sensitive.

(art23-oi-documents)=
## OI-20 Documents dataset

**Baseline.** The draft reporting guidance gives every document as a url field on the reporting
table itself: the programme, the prioritisation methodology, the investment plans, the extension
reasons, the cultural heritage lists, the Article 6(4) study and the risk summary.

**Proposal.** Follow the WISE convention used in the other dataflows and deliver documents in a
separate documents dataset ({ref}`art23-documents-dataset`). The reporting tables then hold a
`referenceCode` instead of a web address, and each document is delivered once, as a hyperlink or
as a file uploaded to Reportnet 3.

**Questions.**

* Should a Member State be allowed to upload the programme, or must it be published online?
* Is one row per cited chapter workable for Reporters, or should a document be cited as a whole?

(art23-oi-coordinates)=
## OI-21 Coordinates of new plants and agglomerations

**Resolved.** Names and locations are no longer reported in the Article 23 tables. Every
treatment plant and agglomeration is identified and located once, in the {ref}`spatial-points`
dataflow. That dataflow starts from the objects reported under Directive 91/271/EEC, stays open
for updates, and is first opened together with the Article 23 dataflow. The UWWTP and
Agglomeration tables refer to it by `thematicIdIdentifier`. A new plant or agglomeration is
reported there first, and only accepted codes can be referred to ({ref}`sp-references`). The
questions on the coordinate reference system and on the point representing an agglomeration are
dealt with in that dataflow ({ref}`sp-location`).

(art23-oi-measure-model)=
## OI-22 Measure-first model

**Baseline.** Investment, funding and measure fields are spread over the UWWTP, Agglomeration and
OtherInvestment tables. OtherInvestment holds only the investments not attributed to a single plant
or agglomeration, and the total investment is the sum of the three tables. That sum is right only if
nothing is reported in two tables, which the draft leaves to an instruction. A plant or
agglomeration has one start and one completion date, one EU fund and one loan, so several
measures, dates or funds for one object cannot be told apart.

**Proposal.** Report each investment as a measure, as the Water Framework Directive does in its
programme of measures. Article 23(1) itself speaks of investments, not measures; the Directive
uses "measures" in Article 18(2) and (3), whose summary of measures goes both into the river basin
management plans and into the programme. The proposal is a
Measure table with one row per measure, listing the plants or agglomerations it concerns in a
multi-valued field as the Water Framework Directive lists river basin districts, and a
MeasureFinancing table giving its sources of financing
({ref}`art23-investments`). UWWTP and Agglomeration keep only the state of the object.

**Questions.**

* Terminology: should the tables and guidance use "measure" and "cost of measure", while keeping
  the references to Article 23(1)(b) to (d), which speak of investments?
* Is `costStatus` = `unknown`, with empty expenditure fields, accepted as an exception with a
  warning (OI-08), or should an indicative estimate always be required?
* Are `secured`, `appliedFor`, `planned` and `notIdentified` the funding statuses the Commission
  needs to assess progress?

(art23-oi-measure-granularity)=
## OI-23 Types and completion year of a measure

**Proposal.** As in the draft format, a measure can have several types, all for the same kind of
object, with one cost that is not split between them. A measure has one completion year: if the
plants or agglomerations under one measure finish in different years, the measure is split.

**Questions.** Are totals per measure type needed? With several types per measure, they are only
exact for measures with a single type. Is a completion year per plant or agglomeration needed? It
would need a separate table linking measures and objects, instead of the multi-valued field.

(art23-oi-measure-codes)=
## OI-24 Persistent measure codes

**Proposal.** As in the Water Framework Directive, `measureCode` is a persistent identifier: a
measure keeps its code in later updates of the programme, so that its implementation status and
progress can be followed.

**Question.** Should measure codes be registered, like the codes of plants and agglomerations in
the spatial points dataflow, or only checked against the previous programme?

(art23-oi-wfd)=
## OI-25 Reporting measures once

**Proposal.** Measures for urban wastewater treatment plants and collecting systems are reported
once, in this dataflow, and not again in the programme of measures under the Water Framework
Directive. The Water Framework Directive classifies such measures under the key type of measure
`X01` (construction or upgrades of wastewater treatment plants) or `G` (measures to control point
source discharges) with the pressure `P1-1` (urban waste water). Each UWWTD measure type
corresponds to such a key type and pressure, derived centrally ({ref}`art23-cl-measure-type-wfd`).

**Questions.**

* Is this agreed with the Water Framework Directive reporting, so that Member States are told not
  to report these measures there?
* Is the proposed correspondence between measure types and WFD key types correct, including the
  measure types without a direct equivalent?

(art23-oi-listed-objects)=
## OI-26 Plants and agglomerations in the state tables

**Proposal.** Every plant or agglomeration listed in a measure, in `euUWWTPCode` or
`euAgglomerationCode`, also has a row in UWWTP or Agglomeration, with its status and expected load.
Since every measure with listed objects names its agglomerations, including the agglomerations
served by a plant, Article 23(1)(b) is met: the investments required to implement the Directive
can be identified "for each agglomeration" ({ref}`art23-each-agglomeration`). National measures
are only for renewal under Article 23(1)(c), and measures whose agglomerations are not yet
identified raise a warning.

**Questions.**

* Should plants and agglomerations without a planned measure, for example non-compliant ones whose
  measures are not yet decided, also be listed in UWWTP and Agglomeration?
* Can the agglomerations named with a plant be checked against a plant–agglomeration link, for
  example one reported under Article 22? The spatial points dataflow has no such link (SP-03).

(art23-oi-currency)=
## OI-27 Currency

**Proposal.** As in the Water Framework Directive, amounts are reported in millions: of euro by
euro area Member States, and of national currency by the others, with the currency code in
`millionUnitsOfNationalCurrency`. The draft reports all amounts in million EUR.

**Question.** Which exchange rate and date are used when amounts are converted for comparison?

(art23-oi-less-sensitive)=
## OI-28 Less sensitive areas and less stringent treatment

**Baseline.** The draft has a Required yes/no on Article 6(4) less stringent treatment, with one
study link. Less sensitive areas are not reported.

**Gap.** Two provisions allow treatment less stringent than secondary treatment, and both are
worded as discharges into particular waters:

* Article 6(2): for agglomerations discharging into less sensitive areas under Article 6(1) of
  Directive 91/271/EEC on 1 January 2025, secondary treatment applies from 31 December 2037.
  Under Article 32(5), Article 6 of Directive 91/271/EEC continues to apply to them until
  30 December 2037. Compliance checking needs to know which discharges this concerns. The
  proposal does not cover it.
* Article 6(4): discharges into high mountain waters, certain deep marine waters or in cold
  climates may have less stringent treatment until 31 December 2045. The proposal lists the
  agglomerations concerned in {ref}`art23-lessstringenttreatment`.

An agglomeration can discharge into several receiving waters, of which only some are less
sensitive or qualify under Article 6(4), so a list of agglomerations cannot always say which
discharges are concerned.

**Alternative proposal (ETC).** Report less sensitive areas and less stringent treatment at the
level of the discharge point, in the {ref}`sp-dischargepoint` table reported under Article 22, and
keep at most a flag in the Article 23 dataflow, or none.

**Questions.**

* At which level does the Commission need this information for compliance checking: area,
  discharge point or agglomeration?
* Are less sensitive areas still reported as spatial areas, or only through the discharge points
  that discharge into them?
* If discharge points are used, are the Article 6(4) studies still referenced from the Article 23
  dataflow?
