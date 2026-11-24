---
title: Discharge points
toc: false
---

```js
import {COUNTRIES, SEVERITIES, SEVERITY_COLORS, TABLES, countryName, fieldValue, rowsOf, worstSeverity} from "../components/prefill.js";
import {csvButton} from "../components/download.js";
import {markup} from "../components/reference.js";
```

```js
const PAGE = "discharge-points";
const {table: TABLE, label: LABEL, one: ONE} = TABLES[PAGE];
const DOCS = "../../"; // the documentation, from this page
const data = FileAttachment("data/discharge-points.parquet").parquet();
const flagData = FileAttachment("data/flags.parquet").parquet();
const release = FileAttachment("data/release.json").json();
const ref = FileAttachment("../reference/data/reference.json").json();
```

```js
const raw = rowsOf(data);
const dataColumns = data.schema.fields.map((f) => f.name);
const flagRows = rowsOf(flagData).filter((d) => d.table === TABLE);
const spec = ref.tables.find((t) => t.dataflow === "SpatialPoints" && t.table === TABLE);
const HELPERS = new Set(["countryCode", "longitude", "latitude", "reportedName", "nameSteps", "reportedLongitude", "reportedLatitude", "originalCode"]);
const specFields = spec.fields.map((f) => ({...f, inRelease: f.notation === "geometry" || dataColumns.includes(f.notation)}));
const oldFields = dataColumns.filter((c) => !HELPERS.has(c) && !spec.fields.some((f) => f.notation === c));
```

```js
const flagsByCode = d3.group(flagRows, (d) => d.thematicIdIdentifier);
const rows = raw.map((d) => {
  const flags = flagsByCode.get(d.thematicIdIdentifier) ?? [];
  return {
    ...d,
    reportedName: d.reportedName ?? "",
    originalCode: d.originalCode ?? "",
    flags,
    flagCount: flags.length,
    severity: worstSeverity(flags),
    nameCleaned: !!d.reportedName && d.reportedName !== d.nameText,
    moved: d.reportedLatitude != null,
    converted: !!d.originalCode
  };
});
const byCode = new Map(rows.map((d) => [d.thematicIdIdentifier, d]));
const countries = [...new Set(rows.map((d) => d.countryCode))].sort();
const checks = [...new Set(flagRows.map((d) => d.check))].sort();
```

# Discharge points <span class="tag">provisional</span>

<div class="warning" label="Provisional data, under development">

These are the ${LABEL.toLowerCase()} that will be prefilled in the first delivery of the spatial points
dataflow, from the reporting of reference year ${release.reference_year} under Directive 91/271/EEC.
That reporting is provisional and under Member State review, and the prefill itself is still being
developed: names, locations, codes and flags may change. Not an EEA publication.

</div>

Every row starts as `noChange`: in the delivery, the Member State confirms it, corrects it, or retires
or replaces it. Select a point on the map or a row in the table to see the values that will be
prefilled and the checks to look at. The fields are defined in the
${html`<a href="${DOCS}${spec.page}">${TABLE} table specification</a>`} (draft).

```js
const query = new URLSearchParams(location.search);
const linked = byCode.get(query.get("code"));
const initialCountry = linked?.countryCode ?? query.get("country");
const country = view(Inputs.select([null, ...countries], {
  label: "Country",
  format: countryName,
  value: countries.includes(initialCountry) ? initialCountry : null
}));
```

<div class="filters">

```js
const severity = view(Inputs.checkbox(SEVERITIES, {
  label: "Worst flag",
  value: SEVERITIES,
  format: (s) => html`<span style="color:${SEVERITY_COLORS[s]}">●</span> ${s === "None" ? "No flag" : s}`
}));
```

```js
const check = view(Inputs.select([null, ...checks], {label: "Check", format: (c) => c ?? "Any check"}));
```

```js
const search = view(Inputs.text({label: "Search", placeholder: "Code or name"}));
```

</div>

