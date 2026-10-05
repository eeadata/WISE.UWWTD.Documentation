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

**Identifiers.** `thematicIdIdentifier` is the agglomeration's code: the key that other reporting
uses to refer to it ({ref}`sp-references`). The three INSPIRE fields are only for Member States
that already publish the agglomeration in a national INSPIRE dataset; they let the two records be
matched. Otherwise they stay empty.

**Name.** The official name and its language, with an English name if one is already in use.

**Location.** A representative point in decimal degrees, within the main settlement.

**Change.** `wiseEvolutionType` says what is being reported: no change, a new agglomeration, a
change, a merger, a split or a retirement. A new agglomeration that results from a merger or split
lists the codes it replaces in `supersedesIdentifier`; so does an agglomeration that absorbs
another and keeps its code. See {ref}`sp-lifecycle`.

## Agglomeration fields

:::{list-table} Agglomeration fields
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
  - Code of the agglomeration. A new agglomeration receives a new code; an existing one keeps
    its code ({ref}`sp-reporting`).
    A code from the reporting under Directive 91/271/EEC that does not meet the WISE
    identifier rules is converted ({ref}`sp-code-conversion`).
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
  - Official name of the agglomeration.
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
  - Latitude of the representative point in decimal degrees. ETRS89 or
    WGS-84 is accepted; use the precision available.
  - NumberDecimalType
  - Required
  - –
* - `longitude`
  - Longitude
  - Longitude of the representative point, as for `latitude`.
  - NumberDecimalType
  - Required
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
  - Codes of the agglomerations this one replaces, given once, in the delivery in which
    the change happens. Several codes are separated by commas.
  - wiseIdentifier [0..n]
  - Conditional
  - Required with
    `aggregation` and
    `splitting`, and with
    `change` for an
    absorption
:::
