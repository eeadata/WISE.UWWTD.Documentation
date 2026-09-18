(art23-timing)=
# Reporting timing and reference dates

:::{warning} Draft
The legal deadlines below are taken from Directive (EU) 2024/3019
{footcite:p}`urbanWastewaterTreatmentDirectiveRecast`. The reference dates used in the reporting
tables are draft design and may change.
:::

## Legal deadlines relevant to the programme

:::{list-table} Legal deadlines
:header-rows: 1
:widths: 20 58 22

* - Date
  - Obligation
  - Provision
* - 1 January 2025
  - The Directive enters into force. This is also the reference date for the conditions of the
    deadline extensions and for the figures reported with them.
  - Article 34; Articles 3(2), 6(3), 7(4)
* - 31 July 2027
  - Transposition of Articles 2 to 11 and 14 to 26, including Article 23, into national law.
  - Article 33(1)
* - 1 August 2027
  - Directive 91/271/EEC is repealed.
  - Article 32(1)
* - 31 December 2027
  - List of areas sensitive to eutrophication. Identification and assessment of risks caused by
    urban wastewater discharges.
  - Articles 7(2), 18(1)
* - 1 January 2028
  - Establish the first programme and submit it to the Commission, unless compliance with
    Articles 3 to 8 is demonstrated. Article 17 of Directive 91/271/EEC and Implementing Decision
    2014/431/EU {footcite:p}`uwwtdImplementingDecision2014431` apply until this date.
  - Articles 23(1), 23(2), 32(7)
* - 22 June 2028 at the latest
  - List of agglomerations of 10 000 to 100 000 p.e. that need an integrated urban wastewater
    management plan.
  - Article 5(2)
* - 31 July 2028
  - The Commission notifies Member States if the conditions for deadline extensions are not
    fulfilled.
  - Articles 3(2), 6(3), 7(4)
* - 31 December 2028
  - Extended producer responsibility in place for producers of the products listed in Annex III.
  - Article 9(1)
* - 31 December 2030
  - List of areas at risk from micropollutants.
  - Article 8(2)
* - 31 December 2033
  - Integrated plans for agglomerations of 100 000 p.e. and above. First review of the risk
    identification. First interim targets for tertiary and quaternary treatment.
  - Articles 5(1), 18(3), 7, 8
* - 31 December 2035
  - Collecting systems and secondary treatment for agglomerations of 1 000 to 1 999 p.e., unless
    the deadline is extended.
  - Articles 3(2), 6(3)
* - 2036 to 2045
  - Further interim and final targets (see below). Integrated plans for the agglomerations listed
    under Article 5(2) by 31 December 2039. Less stringent treatment under Article 6(4) possible
    until 31 December 2045.
  - Articles 5(3), 6(4), 7, 8
* - At least every 6 years
  - Update the programme and submit it by 31 December of the year of the update, unless
    compliance with Articles 3 to 8 is demonstrated.
  - Article 23(3)
* - Year of a cultural heritage update
  - Submit the updated programme by 31 December of that year.
  - Article 23(1)
:::

## Interim targets for tertiary and quaternary treatment

The share of plants or agglomerations that must meet the requirements by each date:

:::{list-table} Interim and final targets under Articles 7 and 8
:header-rows: 1
:widths: 16 21 21 21 21

* - By 31 December
  - Article 7(1): plants of 150 000 p.e. and above not applying tertiary treatment on
    1 January 2025
  - Article 7(3): agglomerations of 10 000 p.e. and above discharging into sensitive areas
  - Article 8(1): plants of 150 000 p.e. and above
  - Article 8(4): agglomerations of 10 000 p.e. and above discharging into risk areas
* - 2033
  - 30 %
  - 20 %
  - 20 %
  - 10 %
* - 2036
  - 70 %
  - 40 %
  - –
  - 30 %
* - 2039
  - All plants of 150 000 p.e. and above
  - 60 %
  - 60 %
  - 60 %
* - 2045
  - –
  - All
  - All
  - All
:::

These years match the `sufficientResources2033` to `sufficientResources2045` fields in {ref}`art23-mssummary`.

## Reference dates in the draft reporting format

:::{list-table} Reference dates used in the draft tables
:header-rows: 1
:widths: 28 44 28

* - Date or period
  - Used for
  - Table and fields
* - `situationAt`
  - Date of the reported situation, for example the date the programme was approved or the date
    of the decision not to establish one.
  - {ref}`art23-mssummary`
* - 1 January 2028
  - The draft states that compliance is self-reported "as at" this date in the first programme.
  - {ref}`art23-mssummary`: `article3Compliance` to `article8Compliance`
* - 1 January 2025
  - Numbers and loads justifying deadline extensions (set by the Directive).
  - {ref}`art23-derogation`
* - "Reference year"
  - Status of plants and agglomerations. Not defined in the draft.
  - `status` in both investment tables
* - Expected date of compliance
  - Projected loads and shares.
  - `expectedLoad` in both investment tables, `expectedLoadCollected`,
    `expectedLoadIndividualSystems`
* - Expected year and dates
  - Start of works, compliance and completion.
  - `expectedYearStartWork`, `expectedDatePerformance`, `completionDate`
* - `startYear` to `endYear`
  - Period covered by a row of aggregated investments. The period is not defined in the draft.
  - {ref}`art23-otherinvestment`
:::

Which period the first programme should describe, and whether investment amounts cover the whole
period to 2045, are open questions ({ref}`art23-oi-reference-dates`,
{ref}`art23-oi-otherinvestment`).

## After the first programme

According to the draft, the {ref}`art23-derogation` table is reported in the first programme and
afterwards only if derogation requests change. The Directive requires the programme itself to be
updated at least every six years.

```{footbibliography}
```
