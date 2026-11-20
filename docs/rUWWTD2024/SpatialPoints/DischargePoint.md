(sp-dischargepoint)=
# DischargePoint

**Table status:** Conditional. In the first delivery, confirm or update the prefilled discharge
points ({ref}`first reporting <sp-first-reporting>`). Later, report only new, changed or retired
objects; unchanged rows may be included as `noChange`.
**Rows:** one row per discharge point reported. `thematicIdIdentifier` is the key.
**Prefill:** {explorer}`browse the prefilled discharge points <spatial/discharge-points.html>` on a map, with their
quality-check flags. Provisional: reference year 2024, under Member State review.

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

:::{fieldtable} SpatialPoints/DischargePoint
:::
