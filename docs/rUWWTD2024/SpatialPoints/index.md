---
html_theme.sidebar_secondary.remove: true
---
(spatial-points)=
# Spatial points

:::{warning} Draft
A simplified UWWTD reporting proposal. It reuses WISE terms and fields where they help, but it is
not a copy of the WISE spatial data schema of the Water Framework Directive. The tables, fields
and codelists are not final. How Reportnet supports a dataflow that stays open for updates still
needs technical confirmation ({ref}`sp-oi-reportnet`).
:::

The spatial points dataflow identifies and locates the agglomerations, urban wastewater treatment
plants and discharge points that the reporting under the revised Directive refers to. Each object
is reported here once, with its code, name and location. The Article 22 and Article 23 reporting
then refer to it by its code ({ref}`sp-references`).

The dataflow stays open. A Member State adds new objects, and updates existing ones, when
something changes. It is first opened together with the Article 23 dataflow, so that the codes
exist when the first national implementation programme is reported. Only the three tables below
are reported: no documents, metadata records, document links or file uploads.

```{mermaid} /rUWWTD2024/SpatialPoints/mmd/SpatialPoints_Overview_ClassDiagram.mmd
:name: SpatialPoints_Overview_ClassDiagram
:caption: Spatial points - overview - draft
:align: center
```

::::{grid} 3
:gutter: 1 2 3 3
:::{grid-item-card} {ref}`sp-agglomeration`
Code, name and representative point of each agglomeration.
:::
:::{grid-item-card} {ref}`sp-uwwtp`
Code, name, location and condition of each treatment plant.
:::
:::{grid-item-card} {ref}`sp-dischargepoint`
Location of each discharge point, what discharges there and into what.
:::
::::

(sp-reporting)=
## Reporting

(sp-first-reporting)=
**First reporting.** The tables are prefilled with the objects already reported under Directive
91/271/EEC, every row with `wiseEvolutionType` = `noChange`. Their existing codes are reused where
they follow the WISE identifier rules ({ref}`sp-wise-identifier`); the other codes are converted,
keeping the original code ({ref}`sp-code-conversion`). The Member State:

* leaves a row as `noChange` to confirm it;
* sets a row to `change`, `deletion` or another value where something has changed
  ({ref}`sp-lifecycle`);
* adds a row with `creation` for each object not yet reported.

For the first delivery, lifecycle checks use the EEA-prepared migration baseline in place of the
accepted register. Baseline objects can therefore be confirmed with `noChange`, corrected,
retired or replaced before their first acceptance. New codes must also be distinct from baseline
codes. This exception does not make baseline codes available to Article 22 or Article 23: only
objects accepted through this dataflow can be referenced there.

The accepted delivery puts these objects into the register. Using `noChange` for objects that were
reported before and have not been replaced follows the WISE GIS Guidance ({ref}`sp-sources`).

**Later updates.** After the first reporting, a Member State reports only the objects that are new,
changed or retired. Omitting an object means no change: leaving it out is never a deletion. If the
whole table has to be delivered again, rows left as they are stay `noChange`.

**A row is the complete object.** A reported row gives all the current values of the object, not
only those that changed. It is proposed that the reporting tables are prefilled with the accepted
values, so that the reporter only edits what has changed; whether Reportnet can do this has not
been verified ({ref}`sp-oi-reportnet`).

* An optional field left empty clears the value accepted earlier.
* `supersedesIdentifier` is an exception: left empty, it means that no new replacement is
  reported. It never removes a replacement accepted earlier.

**Codes and history are kept.** An object keeps its `thematicIdIdentifier` for as long as it
remains the same object; a new name, a corrected location or a change of condition does not change
it. An accepted object is never dropped, and its code is never reused. After an object is retired,
its code and history are kept centrally, and Article 22 and Article 23 reporting that referred to
it remains valid. The identifier scheme of each table is fixed and is added centrally; it is not
reported ({ref}`sp-cl-scheme`).

