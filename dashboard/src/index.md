---
title: Overview
toc: false
---

```js
import {SEVERITIES, SEVERITY_COLORS, countryName, worstSeverity} from "./components/prefill.js";
```

```js
const aggs = FileAttachment("data/agglomerations.csv").csv();
const flagRows = FileAttachment("data/agglomeration-flags.csv").csv();
```

```js
const flagsByCode = d3.group(flagRows, (d) => d.thematicIdIdentifier);
const rows = aggs.map((d) => ({
  countryCode: d.countryCode,
  severity: worstSeverity(flagsByCode.get(d.thematicIdIdentifier) ?? [])
}));
```

# Spatial points prefill

:::warning Draft
The first delivery of the rUWWTD spatial points dataflow is prefilled with the objects already
reported under Directive 91/271/EEC. This dashboard shows that prefill so that reporters can look
at it before the delivery. It uses the reporting of reference year 2024, which is provisional and
under Member State review. Not an EEA publication.
:::

Each object is prefilled as `noChange`. In the delivery, the Member State confirms it, corrects it,
or retires or replaces it, and adds the objects not yet reported. The prefill cleans the names,
converts codes that break the WISE identifier rules, and corrects locations reported in degrees and
minutes as if they were decimals. Each change is flagged for the reporter to confirm.

<div class="grid grid-cols-3">
  <a class="card link" href="./agglomerations">
    <h2>Agglomerations</h2>
    <span class="big">${rows.length.toLocaleString("en-US")}</span>
    <p>Location, code, name and checks of every agglomeration to be prefilled.</p>
  </a>
  <div class="card soon">
    <h2>Treatment plants</h2>
    <p>To come.</p>
  </div>
  <div class="card soon">
    <h2>Discharge points</h2>
    <p>To come.</p>
  </div>
</div>

## Agglomerations by country

Coloured by the worst quality-check flag of each agglomeration. Select a country to open its map.

```js
const order = d3.groupSort(rows, (g) => -g.length, (d) => d.countryCode);
display(Plot.plot({
  width,
  height: 60 + 18 * order.length,
  marginLeft: 130,
  x: {label: "Agglomerations", grid: true},
  y: {label: null, domain: order, tickFormat: countryName},
  color: {domain: SEVERITIES, range: SEVERITIES.map((s) => SEVERITY_COLORS[s]), legend: true,
          tickFormat: (s) => (s === "None" ? "No flag" : s)},
  marks: [
    Plot.barX(rows, Plot.groupY({x: "count"}, {
      y: "countryCode",
      fill: "severity",
      order: SEVERITIES,
      tip: true,
      href: (d) => `./agglomerations?country=${d.countryCode}`
    })),
    Plot.ruleX([0])
  ]
}));
```

<style>
.big { font-size: 2rem; font-weight: 600; }
a.card.link { text-decoration: none; color: inherit; }
a.card.link:hover { border-color: var(--theme-foreground-focus); }
.card.soon { color: var(--theme-foreground-muted); }
</style>
