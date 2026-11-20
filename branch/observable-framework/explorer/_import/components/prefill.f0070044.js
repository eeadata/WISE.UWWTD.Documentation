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

// The prefilled tables: the page, the release file and the table name in the specification.
export const TABLES = {
  agglomerations: {table: "Agglomeration", label: "Agglomerations", one: "agglomeration"},
  uwwtps: {table: "UWWTP", label: "Treatment plants", one: "treatment plant"},
  "discharge-points": {table: "DischargePoint", label: "Discharge points", one: "discharge point"}
};

// Rows of an Apache Arrow table (from a Parquet file) as plain objects: dates as yyyy-mm-dd, whole
// numbers as numbers.
export function rowsOf(table) {
  const dates = new Set(table.schema.fields.filter((f) => String(f.type).startsWith("Date")).map((f) => f.name));
  return Array.from(table, (row) => {
    const r = row.toJSON();
    for (const k in r) {
      const v = r[k];
      if (typeof v === "bigint") r[k] = Number(v);
      else if (dates.has(k) && v != null) r[k] = new Date(v).toISOString().slice(0, 10);
    }
    return r;
  });
}

// The value of a field for one prefilled row, as text.
export function fieldValue(row, field) {
  if (field === "geometry") return row.latitude == null ? "" : `${row.latitude}, ${row.longitude}`;
  return row[field] ?? "";
}
