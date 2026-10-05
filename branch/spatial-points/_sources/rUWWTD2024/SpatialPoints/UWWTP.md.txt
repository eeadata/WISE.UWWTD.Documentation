(sp-uwwtp)=
# UWWTP

**Table status:** Conditional. Rows are reported only for treatment plants that are new, changed
or retired.
**Rows:** one row per treatment plant reported. `thematicIdIdentifier` is the key.

The table identifies and locates every urban wastewater treatment plant, including projected ones,
with its code, name, location and condition. The dataflow starts from the objects reported under
Directive 91/271/EEC; a Member State then reports only what changes ({ref}`sp-reporting`).

A projected plant whose site has not been chosen is reported with `locationStatus` =
`notYetKnown` and no coordinates. When its site is chosen, the same code is kept and the plant is
reported as a `change` ({ref}`sp-location`). A plant that closes keeps its code, with its
condition changed ({ref}`sp-lifecycle`).

```{mermaid} /rUWWTD2024/SpatialPoints/mmd/SpatialPoints_UWWTP_ClassDiagram.mmd
:name: SpatialPoints_UWWTP_ClassDiagram
:caption: Spatial points - UWWTP - draft
:align: center
```

## What the fields are

**Identifiers.** `thematicIdIdentifier` is the treatment plant's code: the key that other
reporting uses to refer to it ({ref}`sp-references`). `uwwCode` keeps the plant's code from the
reporting under Directive 91/271/EEC, unchanged ({ref}`sp-code-conversion`). The three INSPIRE
fields are only for Member States that already publish the treatment plant in a national INSPIRE
dataset; they let the two records be matched. Otherwise they stay empty.

**Name.** The official name and its language, with an English name if one is already in use.

**Location and state.** The position of the plant in decimal degrees, and `locationStatus`, which
says whether that position is the actual site, a provisional one, or not yet known.
`conditionOfFacility` says whether the plant is projected, under construction, in use or out of
use. `euRegistryFacilityId` links it to the same installation in the EU Registry, where it is
registered there.

**Change.** `wiseEvolutionType` says what is being reported: a new plant, a change, a merger, a
split or a retirement. A new plant that replaces earlier plants lists their codes in
`supersedesIdentifier`. A plant that closes is a `change` of condition, not a retirement. See
{ref}`sp-lifecycle`.

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
* - `thematicIdIdentifier`
  - Code
  - Code of the treatment plant. A new plant receives a new code; an existing one keeps its
    code ({ref}`sp-reporting`).
  - wiseIdentifier
  - Required
  - –
* - `uwwCode`
  - UWWTP code (1991)
  - Code of the treatment plant as reported under Directive 91/271/EEC, kept unchanged, also where
    `thematicIdIdentifier` is a converted code ({ref}`sp-code-conversion`).
  - string254
  - Optional
  - Filled by the EEA;
    empty for objects not
    reported before; not
    changed by updates
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
* - `nameText`
  - Name
  - Official name of the treatment plant.
  - string254
  - Required
  - –
* - `nameLanguage`
  - Name language
  - Language of `nameText`.
  - Language
  - Required
  - –
* - `nameTextInternational`
  - English name
  - Existing English version of the name, if available. No translation is required.
  - string254
  - Optional
  - –
* - `locationStatus`
  - Location status
  - Whether the location is the selected site, a provisional one, or
    not yet known.
  - LocationStatus
  - Required
  - {ref}`sp-cl-location`
* - `latitude`
  - Latitude
  - Latitude of the location in decimal degrees. ETRS89 or WGS-84 is
    accepted; use the precision available.
  - NumberDecimalType
  - Conditional
  - Required unless
    `locationStatus` =
    `notYetKnown`
* - `longitude`
  - Longitude
  - Longitude of the location, as for `latitude`.
  - NumberDecimalType
  - Conditional
  - Required unless
    `locationStatus` =
    `notYetKnown`
* - `conditionOfFacility`
  - Condition of facility
  - Physical state of the plant: projected, under construction, in use, or no
    longer in use.
  - ConditionOfFacility
  - Required
  - {ref}`sp-cl-condition`
* - `euRegistryFacilityId`
  - EU Registry facility identifier
  - Identifier of the same installation in the EU Registry of industrial
    facilities, where it is registered there.
  - string254
  - Optional
  - –
* - `wiseEvolutionType`
  - Evolution type
  - What is being reported: a new object, a change, a merger, a split or a retirement.
  - WiseEvolutionType
  - Required
  - {ref}`sp-cl-evolution`
* - `supersedesIdentifier`
  - Supersedes
  - Codes of the treatment plants this one replaces, given once, in the delivery in which
    the change happens. Several codes are separated by commas.
  - wiseIdentifier [0..n]
  - Conditional
  - Required with
    `aggregation` and
    `splitting`
:::