```js
const inCountry = country ? rows.filter((d) => d.countryCode === country) : rows;
const q = search.trim().toLowerCase();
const matches = (d) =>
  d.thematicIdIdentifier.toLowerCase().includes(q) ||
  (d.nameText ?? "").toLowerCase().includes(q) ||
  d.reportedName.toLowerCase().includes(q) ||
  d.originalCode.toLowerCase().includes(q);
const shown = inCountry.filter(
  (d) => severity.includes(d.severity) && (!check || d.flags.some((f) => f.check === check)) && (!q || matches(d))
);
const count = (f) => inCountry.filter(f).length.toLocaleString("en-US");
```

<div class="grid grid-cols-4">
  <div class="card"><h2>${LABEL}</h2><span class="big">${inCountry.length.toLocaleString("en-US")}</span><div class="muted">${shown.length.toLocaleString("en-US")} shown</div></div>
  <div class="card"><h2>With a blocker or an error</h2><span class="big" style="color: ${SEVERITY_COLORS.Error}">${count((d) => d.severity === "Blocker" || d.severity === "Error")}</span><div class="muted">${count((d) => d.severity === "Warning")} with warnings only</div></div>
  <div class="card"><h2>Names cleaned</h2><span class="big">${count((d) => d.nameCleaned)}</span><div class="muted">reported name changed in <code>nameText</code></div></div>
  <div class="card"><h2>Codes and locations</h2><span class="big">${count((d) => d.converted)}</span><div class="muted">codes converted · ${count((d) => d.moved)} locations corrected</div></div>
</div>

```js
const mapDiv = html`<div class="map"></div>`;
const map = L.map(mapDiv, {preferCanvas: true, worldCopyJump: true}).setView([50, 10], 4);
L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
  maxZoom: 19,
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);
const pointsLayer = L.layerGroup().addTo(map);
const highlightLayer = L.layerGroup().addTo(map);
new ResizeObserver(() => map.invalidateSize()).observe(mapDiv);
invalidation.then(() => map.remove());
```

```js
const picked = Mutable(linked?.thematicIdIdentifier ?? null);
const pick = (code) => (picked.value = code);
```

<div class="grid map-row">
  <div class="card" style="padding: 0; overflow: hidden;">${mapDiv}</div>
  <div class="card detail">${detail}</div>
</div>

<div class="legend">${SEVERITIES.map((s) => html`<span><span class="dot" style="background:${SEVERITY_COLORS[s]}"></span>${s === "None" ? "No flag" : s}</span>`)}<span><span class="dot ring"></span>Selected</span><span><span class="dot ring dashed"></span>Reported location, where corrected</span></div>

```js
// Draw the points, the worst flags last so that they stay on top.
const rank = (d) => SEVERITIES.length - SEVERITIES.indexOf(d.severity);
pointsLayer.clearLayers();
for (const d of d3.sort(shown, rank)) {
  if (d.latitude == null) continue;
  L.circleMarker([d.latitude, d.longitude], {
    radius: 5,
    weight: 1,
    color: "#ffffff",
    fillColor: SEVERITY_COLORS[d.severity],
    fillOpacity: 0.9
  })
    .bindTooltip(`${d.nameText ?? ""} · ${d.thematicIdIdentifier}`)
    .on("click", () => pick(d.thematicIdIdentifier))
    .addTo(pointsLayer);
}
```

```js
// Zoom to the country, leaving out outlying points such as overseas regions; for all countries, to Europe.
{
  const located = inCountry.filter((d) => d.latitude != null);
  // Fit only once the map has its size on the page; before that, Leaflet fits into an empty box.
  const fit = () => {
    if (!mapDiv.clientWidth) return requestAnimationFrame(fit);
    map.invalidateSize();
    if (!country) {
      map.fitBounds([[34, -25], [71, 35]]); // all countries: Europe, overseas regions left out of view
    } else if (located.length) {
      const lat = located.map((d) => d.latitude), lon = located.map((d) => d.longitude);
      const lo = located.length > 50 ? 0.01 : 0, hi = 1 - lo;
      map.fitBounds(
        [[d3.quantile(lat, lo), d3.quantile(lon, lo)], [d3.quantile(lat, hi), d3.quantile(lon, hi)]],
        {padding: [20, 20], maxZoom: 11}
      );
    }
  };
  fit();
  if (!linked || (country && linked.countryCode !== country)) pick(null);
}
```

