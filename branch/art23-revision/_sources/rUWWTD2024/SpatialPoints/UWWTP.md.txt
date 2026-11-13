(sp-uwwtp)=
# UWWTP

**Table status:** Conditional. In the first delivery, confirm or update the prefilled treatment
plants ({ref}`first reporting <sp-first-reporting>`). Later, report only new, changed or retired
objects; unchanged rows may be included as `noChange`.
**Rows:** one row per treatment plant reported. `thematicIdIdentifier` is the key.

The table identifies and locates every urban wastewater treatment plant, including proposed ones,
with its code, name, location, condition and capacity. The dataflow starts from the objects reported under
Directive 91/271/EEC; a Member State then reports only what changes ({ref}`sp-reporting`).

A proposed plant is reported once its location is known. A plant that closes keeps its code,
with its condition changed ({ref}`sp-lifecycle`).

```{mermaid} /rUWWTD2024/SpatialPoints/mmd/SpatialPoints_UWWTP_ClassDiagram.mmd
:name: SpatialPoints_UWWTP_ClassDiagram
:caption: Spatial points - UWWTP - draft
:align: center
```

## What the fields are

The fields follow the geospatial schema proposal of 12 November 2026 and the WISE spatial data
definitions ({ref}`sp-sources`). Descriptive information on the plant is for a later Article 22
table, not this dataflow.

**Location.** `geometry`, a single point at the site of the plant.

**Identifiers.** `thematicIdIdentifier` is the treatment plant's code: the key that other reporting uses
to refer to it ({ref}`sp-references`). Its scheme, `thematicIdIdentifierScheme`, is always
`euUWWTPCode`. The three INSPIRE fields are only for Member States that already publish the treatment plant in
a national INSPIRE dataset; they let the two records be matched. Otherwise they stay empty.

**Name.** The official name and its language, with an English name if one is already in use.
For a proposed plant without an official name, give a working or descriptive name. When the
official name is assigned, report the new name as a `change`, keeping the same identifier.

**Version and history.** `beginLifespanVersion` and `endLifespanVersion` date the version reported.
`wiseEvolutionType` says what is being reported: no change, a new treatment plant, a change, a merger, a
split or a retirement. A new treatment plant that replaces earlier ones lists their codes in
`predecessorsIdentifier`. A plant that closes is a `change` of condition, not a retirement. See {ref}`sp-lifecycle`.

**Designation.** `designationPeriodBegin` and `designationPeriodEnd` give the period in which the
treatment plant is in the scope of the Directive.

**Condition and capacity.** `conditionOfFacility` says whether the plant is proposed, under
construction, in use or out of use. `uwwCapacity` is its organic design capacity in population
equivalent.

## UWWTP fields

:::{list-table} UWWTP fields
:header-rows: 1
:widths: 22 16 30 12 8 12

* - Notation
  - Label
  - Definition
  - Type
  - Status
  - Condition
* - `geometry`
  - Location
  - Location of the treatment plant, as a single point geometry (a latitude and longitude pair) in ETRS89
    (EPSG:4258) or WGS 84 (EPSG:4326), with at least four decimal places ({ref}`sp-location`).
  - point
  - Required
  - –
* - `inspireIdLocalId`
  - INSPIRE local identifier
  - Local identifier of the same object in a national INSPIRE dataset.
  - string254
  - Conditional
  - Required if an INSPIRE
    identifier has been
    assigned; give with
    `inspireIdNamespace`
* - `inspireIdNamespace`
  - INSPIRE namespace
  - Namespace of that INSPIRE dataset.
  - string254
  - Conditional
  - Required if
    `inspireIdLocalId` is
    given
* - `inspireIdVersionId`
  - INSPIRE version identifier
  - Version of the object in that INSPIRE dataset, where the source uses versions.
  - string25
  - Optional
  - –
* - `thematicIdIdentifier`
  - Code
  - Code of the treatment plant. A new plant receives a new code; an existing one keeps its code
    ({ref}`sp-reporting`). A code from the reporting under Directive 91/271/EEC that does not meet
    the WISE identifier rules is converted ({ref}`sp-code-conversion`).
  - wiseIdentifier
  - Required
  - –
* - `thematicIdIdentifierScheme`
  - Code scheme
  - Scheme of `thematicIdIdentifier`. Always `euUWWTPCode` ({ref}`sp-cl-scheme`).
  - IdentifierScheme
  - Required
  - –
* - `nameTextInternational`
  - English name
  - Existing English version of the name, if available. No translation is required.
  - string254
  - Optional
  - –
* - `nameText`
  - Name
  - Official name of the treatment plant, or a working name for a proposed plant.
  - string254
  - Required
  - –
* - `nameLanguage`
  - Name language
  - Language of `nameText`.
  - Language
  - Required
  - –
* - `beginLifespanVersion`
  - Version start
  - Date on which this version of the treatment plant was inserted or changed.
  - date
  - Optional
  - –
* - `endLifespanVersion`
  - Version end
  - Date on which the treatment plant was retired.
  - date
  - Conditional
  - Required with
    `deletion`; otherwise
    empty
* - `predecessorsIdentifier`
  - Predecessors
  - Codes of the treatment plants this one replaces, given once, in the delivery in which the change
    happens. Several codes are separated by commas.
  - wiseIdentifier [0..n]
  - Conditional
  - Required with
    `aggregation` and
    `splitting`
* - `predecessorsIdentifierScheme`
  - Predecessors scheme
  - Scheme of `predecessorsIdentifier`. Always `euUWWTPCode` ({ref}`sp-cl-scheme`).
  - IdentifierScheme
  - Conditional
  - Required if
    `predecessorsIdentifier`
    is given
* - `wiseEvolutionType`
  - Evolution type
  - What is being reported: no change, a new object, a change, a merger, a split or a
    retirement.
  - WiseEvolutionType
  - Required
  - {ref}`sp-cl-evolution`
* - `designationPeriodBegin`
  - Designation start
  - Date from which the treatment plant is in the scope of the Directive.
  - date
  - Required
  - –
* - `designationPeriodEnd`
  - Designation end
  - Date on which the treatment plant left the scope of the Directive.
  - date
  - Conditional
  - Required when the
    treatment plant leaves the
    scope of the Directive
* - `conditionOfFacility`
  - Condition
  - Physical state of the plant: proposed, under construction, in use, disused or decommissioned.
  - ConditionOfFacility
  - Required
  - {ref}`sp-cl-condition`
* - `uwwCapacity`
  - Capacity
  - Organic design capacity of the treatment plant, in population equivalent (p.e.).
  - integer
  - Required
  - –
:::
