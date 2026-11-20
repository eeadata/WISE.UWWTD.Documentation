// Observable Framework configuration: https://observablehq.com/framework/config
//
// The explorer is published with the documentation, under explorer/ (see README.md). Links to the
// documentation are relative, so that they also work in the preview of a branch.

// The published documentation
const DOCS = "https://eeadata.github.io/WISE.UWWTD.Documentation/";

export default {
  title: "rUWWTD data explorer",
  root: "src",
  pages: [
    {
      name: "Reference data",
      open: true,
      pages: [
        {name: "Code lists", path: "/reference/codelists"},
        {name: "Field tables", path: "/reference/fields"}
      ]
    },
    {
      name: "Spatial points prefill (provisional)",
      open: true,
      pages: [
        {name: "Agglomerations", path: "/spatial/agglomerations"},
        {name: "Treatment plants", path: "/spatial/uwwtps"},
        {name: "Discharge points", path: "/spatial/discharge-points"}
      ]
    }
  ],
  theme: ["air", "near-midnight"],
  head: `<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><circle cx=%2250%22 cy=%2250%22 r=%2240%22 fill=%22%232b7bb9%22/></svg>">
<style>
.under-development { padding: 0.5rem 0.75rem; border-radius: 4px; font-size: 0.9rem;
  background: color-mix(in srgb, var(--theme-orange, #e8590c) 15%, var(--theme-background));
  border-left: 4px solid var(--theme-orange, #e8590c); }
/* The header holds two lines: the link back to the documentation, and the notice */
:root { --observablehq-header-height: 5.5rem; }
@media (max-width: 720px) { :root { --observablehq-header-height: 8rem; } }
#observablehq-header { flex-direction: column; align-items: stretch; gap: 0.5rem; }
.docs-bar { display: flex; align-items: center; gap: 1rem; }
.docs-link { font-weight: 600; padding: 0.25rem 0.75rem; border: 1px solid var(--theme-foreground-focus);
  border-radius: 4px; text-decoration: none; white-space: nowrap; }
.docs-link:hover { background: var(--theme-foreground-focus); color: var(--theme-background); }
.docs-bar-title { color: var(--theme-foreground-muted); font-size: 0.9rem; }
</style>`,
  // On every page: a link back to the documentation, and the notice that the explorer is under
  // development. The documentation is published one folder above the explorer. Framework rewrites
  // relative links that leave the explorer, so the link points to the published documentation, and
  // the script points it to the copy next to this explorer instead: in the preview of a branch, the
  // documentation of that branch.
  header: `<nav class="docs-bar"><a class="docs-link" id="docs-link" href="${DOCS}rUWWTD2024/index.html">← rUWWTD documentation</a>
<span class="docs-bar-title">rUWWTD data explorer</span></nav>
<script>{const m = location.pathname.match(/^(.*\\/)explorer\\//); const a = document.getElementById("docs-link"); a.removeAttribute("target"); if (m) a.href = m[1] + "rUWWTD2024/index.html";}</script>
<div class="under-development"><strong>Under development.</strong> This explorer and the
documentation it draws on are drafts. The spatial points prefill is provisional data under Member State
review, shown for reporters to check before their first delivery. Not an EEA publication.</div>`,
  footer:
    "Draft, under development. Reference data from the rUWWTD documentation; spatial points prefill: provisional Member State data, under review. Not an EEA publication.",
  search: true,
  pager: false
};
