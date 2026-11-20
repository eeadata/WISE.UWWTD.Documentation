---
title: Field tables
toc: false
---

```js
import {DATAFLOWS, docsHref, markup, plain, typeText} from "../components/reference.js";
import {csvButton, jsonButton} from "../components/download.js";
```

```js
const ref = FileAttachment("data/reference.json").json();
const DOCS = "../../"; // the documentation, from this page
```

```js
const labels = ref.labels;
const codelists = new Set(ref.codelists.map((c) => c.type));
const types = new Map(ref.types.map((t) => [t.type, t]));
const key = (t) => `${t.dataflow}/${t.table}`;
const byKey = new Map(ref.tables.map((t) => [key(t), t]));
const COLUMNS = ["notation", "label", "definition", "type", "multiplicity", "unit", "status", "condition", "group"];

// The Type column links a code list to its page, and shows the definition of a simple type.
function typeCell(f) {
  if (codelists.has(f.type)) return html`<a href="./codelists?type=${f.type}"><code>${typeText(f)}</code></a>`;
  const t = types.get(f.type);
  return html`<code title="${t ? t.definition : ""}">${typeText(f)}</code>`;
}
```

# Field tables

The fields of every table of the rUWWTD dataflows, as in the documentation, which reads the same
files. Select a table, or search the fields of all of them. Drafts: names, types and statuses may
change.

```js
const allFields = ref.tables.flatMap((t) =>
  t.fields.map((f) => ({
    table: key(t),
    notation: f.notation,
    label: f.label,
    type: f.type,
    status: f.status,
    definition: plain(f.definition, labels)
  }))
);
const found = view(Inputs.search(allFields, {placeholder: "Search all fields: a name, a type or a word", width: 480}));
```

```js
display(
  found.length < allFields.length
    ? Inputs.table(found, {
        columns: ["table", "notation", "label", "type", "status", "definition"],
        header: {table: "Table", notation: "Field", label: "Label", type: "Type", status: "Status", definition: "Definition"},
        format: {
          table: (t) => html`<a href="?table=${t}">${t}</a>`,
          notation: (n) => html`<code>${n}</code>`,
          type: (t) => (codelists.has(t) ? html`<a href="./codelists?type=${t}"><code>${t}</code></a>` : html`<code>${t}</code>`)
        },
        rows: 8,
        layout: "auto"
      })
    : html`<p class="muted small">${allFields.length} fields in ${ref.tables.length} tables.</p>`
);
```

```js
const initial = byKey.get(new URLSearchParams(location.search).get("table")) ?? ref.tables[0];
const choice = view(Inputs.select(ref.tables, {
  label: "Table",
  format: (t) => `${DATAFLOWS[t.dataflow]}${t.dataset ? ` · ${t.dataset}` : ""} · ${t.table}`,
  value: initial
}));
```

```js
display(html`<div class="card">
  <h2>${choice.table}</h2>
  <p>${DATAFLOWS[choice.dataflow]} dataflow${choice.dataset ? html`, ${choice.dataset}` : ""}.
  ${choice.fields.length} fields. ${choice.primaryKey.length
    ? html`Key: ${choice.primaryKey.map((k, i) => html`${i ? ", " : ""}<code>${k}</code>`)}.`
    : html`<span class="muted">No key stated.</span>`}
  <a href="${docsHref(DOCS, choice.page, choice.anchor)}">Definition in the documentation</a>.</p>
</div>`);
```

```js
const groups = new Map(choice.groups.map((g) => [g.group, g.caption]));
const shown = choice.fields.map((f) => ({...f, part: groups.get(f.group) ?? ""}));
display(Inputs.table(shown, {
  columns: ["notation", "label", "definition", "type", "status", "condition", ...(choice.groups.length > 1 ? ["part"] : [])],
  header: {notation: "Field", label: "Label", definition: "Definition", type: "Type", status: "Status", condition: "Condition", part: "Part"},
  format: {
    notation: (n) => html`<code id="${n}">${n}</code>`,
    definition: (d) => markup(d, labels, DOCS),
    condition: (c) => markup(c, labels, DOCS),
    type: (t, i) => typeCell(shown[i])
  },
  rows: 40,
  layout: "auto"
}));
```

<div class="downloads">

```js
display(html`<span>Download <code>${choice.table}</code>:</span>`);
display(csvButton(choice.fields, COLUMNS, `${choice.dataflow}_${choice.table}.csv`));
display(jsonButton({dataflow: choice.dataflow, dataset: choice.dataset, table: choice.table, primaryKey: choice.primaryKey, fields: choice.fields}, `${choice.dataflow}_${choice.table}.json`));
display(html`<a href="${FileAttachment("data/reference.zip").href}" download="rUWWTD-reference.zip">All code lists and field tables (zip)</a>`);
```

</div>

<p class="muted small">The files are the CSV sources of the field tables in the repository
(<code>reference/schema</code>); its README explains the columns. Definitions and conditions may contain
documentation markup, such as <code>{ref}`label`</code>, which is shown here as a link.</p>

<style>
.muted { color: var(--theme-foreground-muted); }
.small { font-size: 0.85rem; }
.downloads { display: flex; flex-wrap: wrap; gap: 0.75rem; align-items: center; margin: 1rem 0; }
</style>
