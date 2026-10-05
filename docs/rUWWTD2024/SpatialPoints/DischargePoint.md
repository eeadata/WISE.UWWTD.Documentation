(sp-dischargepoint)=
# DischargePoint

**Table status:** Conditional. In the first delivery, confirm or update the prefilled discharge points
({ref}`first reporting <sp-first-reporting>`). Later, report only new, changed or retired objects; unchanged rows
may be included as `noChange`.
**Rows:** one row per discharge point reported. `thematicIdIdentifier` is the key.

**Use by other reporting.** Discharge points are not needed for the Article 23 national
implementation programme: its tables refer only to agglomerations and treatment plants.
This table is intended for use by Article 22 reporting, whose detailed format is still to be
defined. Completing it is not a prerequisite for submitting Article 23 reporting.

The table identifies and locates the points where urban wastewater is discharged, and records the receiving
water or land. No treatment plant or agglomeration link is requested. The dataflow starts from the
objects reported under Directive 91/271/EEC; a Member State then reports only what changes
({ref}`sp-reporting`).

**Scope.** The table covers the outlets of treatment plants and direct untreated discharges from
agglomerations. Storm water overflows are not reported in this dataflow
({ref}`sp-oi-storm-overflows`).

The location of a discharge point is always required, whatever its condition: a projected
discharge point is reported once its location is known ({ref}`sp-location`).

```{mermaid} /rUWWTD2024/SpatialPoints/mmd/SpatialPoints_DischargePoint_ClassDiagram.mmd
:name: SpatialPoints_DischargePoint_ClassDiagram
:caption: Spatial points - DischargePoint - draft
:align: center
```

The scheme of `waterBodyCode` follows from `receivingType`: `euSurfaceWaterBodyCode` for surface
water and `euGroundWaterBodyCode` for groundwater.

Each discharge point has a name and its language, as in the WISE spatial data definitions. Where no
name is in use, a descriptive name such as the plant or watercourse it relates to may be given.

## What the fields are

**Identifiers.** `thematicIdIdentifier` is the discharge point's code: the key that other
reporting uses to refer to it ({ref}`sp-references`). The three INSPIRE fields are only for Member
States that already publish the discharge point in a national INSPIRE dataset; they let the two
records be matched. Otherwise they stay empty.

**Name.** The official name and its language, with an English name if one is already in use.

**Location and receiving water.** The position of the outlet in decimal degrees, always required,
and `conditionOfFacility` as for treatment plants. `receivingType` says whether the wastewater goes
to surface water, groundwater or soil, and `waterBodyCode` gives the receiving water body reported
under the Water Framework Directive.

**Change.** `wiseEvolutionType` says what is being reported: no change, a new discharge point, a
change, a merger, a split or a retirement. A new discharge point that replaces earlier ones lists
their codes in `supersedesIdentifier`. A discharge point that closes is a `change` of condition,
not a retirement. See {ref}`sp-lifecycle`.

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
* - `thematicIdIdentifier`
  - Code
  - Code of the discharge point. A new discharge point receives a new code; an existing one
    keeps its code ({ref}`sp-reporting`).
  - wiseIdentifier
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
* - `nameText`
  - Name
  - Name of the discharge point.
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
* - `latitude`
  - Latitude
  - Latitude of the location in decimal degrees. ETRS89 or WGS-84 is
    accepted; use the precision available.
  - NumberDecimalType
  - Required
  - –
* - `longitude`
  - Longitude
  - Longitude of the location, as for `latitude`.
  - NumberDecimalType
  - Required
  - –
* - `conditionOfFacility`
  - Condition of facility
  - Physical state of the discharge point. Same codelist as for treatment plants.
  - ConditionOfFacility
  - Required
  - {ref}`sp-cl-condition`
* - `receivingType`
  - Receiving type
  - What the wastewater is discharged into.
  - ReceivingType
  - Required
  - {ref}`sp-cl-receiving`
* - `waterBodyCode`
  - Water body
  - Code of the WFD surface water body or groundwater body receiving the
    discharge.
  - wiseIdentifier
  - Optional
  - –
* - `wiseEvolutionType`
  - Evolution type
  - What is being reported: no change, a new object, a change, a merger, a split or a
    retirement.
  - WiseEvolutionType
  - Required
  - {ref}`sp-cl-evolution`
* - `supersedesIdentifier`
  - Supersedes
  - Codes of the discharge points this one replaces, given once, in the delivery in which
    the change happens. Several codes are separated by commas.
  - wiseIdentifier [0..n]
  - Conditional
  - Required with
    `aggregation` and
    `splitting`
:::

`waterBodyCode` refers to the water bodies reported under the Water Framework Directive.
