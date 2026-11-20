(art23-agglomeration)=
# Agglomeration

:::{warning} Draft
Draft baseline. Which agglomerations must be listed and the status codelist are still under
discussion (see the open issues linked below). In the proposed measure-first model, measures,
dates, investment costs and funding are reported in {ref}`art23-measure` and its related tables,
not here ({ref}`art23-oi-measure-model`).
:::

**Table status:** Conditional. Required for each agglomeration listed in the
`euAgglomerationCode` of a measure in {ref}`art23-measure`.
**Rows:** one row per agglomeration. `thematicIdIdentifier` is the primary key.

The table gives the state of each listed agglomeration: its status, its expected load, and the
expected shares of that load collected and addressed through individual systems. Each row refers
to an agglomeration in the {ref}`sp-agglomeration` table of the {ref}`spatial-points` dataflow,
by its `thematicIdIdentifier`. The agglomeration's name and location are reported there, not here.
An agglomeration reported for the first time is reported there first, and its code must have been
accepted before this table can refer to it ({ref}`sp-references`).

The draft lists agglomerations that are currently non-compliant, face upcoming deadlines, or are
at risk of future non-compliance, for example because of load increases, insufficient collecting
system capacity or the need to manage urban runoff. Whether compliant agglomerations with planned
renewal must also be listed is open ({ref}`art23-oi-scope`). The measures planned for collecting
systems, individual systems and integrated urban wastewater management plans are reported in
{ref}`art23-measure`, with the agglomeration's code in `euAgglomerationCode`.

```{mermaid} /rUWWTD2024/Article23/mmd/Article23_Agglomeration_ClassDiagram.mmd
:name: Article23_Agglomeration_ClassDiagram
:caption: Article 23 - Agglomeration - draft
:align: center
```

In {numref}`Article23_Agglomeration_ClassDiagram`, `[1]` marks the Required fields and `[0..1]` the
Optional ones ({ref}`art23-requirement-status`).

## Agglomeration fields

:::{fieldtable} Article23/Agglomeration
:::

## Filling in the table

* **Collecting system and individual systems in the same agglomeration.** Report them as separate
  measures in {ref}`art23-measure`, each with its own type, dates and cost, and link both to the
  agglomeration. Use `expectedLoadCollected` and `expectedLoadIndividualSystems` to show the
  expected split of the load.
* **Treatment plant measures.** List the plant in `euUWWTPCode` and the agglomerations it serves
  in `euAgglomerationCode`, so that the investment can be found for each agglomeration
  ({ref}`art23-each-agglomeration`).

## Related open issues

* {ref}`art23-oi-scope`, {ref}`art23-oi-status`, {ref}`art23-oi-listed-objects`
* {ref}`art23-oi-loads`, {ref}`art23-oi-measure-model`
