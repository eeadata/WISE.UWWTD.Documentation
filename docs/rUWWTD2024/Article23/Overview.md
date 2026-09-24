(art23-overview)=
# Purpose and scope

:::{warning} Draft
Legal requirements on this page are taken from Directive (EU) 2024/3019. Everything described
as "the draft" is proposed reporting design and is not final.
:::

## Legal basis

By 1 January 2028, each Member State must establish a national implementation programme (NIP)
(Article 23(1)) {footcite:p}`urbanWastewaterTreatmentDirectiveRecast`. The programme must include:

(a) an assessment of the level of implementation of Articles 3 to 8;

(b) the identification and planning of the investments required to implement the Directive
    for each agglomeration, including an indicative financial estimation, an estimation of the
    financial contribution from producer responsibility organisations (PROs) when available,
    and a prioritisation of those investments related to the size of the agglomeration and the
    level of environmental impact of discharges of untreated urban wastewater and related risks;

(c) an estimate of the investments needed to renew, upgrade or replace existing urban wastewater
    infrastructure, including collecting systems;

(d) the identification, or at least an indication, of potential sources of public financing,
    when needed to complement user charges;

(e) any information required under Articles 6(3) and 7(4), where applicable.

Other provisions add content to the programme:

* Article 3(2) - where a Member State extends the deadline for collecting systems in
  agglomerations of 1 000 to 1 999 p.e., the first NIP must include the number of agglomerations
  concerned, an investment plan and the justification.
* Article 18(3) - a summary of the identified risks caused by urban wastewater discharges, with
  a description of the measures adopted, must be included in the NIP.
* Article 23(1), third subparagraph - where preserving cultural heritage makes it impossible to
  meet the deadlines of Article 3(2) or 6(3) in specific areas, the NIP must be updated with the
  agglomerations concerned, a justification and an adjusted timeline.

Recital 47 explains the intention: the programmes should include long-term programming of the
required investments accompanied by a financing strategy, and the Commission should consider them
when preparing future multiannual financial frameworks.

The Commission may adopt implementing acts on the methods and formats for submitting programmes
(Article 23(4)). The format described in this section is draft reporting guidance.

## Who reports

Member States submit their programmes to the Commission by 1 January 2028. A Member State does not
have to submit a programme if it demonstrates, on the basis of the monitoring results referred to
in Article 21, that it complies with Articles 3 to 8 (Article 23(2)). Programmes are updated at
least every six years (Article 23(3)). See {ref}`art23-timing`.

In the draft, the field `programmeObligation` in {ref}`art23-mssummary` records whether a programme
is required, and `situationAt` records the date of the reported situation.

## Where each part of the programme is reported

:::{list-table} Legal content of the programme and the draft tables that carry it
:header-rows: 1
:widths: 35 65

* - Legal content
  - Draft tables and fields
* - Article 23(1)(a) - level of implementation of Articles 3 to 8
  - {ref}`art23-selfassessment`: the Article 3 to 8 self-assessment fields.
    {ref}`art23-uwwtp` and {ref}`art23-agglomeration`: the `status` field of each.
* - Article 23(1)(b) - investments required to implement the Directive, PRO contribution and
    prioritisation
  - {ref}`art23-uwwtp`, {ref}`art23-agglomeration`, {ref}`art23-otherinvestment`
    (`collectingSystemNewInvestment`, `treatmentPlantNewInvestment`).
    {ref}`art23-mssummary`: `producerResponsibilityContribution`,
    `producerResponsibilityEstimateBasedOn`, `contributionPeriod`, `prioritisationReference`.
* - Article 23(1)(c) - renewal, upgrade or replacement of existing infrastructure
  - Measure code `23(1c)` in {ref}`art23-uwwtp` and {ref}`art23-agglomeration`;
    {ref}`art23-otherinvestment` (`collectingSystemRenewalInvestment`, `treatmentPlantRenewalInvestment`).
* - Article 23(1)(d) - sources of public financing
  - EU fund and other public fund fields in the three investment tables.
    The draft also asks for loans; see {ref}`art23-oi-loans`.
* - Article 23(1)(e) and Article 3(2) - derogation information
  - {ref}`art23-derogation`.
* - Article 23(1), third subparagraph - cultural heritage
  - {ref}`art23-derogation`: `article3_2CulturalHeritage`, `article6_3CulturalHeritage` and their links.
* - Article 18(3) - summary of risks and measures
  - {ref}`art23-mssummary`: `riskAssessment`, `riskDate`, `riskIdentified`, `riskSummaryReference`.
* - The programme document itself
  - {ref}`art23-mssummary`: `programmeReference`.
:::

## Which plants and agglomerations to list

The draft lists, in the {ref}`art23-uwwtp` and {ref}`art23-agglomeration` tables, only plants and
agglomerations that:

* are currently non-compliant;
* face upcoming implementation deadlines; or
* are at risk of future non-compliance, for example because of projected capacity constraints,
  load increases, more stringent requirements from the risk assessment, urban development or
  the need to manage urban runoff.

The same draft also makes the UWWTP table mandatory where investments are planned to renew,
upgrade or replace existing infrastructure, which can concern compliant plants. Whether compliant
plants and agglomerations with planned renewal investments must be listed individually is not
yet decided ({ref}`art23-oi-scope`).

Either way, renewal investments are part of the programme under Article 23(1)(c). Investments
that are not reported against a listed plant or agglomeration are reported as totals in the
{ref}`art23-otherinvestment` table. See {ref}`art23-investments`.

## Level of detail

The Directive asks for an indicative financial estimation, an estimate of renewal investments and
at least an indication of sources of public financing. The first programme is therefore expected
to reflect the best information available when it is prepared, and it is updated at least every
six years. Where investments are not yet allocated to specific plants or agglomerations, the draft
allows them to be reported as totals in {ref}`art23-otherinvestment`.

## Formats and tools

According to the draft guidance, data will be requested through
[Reportnet 3](https://reportnet.europa.eu/). Reporters will be able to enter data in the web
interface or upload CSV or Microsoft Excel files, and an Excel template will be provided. An API is
also available. The [Reportnet 3 help pages](https://help.reportnet.europa.eu/) describe the
platform.

* Reportnet 3 and API support: ServiceDesk@eea.europa.eu
* Thematic questions: uwwtd.helpdesk@eionet.europa.eu

Write remarks in English so that reported information can be compared.

```{footbibliography}
```