```js
// Mark the selected object and, where its location was corrected, the reported one.
highlightLayer.clearLayers();
const sel = picked ? byCode.get(picked) : null;
if (sel && sel.latitude != null) {
  const here = [sel.latitude, sel.longitude];
  L.circleMarker(here, {radius: 11, color: "#111111", weight: 2.5, fill: false, interactive: false}).addTo(highlightLayer);
  if (sel.moved) {
    const there = [sel.reportedLatitude, sel.reportedLongitude];
    L.polyline([there, here], {color: "#555555", weight: 2, dashArray: "4 4"}).addTo(highlightLayer);
    L.circleMarker(there, {radius: 7, color: "#555555", weight: 2, dashArray: "3 3", fill: false})
      .bindTooltip("Reported location")
      .addTo(highlightLayer);
  }
  if (!map.getBounds().contains(here)) map.panTo(here);
}
```

```js
function zoomTo(d) {
  const button = html`<button>Zoom to</button>`;
  button.onclick = () => map.setView([d.latitude, d.longitude], Math.max(map.getZoom(), 12));
  return button;
}
// A discharge point names its treatment plant: link to it.
function valueCell(row, field) {
  const value = fieldValue(row, field);
  if (field === "relatedZoneIdentifier" && value) return html`<a href="./uwwtps?code=${encodeURIComponent(value)}"><code>${value}</code></a>`;
  return html`<span>${value}</span>`;
}
const detail = !sel
  ? html`<h2>No ${ONE} selected</h2><p class="muted">Select a point on the map or a row in the table below.</p>`
  : html`<h2>${sel.nameText ?? sel.thematicIdIdentifier}</h2>
<div class="muted"><code>${sel.thematicIdIdentifier}</code> · ${countryName(sel.countryCode)}</div>
<div class="actions">${sel.latitude != null ? zoomTo(sel) : ""}</div>
${sel.flags.length
  ? html`<h3>Checks to look at</h3><ul class="flags">${d3.sort(sel.flags, (f) => SEVERITIES.indexOf(f.severity)).map(
      (f) => html`<li><span class="sev" style="background:${SEVERITY_COLORS[f.severity]}">${f.severity}</span> ${f.check}${f.detail ? html`<div class="muted">${f.detail}</div>` : ""}</li>`
    )}</ul>`
  : html`<p>No quality-check flags.</p>`}
${sel.nameCleaned || sel.converted || sel.moved
  ? html`<h3>Changed by the prefill</h3><ul class="changes">
      ${sel.nameCleaned ? html`<li>Name reported as <q>${sel.reportedName}</q></li>` : ""}
      ${sel.converted ? html`<li>Code reported as <code>${sel.originalCode}</code></li>` : ""}
      ${sel.moved ? html`<li>Location reported as ${sel.reportedLatitude}, ${sel.reportedLongitude}</li>` : ""}
    </ul>`
  : ""}
<h3>Prefilled values</h3>
<table class="fields">
  <thead><tr><th>Field</th><th>Value</th></tr></thead>
  <tbody>${specFields.map((f) => {
    const value = f.inRelease ? fieldValue(sel, f.notation) : "";
    const missing = f.inRelease && !value && f.status === "Required";
    return html`<tr class=${missing ? "missing" : ""}>
      <td><code>${f.notation}</code><div class="muted">${f.status}</div></td>
      <td>${!f.inRelease
        ? html`<span class="muted">Not in this release: a field of the current specification</span>`
        : value ? valueCell(sel, f.notation) : html`<span class="muted">${missing ? "To be given" : "Empty"}</span>`}
        <div class="muted small">${markup(f.label, ref.labels, DOCS)}</div></td>
    </tr>`;
  })}</tbody>
</table>
${oldFields.length
  ? html`<h3>In this release only</h3>
<p class="muted small">Fields of the baseline that are no longer in the current specification.</p>
<table class="fields"><tbody>${oldFields.map((c) => html`<tr><td><code>${c}</code></td><td>${valueCell(sel, c)}</td></tr>`)}</tbody></table>`
  : ""}`;
```

## Prefilled rows

