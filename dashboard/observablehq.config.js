// Observable Framework configuration: https://observablehq.com/framework/config
export default {
  title: "rUWWTD spatial points prefill",
  root: "src",
  pages: [
    {name: "Agglomerations", path: "/agglomerations"},
    {name: "Treatment plants (to come)", path: "/uwwtp"},
    {name: "Discharge points (to come)", path: "/discharge-points"}
  ],
  theme: ["air", "near-midnight"],
  head: '<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><circle cx=%2250%22 cy=%2250%22 r=%2240%22 fill=%22%232b7bb9%22/></svg>">',
  footer:
    "Draft. Prefill of the reference year 2024 reporting under Directive 91/271/EEC: provisional Member State data, under review. Not an EEA publication.",
  search: true,
  pager: false
};
