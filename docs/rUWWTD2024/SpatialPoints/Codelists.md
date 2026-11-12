(sp-codelists)=
# Codelists

(sp-cl-scheme)=
## Identifier scheme

**Type:** `IdentifierScheme`

Each table has only one kind of code, so its scheme is fixed. It is reported, as in WISE, in
`thematicIdIdentifierScheme` and `predecessorsIdentifierScheme`, and in the DischargePoint table
also in `relatedZoneIdentifierScheme` for the treatment plant ({ref}`sp-oi-schemes`).

:::{list-table} Identifier scheme values
:header-rows: 1
:widths: 24 22 34 20

* - Notation
  - Label
  - Definition
  - Notes
* - `euAgglomerationCode`
  - Agglomeration code
  - The code of an agglomeration.
  - Agglomeration table.
* - `euUWWTPCode`
  - Treatment plant code
  - The code of an urban wastewater treatment plant.
  - UWWTP table; `relatedZoneIdentifierScheme` in the DischargePoint table.
* - `euDischargePointCode`
  - Discharge point code
  - The code of a discharge point.
  - DischargePoint table.
:::

(sp-cl-evolution)=
## Evolution type

**Type:** `WiseEvolutionType`

Used by `wiseEvolutionType` in the Agglomeration, UWWTP and DischargePoint tables
({ref}`sp-lifecycle`). The values are taken from the
[WISE evolution type vocabulary](https://dd.eionet.europa.eu/vocabulary/wise/WiseEvolutionTypeValue)
({ref}`sp-sources`); only those needed here are used.

:::{list-table} Evolution type values
:header-rows: 1
:widths: 24 22 34 20

* - Notation
  - Label
  - Definition
  - Notes
* - `creation`
  - Creation
  - A new object that does not replace another.
  - New code.
* - `noChange`
  - No change
  - The code and location are unchanged.
  - The prefilled value in the first reporting. Missing values may be added. Never with
    replaced codes.
* - `change`
  - Change
  - The code is unchanged; other values are updated.
  - Includes closing and reopening a facility, and an agglomeration absorbing another.
* - `aggregation`
  - Aggregation
  - A new object formed by merging two or more objects, which it replaces.
  - New code. Needs the replaced codes.
* - `splitting`
  - Splitting
  - A new object formed by splitting one object, which it replaces.
  - New code. Needs the replaced codes.
* - `deletion`
  - Deletion
  - The object no longer exists and is not replaced.
  - The code is retired, not removed, and is not reused.
* - `reactivation`
  - Reactivation
  - An object retired with `deletion` is in use again, under its old code.
  - Not for an object that has been replaced.
:::

(sp-cl-zonetype)=
## Zone type

**Type:** `ZoneType`

Used by `zoneType` in the Agglomeration table. WISE takes its values from the INSPIRE
[ZoneTypeCode](https://dd.eionet.europa.eu/vocabulary/inspire/ZoneTypeCode/view) vocabulary. That
vocabulary has no value for an agglomeration under the Directive, so the value is still to be
agreed ({ref}`sp-oi-zonetype`). It is the same for every agglomeration.

(sp-cl-specialisedzonetype)=
## Specialised zone type

**Type:** `SpecialisedZoneType`

Used by `specialisedZoneType` in the Agglomeration table. WISE takes its values from the INSPIRE
[SpecialisedZoneTypeCode](https://dd.eionet.europa.eu/vocabulary/inspire/SpecialisedZoneTypeCode/view)
vocabulary, which has no values for agglomerations under the Directive. The values below are
proposed in the geospatial schema of 12 November 2026 and are to be agreed
({ref}`sp-oi-zonetype`).

:::{list-table} Specialised zone type values
:header-rows: 1
:widths: 24 22 34 20

* - Notation
  - Label
  - Definition
  - Notes
* - `agglomerationWithinUWWTDScope`
  - Within the scope
  - The agglomeration is within the scope of the Directive.
  - Proposed.
* - `agglomerationOutsideUWWTDScope`
  - Outside the scope
  - The agglomeration is outside the scope of the Directive (below 1 000 p.e.), has been
    cancelled, or has merged with another agglomeration.
  - Proposed.
* - `agglomerationFluctuatesUWWTDScope`
  - Fluctuating
  - The size of the agglomeration fluctuates around 1 000 p.e.
  - Proposed.
:::

(sp-cl-condition)=
## Condition of facility

**Type:** `ConditionOfFacility`

Used by `conditionOfFacility` in the UWWTP table. It describes the physical
state of the facility only. Whether an investment has been approved belongs to investment planning,
not here. The values follow the INSPIRE
[ConditionOfFacilityValue](https://inspire.ec.europa.eu/codelist/ConditionOfFacilityValue) codelist
and use its notations ({ref}`sp-oi-vocabulary`).

:::{list-table} Condition of facility values
:header-rows: 1
:widths: 24 22 34 20

* - Notation
  - Label
  - Definition
  - Notes
* - `projected`
  - Projected
  - The facility is planned or being designed; construction has not started.
  - The only pre-construction value.
* - `underConstruction`
  - Under construction
  - The facility is being built.
  - –
* - `functional`
  - Functional
  - The facility is in use.
  - –
* - `disused`
  - Disused
  - The facility is not in use but still exists.
  - Its known location is kept.
* - `decommissioned`
  - Decommissioned
  - The facility has been closed and taken out of service.
  - Its known location is kept.
:::

(sp-cl-language)=
## Language

**Type:** `Language`

Used by `nameLanguage` in the Agglomeration, UWWTP and DischargePoint tables, for the language of
`nameText`. The values are the three-letter codes of the shared
[ISO 639-2 vocabulary](https://dd.eionet.europa.eu/vocabulary/common/iso639-2/view) of the Eionet
Data Dictionary (`common/iso639-2`, released 10 July 2019), for example `eng`, `fra` or `deu`. It
is the vocabulary of the WISE data element
[`nameLanguage`](https://dd.eionet.europa.eu/dataelements/76740), and is not repeated here.
