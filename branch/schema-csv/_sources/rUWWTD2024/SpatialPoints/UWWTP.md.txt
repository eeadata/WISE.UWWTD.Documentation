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

:::{fieldtable} SpatialPoints/UWWTP
:::
