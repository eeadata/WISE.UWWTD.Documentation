// Download buttons: the rows shown, as a CSV or JSON file made in the browser.

export function csvText(rows, columns) {
  const escape = (v) => {
    const s = v == null ? "" : String(v);
    return /[",\n\r]/.test(s) ? `"${s.replaceAll('"', '""')}"` : s;
  };
  return [columns.join(","), ...rows.map((r) => columns.map((c) => escape(r[c])).join(","))].join("\n") + "\n";
}

function save(text, filename, type) {
  const url = URL.createObjectURL(new Blob([text], {type}));
  const a = Object.assign(document.createElement("a"), {href: url, download: filename});
  a.click();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}

function button(label, onclick) {
  const b = document.createElement("button");
  b.textContent = label;
  b.onclick = onclick;
  return b;
}

export function csvButton(rows, columns, filename, label = "CSV") {
  return button(`${label} (${rows.length.toLocaleString("en-US")} rows)`, () =>
    save(csvText(rows, columns), filename, "text/csv;charset=utf-8")
  );
}

export function jsonButton(value, filename, label = "JSON") {
  return button(label, () =>
    save(JSON.stringify(value, (k, v) => (typeof v === "bigint" ? Number(v) : v), 1), filename, "application/json")
  );
}
