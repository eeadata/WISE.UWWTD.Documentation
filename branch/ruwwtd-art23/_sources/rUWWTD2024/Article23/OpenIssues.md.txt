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
replacement investments be listed individually, or reported as totals in OtherInvestment?
Article 23(1)(b) refers to investments for each agglomeration, and Article 23(1)(c) to existing
infrastructure in general.

**Under consideration.** Covering all plants and agglomerations, or listing only those needing
investment to reach or maintain compliance, with other investments reported as totals.

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
`measure` accepts several measures. `measures` does not say.

**Question.** How should measures with different dates, or collecting system and individual system
investments in the same agglomeration, be reported?

(art23-oi-multiple-funds)=
## OI-07 Several funds in one row

**Baseline.** One fund name or specification per row. The draft does not state whether several
can be given, or whether funding amounts must add up to the investment.

**Under consideration.** Allowing several fund names with one total amount and no split between
funds.

(art23-oi-unknown)=
## OI-08 Unknown amounts and uncertain costs

**Baseline.** Amounts are required, and 0 means none. There is no "unknown" value.

**Under consideration.** Adding an "unknown" option, allowing more flexibility where costs cannot
yet be estimated, and using OtherInvestment for aggregated estimates. A minimum threshold for
reporting investments was also suggested.

(art23-oi-loans)=
## OI-09 Loan fields

**Baseline.** The `loan` fields of both investment tables are Required. Lender names are
required when the amount is
above 0.

**Questions.** What is the legal basis and purpose, given that Article 23(1)(d) refers to public
financing? Does "loan" cover public and private lenders? How do loans relate to the EU fund
codelist, which includes the European Investment Bank?

**Under consideration.** Making the loan fields optional.

(art23-oi-pro)=
## OI-10 Producer responsibility contribution

**Questions.** Which period does `producerResponsibilityContribution` cover, and is the amount
nominal? Which
requirements does `contributionPeriod` refer to, and should it be Required now that it replaces
four Required questions? Should there be an "unknown"
option? Can the fields be optional in the first programme, when estimates may not be available?
How does `producerResponsibilityFund` relate to the national total?

(art23-oi-costs)=
## OI-11 Nominal or annualised costs

**Question.** Are investment amounts (the `investment` fields and
`producerResponsibilityContribution`) nominal or
annualised? If annualised, which assumptions should be reported?

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

(art23-oi-measures)=
## OI-14 Measure codelists

**Questions.**

* Should new or existing individual systems be added to the agglomeration measures?
* What does compliance with Article 5 mean at agglomeration level?
* Should energy neutrality, a plant-level code, be reported per plant?
* Should small plants selected under Article 18(2) be listed?
* Should the plant measure field be named in the plural, as Figure 1 does?
* What codes will be used in the template?

(art23-oi-derogation)=
## OI-15 Derogation details

**Questions.**

* What counts as a complete collecting system, including where individual systems are used?
* How are agglomerations served by one plant each treated?
* The Article 3(2) condition asks for numbers or loads, but the Article 6(3) condition asks for
  both.
* Should the Article 6(4) study be optional where studies are not yet complete?
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
