---
title: Overview
toc: false
---

```js
const ref = FileAttachment("reference/data/reference.json").json();
const release = FileAttachment("spatial/data/release.json").json();
```

# rUWWTD data explorer

Browse, search and download the reference data of the recast Urban Wastewater Treatment Directive
reporting, and look at the provisional prefill of the spatial points dataflow. The definitions are in
the ${html`<a href="../index.html">documentation</a>`}; this explorer reads the same files.

<div class="grid grid-cols-2">
  <div class="card">
    <h2>Reference data</h2>
    <p>The code lists and the fields of every reporting table, with their definitions, and the
    fields that use each code list.</p>
    <p><a href="./reference/codelists">${ref.codelists.length} code lists</a> ·
    <a href="./reference/fields">${ref.tables.length} tables</a></p>
    <p class="muted small">Drafts, as in the documentation: names, types and values may change.</p>
  </div>
  <div class="card">
    <h2>Spatial points prefill <span class="tag">provisional</span></h2>
    <p>The agglomerations, treatment plants and discharge points that will be prefilled in the first
    delivery, with their quality-check flags.</p>
    <p><a href="./spatial/agglomerations">${release.rows.agglomerations.toLocaleString("en-US")} agglomerations</a> ·
    <a href="./spatial/uwwtps">${release.rows.uwwtps.toLocaleString("en-US")} treatment plants</a> ·
    <a href="./spatial/discharge-points">${release.rows["discharge-points"].toLocaleString("en-US")} discharge points</a></p>
    <p class="muted small">Reference year ${release.reference_year}, ${release.release_status}: under
    Member State review. Release ${html`<a href="${release.url}"><code>${release.tag}</code></a>`}.</p>
  </div>
</div>

## Downloads

- **Reference data:** each code list and table can be downloaded from its page, as CSV or JSON.
  All of them, as the CSV files of the repository:
  ${html`<a href="${FileAttachment("reference/data/reference.zip").href}" download="rUWWTD-reference.zip">rUWWTD-reference.zip</a>`}.
- **Template databases:** an empty database of each dataflow, with the code lists and keys, on the
  ${html`<a href="./reference/fields#template-databases">field tables</a>`} page.
- **Spatial points prefill:** each page downloads the rows of a country as CSV. The whole tables, as
  Parquet, are attached to the release ${html`<a href="${release.url}"><code>${release.tag}</code></a>`}.

<style>
.muted { color: var(--theme-foreground-muted); }
.small { font-size: 0.85rem; }
.tag { font-size: 0.7rem; vertical-align: middle; padding: 1px 6px; border-radius: 3px;
  background: var(--theme-orange, #e8590c); color: white; }
</style>