(sp-code-conversion)=
### Converting existing codes into WISE identifiers

Some plant and agglomeration codes reported in earlier cycles do not meet the WISE identifier
rules. To keep the link with past reporting, the EEA converts each one into a compliant
`thematicIdIdentifier`, and keeps the link between the original code and the converted one.

Codes that already meet the rules are copied unchanged. The rest are converted by applying these
steps in order.

:::{list-table} Converting a code
:header-rows: 1
:widths: 6 50 44

* - Step
  - Rule
  - Example (before → after)
* - 1
  - Remove spaces at the start and end of the code.
  - `" FR123 "` → `FR123`
* - 2
  - Make all letters upper case.
  - `PTAGL014tp01` → `PTAGL014TP01`
* - 3
  - Replace accented letters with their plain letter (Ä → A, É → E, Ø → O, ß → SS).
  - `ATAG_8-MÖDLING` → `ATAG_8-MODLING`
* - 4
  - Replace every other character that is not allowed (anything other than A–Z, 0–9, `_` and
    `-`, such as `.` `/` `\` `,` `;` `:` and spaces inside the code) with a hyphen `-`.
  - `DEAG_MV55.20.2` → `DEAG_MV55-20-2`

    `CZ8108-644404-00575917-4/1U` → `CZ8108-644404-00575917-4-1U`
* - 5
  - Reduce repeated separators to one, keeping the first.
  - `FR1__XYZ1234--1` → `FR1_XYZ1234-1`
* - 6
  - Remove a separator straight after the country code.
  - `HU-AGGL-AIR064` → `HUAGGL-AIR064`

    `SE_AGGLO_1048` → `SEAGGLO_1048`
* - 7
  - Remove any separator at the end of the code.
  - `FR123_` → `FR123`
:::

**Why disallowed characters become a hyphen instead of being deleted.** A hyphen keeps the parts of
the code apart. If the full stop were deleted, `MV55.20.2` and `MV552.0.2` would both become
`MV552002`. Turning it into a hyphen keeps them distinct.

**What the conversion does not do.** The following cases are flagged for the Member State to
resolve, not fixed automatically:

* **Wrong or missing country prefix:** a code that does not start with the reporting country's
  code (`EL` for Greece, `UK` for the United Kingdom) is not changed.
* **Too long:** a code longer than 42 characters is not shortened.
* **Duplicates:** if two codes end up the same within a country, neither is changed. The Member
  State chooses new identifiers.

(sp-lifecycle)=
### What to report when something changes

| Situation | What to report | `wiseEvolutionType` | `supersedesIdentifier` |
| --- | --- | --- | --- |
| Nothing has changed | Nothing, or the prefilled row as it is | `noChange` | – |
| New object | The object, with a new code | `creation` | – |
| Name, location or other value changed | The object, same code | `change` | – |
| Facility closed or reopened | The object, with its new condition | `change` | – |
| Objects merged into a new one | The new object, with a new code | `aggregation` | The old codes |
| Object split into new ones | Each new object, with a new code | `splitting` | The old code |
| Object retired, not replaced | The object, same code | `deletion` | – |
| Retired object back in use | The object, same code | `reactivation` | – |

* **Retired codes stay.** An object that is merged, split or retired is not removed. Its code
  remains identifiable, so earlier reporting that refers to it can still be traced. The codes
  listed in `supersedesIdentifier` are treated as retired.
* **Replacements are reported once.** Only the new object lists the codes it replaces, in the
  delivery in which the change happens. Reporters do not fill in the reverse link; it is derived
  centrally. The history of an object is kept centrally and is not reported again.
* **Closing is not retiring.** A closed treatment plant or discharge point is reported as a
  `change` with `conditionOfFacility` set to `disused` or `decommissioned`. It keeps its code and
  can be reopened in the same way.

Three cases that are easy to get wrong:

1. **Merger.** XXAGG0101 and XXAGG0102 merge into a new agglomeration. Report XXAGG0150 with
   `aggregation` and `supersedesIdentifier` = `XXAGG0101,XXAGG0102`. Do not report the two old
   agglomerations; they are retired with XXAGG0150 as their successor. A later rename of XXAGG0150
   is a `change` with `supersedesIdentifier` left empty, which keeps the merger in its history.
2. **Absorption.** XXAGG0110 absorbs XXAGG0111 and remains the same agglomeration. Report XXAGG0110
   as a `change`, with its new values, and `supersedesIdentifier` = `XXAGG0111`. It keeps its
   code: in WISE, an `aggregation` produces a new object and must not reuse a replaced code. How
   this case is published to WISE is open ({ref}`sp-oi-wise`).
3. **Closure or retirement.** A treatment plant that closes is a `change` of condition, not a
   `deletion`. `deletion` is for an object that no longer exists and is not replaced; its code is
   kept and is not reused.

`XX` stands for the country code. An object reported by mistake is corrected through the
helpdesk, not by leaving it out of a delivery ({ref}`sp-oi-reportnet`).

(sp-lifecycle-rules)=
### Rules for changes and replacements

All the rows of a delivery are checked together against the accepted state before the delivery,
so the order of the rows does not matter. For the first delivery only, the EEA-prepared migration
baseline takes the place of that accepted state throughout these checks
({ref}`first reporting <sp-first-reporting>`). Later deliveries use the accepted register.

* **No change, change and retirement.** `noChange`, `change` and `deletion` apply only to an
  accepted object that is current, that is, not retired. A `noChange` row keeps the accepted code
  and location and lists no codes in `supersedesIdentifier`; values missing from the earlier
  reporting, such as a name language, may be added under `noChange`.
* **Reactivation.** `reactivation` applies only to an object retired with `deletion`, not to one
  that has been replaced.
* **Predecessors.** Each code in `supersedesIdentifier` must be an accepted, current object of the
  same country and the same table, other than the object itself. It must not also be reported in
  its own row of the delivery, nor be listed by another row, except by the other parts of the same
  split.
* **Mergers and splits.** An `aggregation` lists at least two codes. A `splitting` lists exactly
  one; all the new objects that list the same code are checked together as one split, and there
  must be at least two.
* **Absorption.** A `change` with `supersedesIdentifier` is accepted only in the Agglomeration
  table.
* **New codes.** `creation`, `aggregation` and `splitting` use a code never used before in the
  table, including retired codes.

(sp-references)=
## Use by Article 22 and Article 23 reporting

The Article 23 {ref}`art23-uwwtp` and {ref}`art23-agglomeration` tables refer to treatment plants
and agglomerations by `thematicIdIdentifier`, without repeating their name or location. The
Article 22 reporting is expected to refer to agglomerations, treatment plants and discharge points
in the same way; its tables are not defined yet.

* A referenced code must already have been accepted in this dataflow, for the reporting country
  and the right object type. A new object is therefore reported here first.
* Reporting already accepted remains valid when an object later changes or is retired. References
  are not rewritten to point to successors.

(sp-location)=
## Locations

**Coordinates as numbers.** Report latitude and longitude in decimal degrees, using ETRS89 or
WGS-84. Either is accepted. No conversion between the two systems or separate declaration of the
system is required.

Use existing coordinates or read them from a map that provides latitude and longitude in either
system. Enter the two numbers directly in the table; no GIS file or metadata is needed. Use a
full stop as the decimal separator, for example `52.374031` and `4.889690`, and a negative
longitude west of Greenwich. Use the precision available; six decimal places are not required
and do not imply that the location is accurate to 0.1 m.

**Agglomerations.** The point represents the agglomeration; it is not its boundary. A point
already reported is kept where it still represents the agglomeration. A new agglomeration is
located by a point within its main settlement, chosen by the reporting authority. The location of
a treatment plant is not used in its place. An unsuitable earlier point is corrected as a
`change`, keeping the code.

**Treatment plants.** The location of a plant may not yet be known while it is projected.

| `conditionOfFacility` | `locationStatus` | Coordinates |
| --- | --- | --- |
| `projected`, site not selected | `notYetKnown` | empty |
| `projected`, provisional site known | `provisional` | an approximate point |
| `projected`, site selected | `confirmed` | the site |
| `underConstruction` or `functional` | `confirmed` | the site |
| `disused` or `decommissioned` | `confirmed` | the known location, kept |

When the site of a projected plant is selected, the same code is kept and the plant is reported as
a `change`.

**Discharge points.** Latitude and longitude are always required, whatever the condition of the
discharge point. A projected discharge point is reported once its location is known; its condition
stays `projected` until it is built.

A location is never filled with zero, or with the point of the agglomeration a facility serves.

(sp-names)=
## Names

Each object has one name, with its language, and optionally an English name:

* `nameText` is the name in the national language.
* `nameLanguage` is the language of `nameText`, as a three-letter code from the
  [ISO 639-2 vocabulary](https://dd.eionet.europa.eu/vocabulary/common/iso639-2/view) of the Eionet
  Data Dictionary, for example `fra` or `deu` ({ref}`sp-cl-language`).
* `nameTextInternational` is an English name, where one is already in use. No translation is
  required.

`nameText` and `nameLanguage` are required and `nameTextInternational` is optional, for
agglomerations, treatment plants and discharge points alike. This reuses the name fields of the
WISE spatial data definitions ({ref}`sp-sources`); it is a convention of this reporting, not a
requirement of the Directive. Where the earlier reporting did not give the language, the reporter
adds it the first time the object is updated.

A projected treatment plant without an official name uses a working or descriptive name. When
the official name is assigned, update the name and keep the same identifier ({ref}`sp-uwwtp`).

## INSPIRE identifiers

The WISE code in `thematicIdIdentifier` is required for every object. `inspireIdLocalId` and
`inspireIdNamespace` are given together where an INSPIRE identifier has already been assigned to
the same object, and left empty otherwise. `inspireIdVersionId` is optional. INSPIRE identifiers
are not to be invented to complete a row. This rule concerns this reporting only; it says nothing
about a Member State's separate INSPIRE obligations.

## Data types

| Type | Meaning |
| --- | --- |
| `wiseIdentifier` | A WISE code, following the rules below |
| `string254`, `string25` | Text of at most 254 or 25 characters |
| `NumberDecimalType` | A decimal number, which may be negative |
| *codelist name* | A value from the codelist of that name ({ref}`sp-codelists`) |

`[0..n]` marks a field that accepts several values, separated by commas.

(sp-wise-identifier)=
### WISE identifiers

A `wiseIdentifier` is a string of at most 42 characters that, as defined for the WISE reporting of
the Water Framework Directive:

* starts with the ISO 3166-1 alpha-2 country code, except `EL` for Greece and `UK` for the United
  Kingdom;
* uses only upper case letters A to Z and digits 0 to 9;
* may use `_` or `-` as separators, but not immediately after the country code and not at the end;
* has no consecutive separators;
* is unique at national level, within the context to which it applies.

Valid: `FR123`, `FR1_XYZ1234_1`, `FR1-XYZ1234-1`, `FR1XYZ12341`. Not valid: `FR1__XYZ1234__1`,
`FRa123`, `FR123_`.

(sp-quality-checks)=
## Quality checks

The lifecycle checks compare the delivery with the accepted state before it. For the first
delivery only, read "accepted" in these checks as the EEA-prepared migration baseline
({ref}`sp-lifecycle-rules`); baseline codes also count as used when checking new codes.

:::{list-table}
:header-rows: 1
:widths: 80 20

* - Check
  - Severity
* - `thematicIdIdentifier` follows the WISE identifier rules
  - Blocker
* - `creation`, `aggregation` and `splitting` use a code never used in the table, including
    retired codes
  - Blocker
* - `noChange`, `change` and `deletion` refer to an accepted, current object
  - Blocker
* - A `noChange` row has no `supersedesIdentifier`
  - Error
* - A `noChange` row has the accepted location; a different location is a `change`
  - Error
* - `reactivation` refers to an object retired with `deletion` and not replaced
  - Blocker
* - `supersedesIdentifier` is given with `aggregation` and `splitting`, and otherwise only with a
    `change` in the Agglomeration table
  - Error
* - Each code in `supersedesIdentifier` is an accepted, current object of the same country and
    table, other than the object itself. It is not reported in its own row or replaced elsewhere
    in the delivery, except by other successors of the same split
  - Blocker
* - An `aggregation` lists at least two codes; a split lists one code, shared by at least two new
    objects
  - Error
* - `latitude` is between -90 and 90 and `longitude` between -180 and 180
  - Blocker
* - Agglomerations and discharge points have coordinates; treatment plants have them unless
    `locationStatus` is `notYetKnown`
  - Blocker
* - `notYetKnown` and `provisional` occur only with `conditionOfFacility` = `projected`
  - Error
* - Coordinates are not both zero
  - Error
* - `inspireIdLocalId` and `inspireIdNamespace` are both given or both empty
  - Error
* - `nameText` and `nameLanguage` are given, and `nameLanguage` is in the ISO 639-2 vocabulary
  - Blocker
* - `waterBodyCode` refers to a water body reported under the Water Framework Directive
  - Warning
:::

Article 22 and Article 23 deliveries check that each referenced code has been accepted here, for
the reporting country and the right object type (Blocker), and warn when it has been retired.

(sp-sources)=
## Sources

The WISE definitions below are reused selectively. This dataflow is a simplified UWWTD proposal,
not a copy of the WISE spatial data schema.

* WISE spatial data, Eionet Data Dictionary dataset 3158, released 18 May 2017: tables
  [MonitoringSite](https://dd.eionet.europa.eu/datasets/latest/WISE_SpatialData/tables/MonitoringSite),
  [RiverBasinDistrict](https://dd.eionet.europa.eu/datasets/latest/WISE_SpatialData/tables/RiverBasinDistrict)
  and
  [SurfaceWaterBodyLine](https://dd.eionet.europa.eu/datasets/latest/WISE_SpatialData/tables/SurfaceWaterBodyLine).
  All three use the same name fields.
* Name data elements: [`nameText`](https://dd.eionet.europa.eu/dataelements/76739), released
  3 December 2015;
  [`nameTextInternational`](https://dd.eionet.europa.eu/dataelements/76738), released
  3 December 2015; [`nameLanguage`](https://dd.eionet.europa.eu/dataelements/76740), released
  10 July 2019, whose values are the ISO 639-2 vocabulary.
* ISO 639-2 language vocabulary, Eionet Data Dictionary,
  [common/iso639-2](https://dd.eionet.europa.eu/vocabulary/common/iso639-2/view), released
  10 July 2019.
* WISE evolution type vocabulary, Eionet Data Dictionary,
  [WiseEvolutionTypeValue](https://dd.eionet.europa.eu/vocabulary/wise/WiseEvolutionTypeValue),
  released 28 September 2026.
* WISE GIS Guidance,
  [v7.0.6, 20 September 2023](https://cdr.eionet.europa.eu/help/WFD/WFD_780_2022/GISGuidance/WISE_GIS_Guidance.pdf),
  section "Life-cycle management".
* Water Framework Directive 4th-cycle data model review, a proposal,
  [commit 954c7c7](https://github.com/eeadata/WISE.WFD.Documentation/tree/954c7c742a6739c5edcd1c97131aeb24a85dd0b4/docs/DataModelReview),
  28 September 2026.

```{toctree}
:maxdepth: 1
:hidden:

Agglomeration
UWWTP
DischargePoint
Codelists
OpenIssues
```
