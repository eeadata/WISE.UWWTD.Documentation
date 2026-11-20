// Helpers for the reference data pages: links into the documentation, and the markup of the cells.

// Labels, definitions and conditions are documentation text in MyST: {ref}`label` is a link to a
// page or a section, and `text` is code. This turns them into HTML, with the links pointing to the
// documentation published next to the explorer. `base` is the path from the page to the root of the
// documentation, such as "../../".
export function markup(text, labels, base) {
  const span = document.createElement("span");
  if (!text) {
    span.textContent = "–";
    return span;
  }
  // A reference alone in brackets to a page left out of the published documentation is dropped,
  // as in the documentation itself.
  text = text.replace(/\s*\(\{ref\}`([^`<]+)`\)/g, (m, label) => (labels[label.toLowerCase()]?.internal ? "" : m));
  const pattern = /\{ref\}`([^`]+)`|`([^`]+)`/g;
  let last = 0;
  for (let m; (m = pattern.exec(text)); last = pattern.lastIndex) {
    span.append(text.slice(last, m.index));
    if (m[1] !== undefined) {
      const titled = m[1].match(/^(.*?)\s*<([^>]+)>$/);
      const label = (titled ? titled[2] : m[1]).toLowerCase();
      const target = labels[label];
      const title = titled ? titled[1] : target?.title ?? label;
      if (target && !target.internal) {
        const a = document.createElement("a");
        a.href = docsHref(base, target.page, label);
        a.textContent = title;
        span.append(a);
      } else {
        span.append(title);
      }
    } else {
      const code = document.createElement("code");
      code.textContent = m[2];
      span.append(code);
    }
  }
  span.append(text.slice(last));
  return span;
}

// The same text without markup, for searching.
export function plain(text, labels) {
  return (text ?? "")
    .replace(/\{ref\}`([^`]+)`/g, (m, ref) => {
      const titled = ref.match(/^(.*?)\s*<([^>]+)>$/);
      return titled ? titled[1] : labels[ref.toLowerCase()]?.title ?? ref;
    })
    .replace(/`([^`]+)`/g, "$1");
}

export function docsHref(base, page, anchor) {
  return `${base}${page}${anchor ? `#${anchor}` : ""}`;
}

// Where a code list is defined in the documentation.
export function codelistHref(base, codelist) {
  return docsHref(base, `rUWWTD2024/${codelist.dataflow}/Codelists.html`, codelist.anchor);
}

export const DATAFLOWS = {SpatialPoints: "Spatial points", Article23: "Article 23"};

// The Type column as written in the documentation: type, then (unit), then [multiplicity].
export function typeText(field) {
  return field.type + (field.unit ? ` (${field.unit})` : "") + (field.multiplicity ? ` [${field.multiplicity}]` : "");
}

// The fields of every table that use each code list.
export function codelistUsage(tables) {
  const usage = new Map();
  for (const t of tables)
    for (const f of t.fields) {
      if (!usage.has(f.type)) usage.set(f.type, []);
      usage.get(f.type).push({dataflow: t.dataflow, table: t.table, notation: f.notation, status: f.status});
    }
  return usage;
}

// The version of a dataflow specification, linked to its release.
export function versionNote(versions, dataflow) {
  const v = versions[dataflow];
  const span = document.createElement("span");
  if (!v) return span;
  const a = document.createElement("a");
  a.href = `https://github.com/eeadata/WISE.UWWTD.Documentation/releases/tag/${dataflow.toLowerCase()}-v${v.version}`;
  a.textContent = `${DATAFLOWS[dataflow]} specification ${v.version}`;
  span.append(a, ` (${v.status}, ${v.date})`);
  return span;
}
