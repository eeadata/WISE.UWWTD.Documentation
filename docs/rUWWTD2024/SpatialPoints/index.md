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

**Starting point.** The objects already reported under Directive 91/271/EEC are taken over as the
starting content of the dataflow. Their existing codes are reused where they follow the WISE
identifier rules ({ref}`sp-wise-identifier`); where a code has to be changed, the mapping between
the old and the new code is maintained centrally.

**Updates.** A Member State reports only the objects that are new, changed or retired. An object
that is not reported stays as it is: leaving it out is never a deletion. An accepted object is
never dropped, and its code is never reused for another object.

**Codes.** An object keeps its `thematicIdIdentifier` for as long as it remains the same object. A
new name, a corrected location or a change of condition does not change the code. The identifier
scheme of each table is fixed and is added centrally; it is not reported ({ref}`sp-cl-scheme`).

(sp-lifecycle)=
### What to report when something changes

| Situation | What to report | `wiseEvolutionType` | `supersedesIdentifier` |
| --- | --- | --- | --- |
| Nothing has changed | Nothing | – | – |
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
   is a `change` and does not repeat the old codes.
2. **Absorption.** XXAGG0110 absorbs XXAGG0111 and remains the same agglomeration. Report XXAGG0110
   as a `change`, with its new values, and `supersedesIdentifier` = `XXAGG0111`. It keeps its
   code: in WISE, an `aggregation` produces a new object and must not reuse a replaced code. How
   this case is published to WISE is open ({ref}`sp-oi-wise`).
3. **Closure or retirement.** A treatment plant that closes is a `change` of condition, not a
   `deletion`. `deletion` is for an object that no longer exists and is not replaced; its code is
   kept and is not reused.

`XX` stands for the country code. An object reported by mistake is corrected through the
helpdesk, not by leaving it out of a delivery ({ref}`sp-oi-reportnet`).

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
WGS-84. Either is accepted. No conversion between the two systems or
separate declaration of the system is required.

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

**Treatment plants and discharge points.**

| `conditionOfFacility` | `locationStatus` | Coordinates |
| --- | --- | --- |
| `projected`, site not selected | `notYetKnown` | empty |
| `projected`, provisional site known | `provisional` | an approximate point |
| `projected`, site selected | `confirmed` | the site |
| `underConstruction` or `functional` | `confirmed` | the site |
| `disused` or `decommissioned` | `confirmed` | the known location, kept |

When the site of a projected facility is selected, the same code is kept and the object is
reported as a `change`. A location is never filled with zero, or with the point of the
agglomeration the facility serves.

(sp-names)=
## Names

`nameText` holds the official national name, and `nameLanguage` its language, using the language
codelist selected for WISE reporting. An existing English name may be added in
`nameTextInternational`, but no translation is required. `nameText` and `nameLanguage` are
required for agglomerations, treatment plants and discharge points alike, as in the WISE spatial
data definitions. Where the earlier reporting did not give the language, the reporter adds it the
first time the object is updated.

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

| Check | Severity |
| --- | --- |
| `thematicIdIdentifier` follows the WISE identifier rules | Blocker |
| A new object does not reuse a code already used in the table, including retired codes | Blocker |
| A `change` or `deletion` refers to a code already accepted | Blocker |
| `supersedesIdentifier` is given with `aggregation` and `splitting` | Error |
| Codes in `supersedesIdentifier` exist, and an object does not supersede itself | Error |
| `latitude` is between -90 and 90 and `longitude` between -180 and 180 | Blocker |
| Coordinates are given unless `locationStatus` is `notYetKnown` | Blocker |
| `notYetKnown` and `provisional` occur only with `conditionOfFacility` = `projected` | Error |
| Coordinates are not both zero | Error |
| `inspireIdLocalId` and `inspireIdNamespace` are both given or both empty | Error |
| `nameText` and `nameLanguage` are given | Blocker |
| `waterBodyCode` refers to a water body reported under the Water Framework Directive | Warning |

Article 22 and Article 23 deliveries check that each referenced code has been accepted here, for
the reporting country and the right object type (Blocker), and warn when it has been retired.

(sp-sources)=
## Sources

* WISE evolution type vocabulary, Eionet Data Dictionary,
  [WiseEvolutionTypeValue](https://dd.eionet.europa.eu/vocabulary/wise/WiseEvolutionTypeValue),
  released 28 September 2026.
* WISE GIS Guidance,
  [v7.0.6, 20 September 2023](https://cdr.eionet.europa.eu/help/WFD/WFD_780_2022/GISGuidance/WISE_GIS_Guidance.pdf),
  section "Life-cycle management".
* WISE spatial data, MonitoringSite table, Eionet Data Dictionary dataset 3158, released
  18 May 2017
  ([latest](https://dd.eionet.europa.eu/datasets/latest/WISE_SpatialData/tables/MonitoringSite)).
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
