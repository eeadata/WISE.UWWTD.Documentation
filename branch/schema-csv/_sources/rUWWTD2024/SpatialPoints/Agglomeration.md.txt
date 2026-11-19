(sp-agglomeration)=
# Agglomeration

**Table status:** Conditional. In the first delivery, confirm or update the prefilled
agglomerations ({ref}`first reporting <sp-first-reporting>`). Later, report only new, changed or
retired objects; unchanged rows may be included as `noChange`.
**Rows:** one row per agglomeration reported. `thematicIdIdentifier` is the key.

The table identifies and locates every agglomeration with its code, name and a representative
point. The dataflow starts from the objects reported under Directive 91/271/EEC; a Member State
then reports only what changes ({ref}`sp-reporting`).

The location is a representative point, not the boundary of the agglomeration
({ref}`sp-location`):

* A point already reported is kept where the Member State confirms that it still represents the
  agglomeration.
* For a new agglomeration, the point lies within its main settlement and is chosen by the
  reporting authority. A geometric centroid is not required, as it may fall outside the settled
  area.
* The location of a treatment plant is not used as the location of the agglomeration.
* An unsuitable point from earlier reporting is corrected as a `change`, keeping the agglomeration
  code.

```{mermaid} /rUWWTD2024/SpatialPoints/mmd/SpatialPoints_Agglomeration_ClassDiagram.mmd
:name: SpatialPoints_Agglomeration_ClassDiagram
:caption: Spatial points - Agglomeration - draft
:align: center
```

## What the fields are

The fields follow the WISE spatial data tables for management zones, such as `SubUnit`
({ref}`sp-sources`), as proposed in the UML diagram of the geospatial schema of 16 November 2026.

**Location.** `geometry`, a single point that represents the agglomeration, within its main
settlement.

**Identifiers.** `thematicIdIdentifier` is the agglomeration's code: the key that other reporting
uses to refer to it ({ref}`sp-references`). Its scheme, `thematicIdIdentifierScheme`, is always
`euAgglomerationCode`. `inspireIdLocalId` and `inspireIdNamespace` give the INSPIRE identifier of
the agglomeration and are required ({ref}`sp-oi-uml-2026-11`); `inspireIdVersionId` is optional.

**Name.** The official name and its language, with an English name if one is already in use.

**Version and history.** `beginLifespanVersion` and `endLifespanVersion` date the version reported.
`wiseEvolutionType` says what is being reported: no change, a new agglomeration, a change, a
merger, a split or a retirement. A new agglomeration that results from a merger or split lists the
codes it replaces in `predecessorsIdentifier`; so does an agglomeration that absorbs another and
keeps its code. See {ref}`sp-lifecycle`.

**Designation and zone type.** `designationPeriodBegin` and `designationPeriodEnd` give the period
in which the agglomeration is in the scope of the Directive. `zoneType` classifies it as a
management zone, as in WISE; its value is still to be agreed ({ref}`sp-oi-zonetype`).

**Link.** `link` is an optional web address with more information on the agglomeration
({ref}`sp-oi-uml-2026-11`).

## Agglomeration fields

:::{fieldtable} SpatialPoints/Agglomeration
:::
