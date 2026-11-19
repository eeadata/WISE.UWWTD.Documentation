(art23-mssummary)=
# MSSummary

:::{warning} Draft
Draft baseline. Field names, types and statuses are not final.
:::

**Table status:** Required.
**Rows:** one row per Member State.

The table gives an overview of the programme: whether one is required, references to it and to
the prioritisation methodology, the Article 18 risk assessment, and the estimated contribution
from producer responsibility organisations (PROs). The national self-assessment of compliance
with Articles 3 to 8 is reported in {ref}`art23-selfassessment`.

According to the draft, a Member State that is fully compliant with Articles 3 to 8 does not need
to report the more detailed tables.

```{mermaid} /rUWWTD2024/Article23/mmd/Article23_MSSummary_ClassDiagram.mmd
:name: Article23_MSSummary_ClassDiagram
:caption: Article 23 - MSSummary - draft
:align: center
```

In {numref}`Article23_MSSummary_ClassDiagram`, `[1]` marks the Required fields and `[0..1]` the
Optional and Conditional ones ({ref}`art23-requirement-status`).

## Programme and references

:::{fieldtable} Article23/MSSummary
:group: programme-and-references
:::

The programme is updated at least every six years, unless the Member State is fully compliant
with Articles 3 to 8.

## Risk assessment

Article 18(1) requires Member States to identify and assess the risks caused by urban wastewater
discharges by 31 December 2027. Article 18(3) requires a summary of the identified risks and of
the measures adopted to be included in the programme.

:::{fieldtable} Article23/MSSummary
:group: risk-assessment
:::

A risk assessment covering only some discharges is reported as `partially`. How the three
conditional fields apply in that case is open ({ref}`art23-oi-risk`).

## Producer responsibility contribution

Article 23(1)(b) asks for an estimation of the financial contribution from PROs "when available".
In the first programme a Member State may estimate the contribution for the whole period or for
the period of an interim target, and assign it to that period. Where no estimate is available yet,
for example because the PROs are not yet recognised, the Member State reports
`producerResponsibilityEstimateBasedOn` = `notAvailable` and leaves the amount and its currency
empty. An empty amount then always means that no estimate is available, not that it was
forgotten.

:::{fieldtable} Article23/MSSummary
:group: producer-responsibility-contribution
:::

The years 2033, 2036, 2039 and 2045 are the interim and final deadlines of Articles 7 and 8. A
Member State that has estimated its contribution over a longer period, such as 2028 to 2045, or
that works to a different budgetary cycle, selects `other` and describes the period in
`contributionPeriodOther`.
