(sp-codelists)=
# Codelists

(sp-cl-scheme)=
## Identifier scheme

**Type:** `IdentifierScheme`

The scheme fields are not reported: each table has only one kind of code, so its scheme is fixed
and is added automatically, with the value below, when the WISE output is produced
({ref}`sp-oi-schemes`).

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
  - UWWTP table.
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
    `supersedesIdentifier`.
* - `change`
  - Change
  - The code is unchanged; other values are updated.
  - Includes closing and reopening a facility, and an agglomeration absorbing another.
* - `aggregation`
  - Aggregation
  - A new object formed by merging two or more objects, which it replaces.
  - New code. Needs `supersedesIdentifier`.
* - `splitting`
  - Splitting
  - A new object formed by splitting one object, which it replaces.
  - New code. Needs `supersedesIdentifier`.
* - `deletion`
  - Deletion
  - The object no longer exists and is not replaced.
  - The code is retired, not removed, and is not reused.
* - `reactivation`
  - Reactivation
  - An object retired with `deletion` is in use again, under its old code.
  - Not for an object that has been replaced.
:::

(sp-cl-location)=
## Location status

**Type:** `LocationStatus`

Used by `locationStatus` in the UWWTP table only; a discharge point always has a known location.
A UWWTD codelist.

:::{list-table} Location status values
:header-rows: 1
:widths: 24 22 34 20

* - Notation
  - Label
  - Definition
  - Notes
* - `confirmed`
  - Confirmed
  - The coordinates are those of the selected or existing site.
  - Required for every condition other than `projected`.
* - `provisional`
  - Provisional
  - The coordinates are an approximate point for a site not yet selected.
  - Only with `conditionOfFacility` = `projected`.
* - `notYetKnown`
  - Not yet known
  - No site has been selected and no coordinates are given.
  - Only with `conditionOfFacility` = `projected`.
:::

(sp-cl-condition)=
## Condition of facility

**Type:** `ConditionOfFacility`

Used by `conditionOfFacility` in the UWWTP and DischargePoint tables. It describes the physical
state of the facility only. Whether an investment has been approved belongs to investment planning,
not here.

:::{list-table} Condition of facility values
:header-rows: 1
:widths: 24 22 34 20

* - Notation
  - Label
  - Definition
  - Notes
* - `projected`
  - Projected
  - The facility is being designed; construction has not started.
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
  - Its known location is kept. To be confirmed against the INSPIRE register ({ref}`sp-oi-vocabulary`).
:::

(sp-cl-receiving)=
## Receiving type

**Type:** `ReceivingType`

Used by `receivingType` in the DischargePoint table.

:::{list-table} Receiving type values
:header-rows: 1
:widths: 24 22 34 20

* - Notation
  - Label
  - Definition
  - Notes
* - `surfaceWater`
  - Surface water
  - The discharge goes to a river, lake, transitional or coastal water.
  - –
* - `groundwater`
  - Groundwater
  - The discharge goes directly to groundwater.
  - –
* - `soil`
  - Soil
  - The discharge goes to land.
  - –
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
