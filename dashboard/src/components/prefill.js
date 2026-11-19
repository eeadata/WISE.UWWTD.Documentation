// Shared helpers for the spatial points prefill pages.

export const COUNTRIES = {
  AT: "Austria", BE: "Belgium", BG: "Bulgaria", CH: "Switzerland", CY: "Cyprus", CZ: "Czechia",
  DE: "Germany", DK: "Denmark", EE: "Estonia", EL: "Greece", ES: "Spain", FI: "Finland",
  FR: "France", HR: "Croatia", HU: "Hungary", IE: "Ireland", IS: "Iceland", IT: "Italy",
  LI: "Liechtenstein", LT: "Lithuania", LU: "Luxembourg", LV: "Latvia", MT: "Malta",
  NL: "Netherlands", NO: "Norway", PL: "Poland", PT: "Portugal", RO: "Romania", SE: "Sweden",
  SI: "Slovenia", SK: "Slovakia"
};

export const countryName = (code) => (code ? `${COUNTRIES[code] ?? code} (${code})` : "All countries");

// Severities in order, worst first, with the colour used on the map and in charts.
export const SEVERITIES = ["Blocker", "Error", "Warning", "None"];
export const SEVERITY_COLORS = {
  Blocker: "#c92a2a",
  Error: "#e8590c",
  Warning: "#e0a800",
  None: "#2b7bb9"
};

export function worstSeverity(flags) {
  for (const s of SEVERITIES) if (flags.some((f) => f.severity === s)) return s;
  return "None";
}

// The fields of the Agglomeration table, in the order of the specification, with what the prefill
// puts in each (docs/rUWWTD2024/SpatialPoints/Agglomeration.md, prefill/spatial/README.md).
export const AGGLOMERATION_FIELDS = [
  {field: "geometry", status: "Required", prefill: "Reported latitude and longitude (ETRS89); corrected where degrees and minutes were reported as decimals"},
  {field: "inspireIdLocalId", status: "Required", prefill: "Empty: not in the earlier reporting. To be given by the Member State"},
  {field: "inspireIdNamespace", status: "Required", prefill: "Empty: not in the earlier reporting. To be given by the Member State"},
  {field: "inspireIdVersionId", status: "Optional", prefill: "Empty"},
  {field: "thematicIdIdentifier", status: "Required", prefill: "The reported code; converted where it breaks the WISE identifier rules"},
  {field: "thematicIdIdentifierScheme", status: "Required", prefill: "euAgglomerationCode"},
  {field: "nameTextInternational", status: "Optional", prefill: "The cleaned name in Latin letters without accents (proposed)"},
  {field: "nameText", status: "Required", prefill: "The reported name, cleaned: the official name as written"},
  {field: "nameLanguage", status: "Required", prefill: "The country's name language, or a region's"},
  {field: "beginLifespanVersion", status: "Optional", prefill: "The baseline date, the same for every row"},
  {field: "endLifespanVersion", status: "Conditional", prefill: "Empty"},
  {field: "predecessorsIdentifier", status: "Conditional", prefill: "Empty"},
  {field: "predecessorsIdentifierScheme", status: "Conditional", prefill: "Empty"},
  {field: "wiseEvolutionType", status: "Required", prefill: "noChange"},
  {field: "designationPeriodBegin", status: "Required", prefill: "aggBeginLife, where reported (proposed)"},
  {field: "designationPeriodEnd", status: "Conditional", prefill: "aggEndLife, where reported (proposed)"},
  {field: "zoneType", status: "Required", prefill: "Empty: the value is still to be agreed"},
  {field: "link", status: "Optional", prefill: "Empty: new field"}
];

// The value of a field for one prefilled row, as text.
export function fieldValue(row, field) {
  if (field === "geometry") return row.latitude == null ? "" : `${row.latitude}, ${row.longitude}`;
  return row[field] ?? "";
}

// A button that downloads rows as a CSV file.
export function downloadButton(rows, columns, filename, label = "Download CSV") {
  const escape = (v) => {
    const s = v == null ? "" : String(v);
    return /[",\n\r]/.test(s) ? `"${s.replaceAll('"', '""')}"` : s;
  };
  const button = document.createElement("button");
  button.textContent = `${label} (${rows.length.toLocaleString("en-US")} rows)`;
  button.onclick = () => {
    const text = [columns.join(","), ...rows.map((r) => columns.map((c) => escape(r[c])).join(","))].join("\n");
    const url = URL.createObjectURL(new Blob([text], {type: "text/csv;charset=utf-8"}));
    const a = Object.assign(document.createElement("a"), {href: url, download: filename});
    a.click();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
  };
  return button;
}
