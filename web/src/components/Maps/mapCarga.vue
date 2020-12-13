<template>

  <div style="height: 500px; width: 100%">
    <l-map
    :zoom="zoom"
    :center="center"
    style="height: 500px; width: 100%"
    @click="changeMarker"
    >
      <l-tile-layer
        :url="url"
        :attribution="attribution"
      />
      <l-marker  v-bind="marker" :lat-lng="marker" @update:latLng="updateAddress"/>

    </l-map>
  </div>
</template>

<script>
import L from "leaflet";
import { LMap, LTileLayer, LMarker} from "vue2-leaflet";

export default {
  name: "MapCarga",
  components: {
    LMap,
    LTileLayer,
    LMarker,
  },
  data() {
    return {
      zoom: 6,
      center: L.latLng(-36.5635, -60.1076),
      url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      attribution:
        '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      currentZoom: 11.5,
      marker: L.latLng(-34.9035, -57.9376)
    };
  },
  methods: {
    changeMarker(event){
      this.marker = L.latLng(event.latlng.lat, event.latlng.lng)

    },
    updateAddress (value) {

        console.log('mapa',value);
            this.$emit('update:latlng', value)
       }


  },
  };
</script>
