// The base layers of the spatial points maps: the OpenStreetMap map, and Esri satellite imagery with
// place names and boundaries on top. A control in the corner of the map switches between them, and
// the browser keeps the choice for the next map. Each layer carries its own attribution.
import * as L from "../../_npm/leaflet@1.9.4/b6187c6b.js";

const ESRI = "https://server.arcgisonline.com/ArcGIS/rest/services";
const KEY = "explorer-basemap";

export function addBaseLayers(map) {
  const layers = {
    "Map": L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
      maxZoom: 19,
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }),
    "Satellite": L.layerGroup([
      L.tileLayer(`${ESRI}/World_Imagery/MapServer/tile/{z}/{y}/{x}`, {
        maxZoom: 19,
        attribution: "Imagery &copy; Esri, Maxar, Earthstar Geographics and the GIS User Community"
      }),
      L.tileLayer(`${ESRI}/Reference/World_Boundaries_and_Places/MapServer/tile/{z}/{y}/{x}`, {
        maxZoom: 19,
        attribution: "Places &copy; Esri"
      })
    ])
  };
  let chosen = "Map";
  try { if (localStorage.getItem(KEY) in layers) chosen = localStorage.getItem(KEY); } catch (e) {}
  layers[chosen].addTo(map);
  L.control.layers(layers, null, {position: "topright"}).addTo(map);
  map.on("baselayerchange", (e) => { try { localStorage.setItem(KEY, e.name); } catch (err) {} });
}
