(art23-selfassessment)=
# SelfAssessment

:::{warning} Draft
Draft baseline. The self-assessment fields were revised after the country consultation and are
still under review ({ref}`art23-oi-self-assessment`).
:::

**Table status:** Required.
**Rows:** one row per Member State.

The table records the Member State's own assessment, at national level, of compliance with
Articles 3 to 8 at the time of the first programme. According to the draft, a Member State that
is fully compliant with those Articles does not need to report the more detailed investment
tables.

```{mermaid} /rUWWTD2024/Article23/mmd/Article23_SelfAssessment_ClassDiagram.mmd
:name: Article23_SelfAssessment_ClassDiagram
:caption: Article 23 - SelfAssessment - draft
:align: center
```

In {numref}`Article23_SelfAssessment_ClassDiagram`, `[1]` marks the Required fields
({ref}`art23-requirement-status`). The reference to the published management plans is reported in
{ref}`art23-mssummary`.

## Self-assessment fields

Each field records the Member State's own assessment, at national level, of compliance with one
Article in the first programme. The draft notes that detailed information may not yet be
available, so Articles 3 and 6 are assessed as the share of compliant agglomerations, Article 4 as
a yes or no answer, Article 5 as a count of agglomerations, and Articles 7 and 8 as the share of
compliant treatment plants of 150 000 p.e. and above.

Each share is a range of percentages, from 0 to 100 (`PercentageRange`,
{ref}`art23-data-types`): the Member State gives the range its data supports, for
example `[76,85]`, or `[100,100]` when all comply. An exact share is a range of one value, such as
`[92,92]`.

Articles 3 and 6 are assessed separately for the two size bands, because the deadlines differ:
agglomerations of 2 000 p.e. and above, and agglomerations of 1 000 to 1 999 p.e.

:::{fieldtable} Article23/SelfAssessment
:::

:::{note}
Most deadlines of Articles 3 to 8 fall after 1 January 2028, so the first programme records an
expected position rather than a settled one. How a single national share is derived from plant or
agglomeration data is not stated. See {ref}`art23-oi-self-assessment`.
:::
