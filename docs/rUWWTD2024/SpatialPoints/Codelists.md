(sp-codelists)=
# Codelists

(sp-cl-scheme)=
## Identifier scheme

**Type:** `IdentifierScheme`

Each table has only one kind of code, so its scheme is fixed. It is reported, as in WISE, in
`thematicIdIdentifierScheme` and `predecessorsIdentifierScheme` ({ref}`sp-oi-schemes`). The
treatment plant code in `groupingInstallation` of the DischargePoint table has no scheme field; it
is always a `euUWWTPCode`.

:::{codelist} IdentifierScheme
:::

(sp-cl-evolution)=
## Evolution type

**Type:** `WiseEvolutionType`

Used by `wiseEvolutionType` in the Agglomeration, UWWTP and DischargePoint tables
({ref}`sp-lifecycle`). The values are taken from the
[WISE evolution type vocabulary](https://dd.eionet.europa.eu/vocabulary/wise/WiseEvolutionTypeValue)
({ref}`sp-sources`); only those needed here are used.

:::{codelist} WiseEvolutionType
:::

(sp-cl-zonetype)=
## Zone type

**Type:** `ZoneType`

Used by `zoneType` in the Agglomeration table. WISE takes its values from the INSPIRE
[ZoneTypeCode](https://dd.eionet.europa.eu/vocabulary/inspire/ZoneTypeCode/view) vocabulary. That
vocabulary has no value for an agglomeration under the Directive. The UML diagram of 16 November
2026 proposes `uwwtdAgglomeration`; the value is still to be agreed ({ref}`sp-oi-zonetype`). It is
the same for every agglomeration.

(sp-cl-condition)=
## Condition of facility

**Type:** `ConditionOfFacilityValue`

Used by `status` in the UWWTP and DischargePoint tables. It describes the physical
state of the facility only. Whether an investment has been approved belongs to investment planning,
not here. The values follow the INSPIRE
[ConditionOfFacilityValue](https://inspire.ec.europa.eu/codelist/ConditionOfFacilityValue) codelist
and use its notations ({ref}`sp-oi-vocabulary`).

:::{codelist} ConditionOfFacilityValue
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