```js
const tableView = view(Inputs.table(shown, {
  columns: ["thematicIdIdentifier", "nameText", "reportedName", "nameLanguage", "designationPeriodBegin", "severity", "flagCount"],
  header: {
    thematicIdIdentifier: "Code",
    nameText: "Name (prefilled)",
    reportedName: "Name (reported)",
    nameLanguage: "Language",
    designationPeriodBegin: "Designation start",
    severity: "Worst flag",
    flagCount: "Flags"
  },
  format: {
    severity: (s) => html`<span style="color:${SEVERITY_COLORS[s]}">●</span> ${s === "None" ? "–" : s}`,
    designationPeriodBegin: (v) => v || html`<span class="muted">missing</span>`
  },
  multiple: false,
  rows: 16,
  layout: "auto"
}));
```

```js
if (tableView) pick(tableView.thematicIdIdentifier);
```

```js
const exportColumns = dataColumns.filter((c) => !["reportedLongitude", "reportedLatitude", "nameSteps"].includes(c));
display(csvButton(inCountry, exportColumns, `${TABLE}_prefill_${release.reference_year}_${country ?? "all"}.csv`, `Download the ${country ? countryName(country) : "whole"} table as CSV`));
```

## Checks that fail

```js
const countryFlags = inCountry.flatMap((d) => d.flags);
display(countryFlags.length
  ? Plot.plot({
      marginLeft: 10,
      width,
      height: 40 + 28 * new Set(countryFlags.map((f) => f.check)).size,
      x: {label: `${LABEL} flagged`, grid: true},
      y: {label: null, axis: null},
      color: {domain: SEVERITIES.slice(0, 3), range: SEVERITIES.slice(0, 3).map((s) => SEVERITY_COLORS[s]), legend: true},
      marks: [
        Plot.barX(countryFlags, Plot.groupY({x: "count"}, {y: "check", fill: "severity", sort: {y: "-x"}, tip: true})),
        Plot.text(countryFlags, Plot.groupY({x: "count", text: "first"}, {y: "check", text: "check", textAnchor: "start", dx: 6, x: 0, fill: "currentColor"}))
      ]
    })
  : html`<p>No checks fail.</p>`);
```

<p class="muted small">Source: release ${html`<a href="${release.url}"><code>${release.tag}</code></a>`} of the
spatial points prefill, made from ${release.source.name} (reference year ${release.reference_year},
${release.release_status}). It follows ${release.specification_version
  ? html`specification <code>${release.specification_version}</code>`
  : "a specification from before the versions were introduced"}; the current one is
<code>spatialpoints-v${ref.versions.SpatialPoints.version}</code>. Fields added since the release are
marked as not in this release. The whole tables can be downloaded from the release, as
Parquet. Map tiles © OpenStreetMap contributors.</p>

<style>
.tag { font-size: 0.8rem; vertical-align: middle; padding: 1px 6px; border-radius: 3px;
  background: var(--theme-orange, #e8590c); color: white; }
.map { height: 640px; width: 100%; }
.map-row { grid-template-columns: 1fr; }
@media (min-width: 640px) { .map-row { grid-template-columns: 3fr 2fr; } }
.filters { display: flex; flex-wrap: wrap; gap: 0 2rem; align-items: flex-start; }
.big { font-size: 2rem; font-weight: 600; }
.muted { color: var(--theme-foreground-muted); }
.small { font-size: 0.8rem; }
.detail { max-height: 640px; overflow-y: auto; }
.detail h3 { margin-top: 1rem; }
.detail .actions { margin: 0.5rem 0; }
.flags, .changes { padding-left: 1rem; }
.flags li { margin-bottom: 0.4rem; }
.sev { color: white; border-radius: 3px; padding: 0 4px; font-size: 0.75rem; }
table.fields { font-size: 0.85rem; }
table.fields td { vertical-align: top; }
table.fields tr.missing td:first-child { box-shadow: inset 3px 0 0 var(--theme-red); }
.legend { display: flex; flex-wrap: wrap; gap: 1rem; font-size: 0.85rem; margin-bottom: 1.5rem; }
.legend .dot { display: inline-block; width: 10px; height: 10px; border-radius: 50%; margin-right: 4px; vertical-align: -1px; }
.legend .ring { background: none; border: 2px solid currentColor; width: 12px; height: 12px; }
.legend .dashed { border-style: dashed; }
</style>
