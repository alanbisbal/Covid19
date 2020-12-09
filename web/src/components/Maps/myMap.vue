<template>

  <div>
    <l-map
      :zoom="zoom"
      :center="center"
      style="height: 500px; width: 100%"
    >
      <l-tile-layer
        :url="url"
        :attribution="attribution"
      />
      <l-marker
        :key="index"
        v-for="(centro,index) in centros"
        :lat-lng="latLng(centro.latitud,centro.longitud)" />

    </l-map>
  </div>
</template>

<script>
import axios from "axios";
import L from "leaflet";
import { LMap, LTileLayer, LMarker } from "vue2-leaflet";

export default {
  name: "myMap",
  props: {
    centros: Array
  },
  data() {
   return {
     zoom: 11,
     center: [-34.9159, -57.9924],
     url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
     attribution:
     '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
     marker: L.latLng(-34.9159, -57.9924)
   };
 },
 components: {
   LMap,
   LTileLayer,
   LMarker,
 },
 methods: {
   latLng: function (lat,lng) {
     return L.latLng(lat,lng);
   },
 },

  mounted: function () {
      axios.get("https://admin-grupo37.proyecto2020.linti.unlp.edu.ar/api/centros").then((result) => {
        this.centros = result.data.centros;
      })
    },
};

</script>
