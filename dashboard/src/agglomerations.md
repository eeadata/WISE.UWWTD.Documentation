---
title: Agglomerations
toc: false
---

```js
import {
  AGGLOMERATION_FIELDS, SEVERITIES, SEVERITY_COLORS, countryName, downloadButton, fieldValue, worstSeverity
} from "./components/prefill.js";
```

```js
const raw = FileAttachment("data/agglomerations.csv").csv();
const flagRows = FileAttachment("data/agglomeration-flags.csv").csv();
```

```js
const num = (v) => (v === "" || v == null ? null : +v);
const flagsByCode = d3.group(flagRows, (d) => d.thematicIdIdentifier);
const aggs = raw.map((d) => {
  const flags = flagsByCode.get(d.thematicIdIdentifier) ?? [];
  return {
    ...d,
    longitude: num(d.longitude),
    latitude: num(d.latitude),
    reportedLongitude: num(d.reportedLongitude),
    reportedLatitude: num(d.reportedLatitude),
    flags,
    flagCount: flags.length,
    severity: worstSeverity(flags),
    nameCleaned: d.reportedName !== "" && d.reportedName !== d.nameText,
    moved: d.reportedLatitude !== "",
    converted: d.originalCode !== ""
  };
});
const byCode = new Map(aggs.map((d) => [d.thematicIdIdentifier, d]));
const countries = [...new Set(aggs.map((d) => d.countryCode))].sort();
const checks = [...new Set(flagRows.map((d) => d.check))].sort();
```

# Agglomerations

The agglomerations that will be prefilled in the first delivery of the spatial points dataflow, from
the reporting of reference year 2024 under Directive 91/271/EEC. Every row starts as `noChange`: in
the delivery, the Member State confirms it, corrects it, or retires or replaces it. Select a point on
the map or a row in the table to see the values that will be prefilled and the checks to look at.
The fields are described in the
<a href="https://eeadata.github.io/WISE.UWWTD.Documentation/rUWWTD2024/SpatialPoints/Agglomeration.html" target="_blank">Agglomeration table specification</a> (draft).

```js
const initial = new URLSearchParams(location.search).get("country");
const country = view(Inputs.select([null, ...countries], {
  label: "Country",
  format: countryName,
  value: countries.includes(initial) ? initial : countries[0]
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
const query = view(Inputs.text({label: "Search", placeholder: "Code or name"}));
```

</div>

```js
const inCountry = country ? aggs.filter((d) => d.countryCode === country) : aggs;
const q = query.trim().toLowerCase();
const matches = (d) =>
  d.thematicIdIdentifier.toLowerCase().includes(q) ||
  d.nameText.toLowerCase().includes(q) ||
  d.reportedName.toLowerCase().includes(q) ||
  d.originalCode.toLowerCase().includes(q);
const shown = inCountry.filter(
  (d) => severity.includes(d.severity) && (!check || d.flags.some((f) => f.check === check)) && (!q || matches(d))
);
```

```js
const count = (f) => inCountry.filter(f).length.toLocaleString("en-US");
```

<div class="grid grid-cols-4">
  <div class="card"><h2>Agglomerations</h2><span class="big">${inCountry.length.toLocaleString("en-US")}</span><div class="muted">${shown.length.toLocaleString("en-US")} shown</div></div>
  <div class="card"><h2>With an error</h2><span class="big" style="color: ${SEVERITY_COLORS.Error}">${count((d) => d.severity === "Blocker" || d.severity === "Error")}</span><div class="muted">${count((d) => d.severity === "Warning")} with warnings only</div></div>
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
const picked = Mutable(null);
const pick = (code) => (picked.value = code);
```

<div class="grid grid-cols-3">
  <div class="card grid-colspan-2" style="padding: 0; overflow: hidden;">${mapDiv}</div>
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
    .bindTooltip(`${d.nameText} · ${d.thematicIdIdentifier}`)
    .on("click", () => pick(d.thematicIdIdentifier))
    .addTo(pointsLayer);
}
```

```js
// Zoom to the country, leaving out outlying points such as overseas regions.
{
  const located = inCountry.filter((d) => d.latitude != null);
  if (located.length) {
    const lat = located.map((d) => d.latitude), lon = located.map((d) => d.longitude);
    const lo = located.length > 50 ? 0.01 : 0, hi = 1 - lo;
    map.fitBounds(
      [[d3.quantile(lat, lo), d3.quantile(lon, lo)], [d3.quantile(lat, hi), d3.quantile(lon, hi)]],
      {padding: [20, 20], maxZoom: 11}
    );
  }
  pick(null);
}
```

```js
// Mark the selected agglomeration and, where its location was corrected, the reported one.
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
const detail = !sel
  ? html`<h2>No agglomeration selected</h2><p class="muted">Select a point on the map or a row in the table below.</p>`
  : html`<h2>${sel.nameText}</h2>
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
  <tbody>${AGGLOMERATION_FIELDS.map(({field, status, prefill}) => {
    const value = fieldValue(sel, field);
    const missing = !value && status === "Required";
    return html`<tr class=${missing ? "missing" : ""}>
      <td><code>${field}</code><div class="muted">${status}</div></td>
      <td>${value ? html`<span>${value}</span>` : html`<span class="muted">${missing ? "To be given" : "Empty"}</span>`}<div class="muted small">${prefill}</div></td>
    </tr>`;
  })}</tbody>
</table>
<p class="muted small">Reported scope (1991 <code>aggState</code>): ${sel.specialisedZoneType || "–"}. Not reported in the new table.</p>`;
```

## Prefilled rows

```js
const table = view(Inputs.table(shown, {
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
if (table) pick(table.thematicIdIdentifier);
```

```js
const exportColumns = ["latitude", "longitude", ...AGGLOMERATION_FIELDS.map((f) => f.field).filter((f) => f !== "geometry")];
display(downloadButton(inCountry, exportColumns, `Agglomeration_prefill_${country ?? "all"}.csv`, "Download the prefilled table"));
```

## Checks that fail

```js
const countryFlags = inCountry.flatMap((d) => d.flags);
display(countryFlags.length
  ? Plot.plot({
      marginLeft: 10,
      width,
      height: 40 + 28 * new Set(countryFlags.map((f) => f.check)).size,
      x: {label: "Agglomerations flagged", grid: true},
      y: {label: null, axis: null},
      color: {domain: SEVERITIES.slice(0, 3), range: SEVERITIES.slice(0, 3).map((s) => SEVERITY_COLORS[s]), legend: true},
      marks: [
        Plot.barX(countryFlags, Plot.groupY({x: "count"}, {y: "check", fill: "severity", sort: {y: "-x"}, tip: true})),
        Plot.text(countryFlags, Plot.groupY({x: "count", text: "first"}, {y: "check", text: "check", textAnchor: "start", dx: 6, x: 0, fill: "currentColor"}))
      ]
    })
  : html`<p>No checks fail.</p>`);
```

<p class="muted small">Source: the spatial points migration baseline, made by <code>prefill/spatial/prefill_spatial.py</code> from the Reportnet 3 EU dataset, Article 15 descriptive data, released 29 October 2026 (reference year 2024, provisional). Map tiles © OpenStreetMap contributors.</p>

<style>
.map { height: 640px; width: 100%; }
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
