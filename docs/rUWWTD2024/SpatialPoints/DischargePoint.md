(sp-dischargepoint)=
# DischargePoint

**Table status:** Conditional. In the first delivery, confirm or update the prefilled discharge
points ({ref}`first reporting <sp-first-reporting>`). Later, report only new, changed or retired
objects; unchanged rows may be included as `noChange`.
**Rows:** one row per discharge point reported. `thematicIdIdentifier` is the key.

**Use by other reporting.** Discharge points are not needed for the Article 23 national
implementation programme: its tables refer only to agglomerations and treatment plants.
This table is intended for use by Article 22 reporting, whose detailed format is still to be
defined. Completing it is not a prerequisite for submitting Article 23 reporting.

The table identifies and locates the points where urban wastewater is discharged, and links each
one to the treatment plant that discharges through it. The dataflow starts from the objects
reported under Directive 91/271/EEC; a Member State then reports only what changes
({ref}`sp-reporting`).

**Scope.** The table covers the outlets of treatment plants and direct untreated discharges from
agglomerations. Storm water overflows are not reported in this dataflow
({ref}`sp-oi-storm-overflows`).

The location of a discharge point is always required: a proposed discharge point is reported once
its location is known ({ref}`sp-location`).

```{mermaid} /rUWWTD2024/SpatialPoints/mmd/SpatialPoints_DischargePoint_ClassDiagram.mmd
:name: SpatialPoints_DischargePoint_ClassDiagram
:caption: Spatial points - DischargePoint - draft
:align: center
```

Each discharge point has a name and its language, as in the WISE spatial data definitions. Where no
name is in use, a descriptive name such as the plant or watercourse it relates to may be given.

## What the fields are

The fields follow the UML diagram of the geospatial schema of 16 November 2026 and the WISE
spatial data definitions ({ref}`sp-sources`). The receiving water and other descriptive
information are for a later Article 22 table, not this dataflow.

**Location.** `geometry`, a single point at the outlet.

**Identifiers.** `thematicIdIdentifier` is the discharge point's code: the key that other reporting uses
to refer to it ({ref}`sp-references`). Its scheme, `thematicIdIdentifierScheme`, is always
`euDischargePointCode`. The three INSPIRE fields are only for Member States that already publish the discharge point in
a national INSPIRE dataset; they let the two records be matched. Otherwise they stay empty.

**Name.** The official name and its language, with an English name if one is already in use.

**Version and history.** `beginLifespanVersion` and `endLifespanVersion` date the version reported.
`wiseEvolutionType` says what is being reported: no change, a new discharge point, a change, a merger, a
split or a retirement. A new discharge point that replaces earlier ones lists their codes in
`predecessorsIdentifier`. See {ref}`sp-lifecycle`.

**Condition.** `status` says whether the discharge point is proposed, under construction, in use
or out of use, with the same values as for treatment plants. A discharge point that closes is a
`change` of condition, not a retirement.

**Validity.** `validFrom` and `validTo` give the period in which the discharge point is in the
scope of the Directive. The names follow INSPIRE; their exact meaning is to be confirmed
({ref}`sp-oi-uml-2026-11`).

**Treatment plant.** `groupingInstallation` gives the code of the treatment plant that discharges
through the point. As in INSPIRE, the discharge point is an installation and the treatment plant
the facility that groups it ({ref}`sp-oi-dischargepoint-simplicity`).

**Link.** `link` is an optional web address with more information on the discharge point.

## DischargePoint fields

:::{list-table} DischargePoint fields
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
  - Location of the discharge point, as a single point geometry (a latitude and longitude pair) in ETRS89
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
  - string254
  - Optional
  - –
* - `thematicIdIdentifier`
  - Code
  - Code of the discharge point. A new discharge point receives a new code; an existing one keeps its
    code ({ref}`sp-reporting`).
  - wiseIdentifier
  - Required
  - –
* - `thematicIdIdentifierScheme`
  - Code scheme
  - Scheme of `thematicIdIdentifier`. Always `euDischargePointCode` ({ref}`sp-cl-scheme`).
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
  - Official name of the discharge point, or a descriptive name.
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
  - Date on which this version of the discharge point was inserted or changed.
  - date
  - Optional
  - –
* - `endLifespanVersion`
  - Version end
  - Date on which the discharge point was retired.
  - date
  - Conditional
  - Required with
    `deletion`; otherwise
    empty
* - `predecessorsIdentifier`
  - Predecessors
  - Codes of the discharge points this one replaces, given once, in the delivery in which the change
    happens. Several codes are separated by commas.
  - wiseIdentifier [0..n]
  - Conditional
  - Required with
    `aggregation` and
    `splitting`
* - `predecessorsIdentifierScheme`
  - Predecessors scheme
  - Scheme of `predecessorsIdentifier`. Always `euDischargePointCode` ({ref}`sp-cl-scheme`).
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
* - `status`
  - Condition
  - Physical state of the discharge point: proposed, under construction, in use, disused or
    decommissioned.
  - ConditionOfFacilityValue
  - Required
  - {ref}`sp-cl-condition`
* - `validFrom`
  - Valid from
  - Date from which the discharge point is in the scope of the Directive.
  - date
  - Required
  - –
* - `validTo`
  - Valid to
  - Date on which the discharge point left the scope of the Directive.
  - date
  - Conditional
  - Required when the
    discharge point leaves the
    scope of the Directive
* - `groupingInstallation`
  - Treatment plant
  - Code of the treatment plant, or collecting system without treatment, that discharges through
    this point. It must be an accepted treatment plant in the UWWTP table.
  - wiseIdentifier
  - Required
  - –
* - `link`
  - Link
  - Web address of a page with more information on the discharge point.
  - url
  - Optional
  - –
:::
