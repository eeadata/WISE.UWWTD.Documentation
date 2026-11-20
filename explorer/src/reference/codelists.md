---
title: Code lists
toc: false
---

```js
import {DATAFLOWS, codelistHref, codelistUsage, markup, plain, versionNote} from "../components/reference.js";
import {csvButton, jsonButton} from "../components/download.js";
```

```js
const ref = FileAttachment("data/reference.json").json();
const DOCS = "../../"; // the documentation, from this page
```

```js
const byType = new Map(ref.codelists.map((c) => [c.type, c]));
const usage = codelistUsage(ref.tables);
const labels = ref.labels;
```

# Code lists

The code lists of the rUWWTD dataflows, as in the documentation, which reads the same files. Select
a code list, or search the values of all of them. Drafts: values may change.

```js
const allValues = ref.codelists.flatMap((c) =>
  c.rows.map((r) => ({
    codelist: c.type,
    dataflow: DATAFLOWS[c.dataflow],
    value: r[c.codeColumns[0]] ?? "",
    label: plain(r.label ?? r[c.columns[1]], labels),
    definition: plain(r.definition ?? "", labels)
  }))
);
const found = view(Inputs.search(allValues, {placeholder: "Search all code lists: a code, a label or a word", width: 480}));
```

```js
const query = new URLSearchParams(location.search);
const initial = byType.has(query.get("type")) ? query.get("type") : ref.codelists[0].type;
display(
  found.length < allValues.length
    ? Inputs.table(found, {
        columns: ["codelist", "value", "label", "definition"],
        header: {codelist: "Code list", value: "Value", label: "Label", definition: "Definition"},
        format: {codelist: (t) => html`<a href="?type=${t}">${t}</a>`, value: (v) => html`<code>${v}</code>`},
        rows: 8,
        layout: "auto"
      })
    : html`<p class="muted small">${allValues.length.toLocaleString("en-US")} values in ${ref.codelists.length} code lists.</p>`
);
```

```js
const choice = view(Inputs.select(ref.codelists, {
  label: "Code list",
  format: (c) => `${DATAFLOWS[c.dataflow]} · ${c.type}`,
  value: byType.get(initial)
}));
```

```js
const used = usage.get(choice.type) ?? [];
display(html`<div class="card">
  <h2><code>${choice.type}</code></h2>
  <p>${choice.caption}. ${DATAFLOWS[choice.dataflow]} dataflow.
  <a href="${codelistHref(DOCS, choice)}">Definition in the documentation</a>.</p>
  <p class="muted small">Version: ${versionNote(ref.versions, choice.dataflow)}</p>
  <p>${used.length
    ? html`Used by ${used.map((u, i) => html`${i ? ", " : ""}<a href="./fields?table=${u.dataflow}/${u.table}#${u.notation}"><code>${u.table}.${u.notation}</code></a>`)}.`
    : html`<span class="muted">Not the type of any field: it describes the values of another code list.</span>`}</p>
</div>`);
```

```js
const columns = choice.columns;
display(Inputs.table(choice.rows, {
  columns,
  header: Object.fromEntries(columns.map((c, i) => [c, choice.headers[i] ?? c])),
  format: Object.fromEntries(columns.map((c) => [c, choice.codeColumns.includes(c) ? (v) => (v ? html`<code>${v}</code>` : "–") : (v) => markup(v, labels, DOCS)])),
  rows: 30,
  layout: "auto"
}));
```

<div class="downloads">

```js
display(html`<span>Download <code>${choice.type}</code>:</span>`);
display(csvButton(choice.rows, columns, `${choice.type}.csv`));
display(jsonButton({type: choice.type, dataflow: choice.dataflow, caption: choice.caption, values: choice.rows}, `${choice.type}.json`));
display(html`<a href="${FileAttachment("data/reference.zip").href}" download="rUWWTD-reference.zip">All code lists and field tables (zip)</a>`);
```

</div>

<p class="muted small">The files are the CSV sources of the code lists in the repository. Labels,
definitions and notes may contain documentation markup, such as <code>{ref}`label`</code>, which is
shown here as a link.</p>

<style>
.muted { color: var(--theme-foreground-muted); }
.small { font-size: 0.85rem; }
.downloads { display: flex; flex-wrap: wrap; gap: 0.75rem; align-items: center; margin: 1rem 0; }
</style>
