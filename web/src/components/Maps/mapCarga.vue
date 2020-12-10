<template>

  <div style="height: 500px; width: 100%">
    <l-map
    :zoom="zoom"
    :center="center"
    style="height: 200px; width: 50%"
    >
      <l-tile-layer
        :url="url"
        :attribution="attribution"
      />
      <l-marker :lat-lng="marker"/>

    </l-map>
  </div>
</template>

<script>
import L from "leaflet";
import { LMap, LTileLayer, LMarker} from "vue2-leaflet";

export default {
  name: "Example",
  components: {
    LMap,
    LTileLayer,
    LMarker,
  },
  data() {
    return {
      zoom: 13,
      center: L.latLng(-34.9159, -57.9924),
      url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      attribution:
        '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      currentZoom: 11.5,
      marker: L.latLng(-34.9159, -57.9924)
    };
  },
  };
</script>
