const tilesProvides = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'

let map = L.map('map').setView([-34.9159,-57.9924], 13)

L.tilesProvides(tilesProvides, {
  maxZoom: 18
}).addTo(map)

let marker = L.marker([-34.9159,-57.9924]).addTo(map)

