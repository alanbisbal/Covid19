<template>
  <div>
    <myMap :centros="centros" />
  </div>
</template>


  <script>
  import axios from "axios";
  import myMap from '@/components/Maps/myMap.vue'

  export default {
    name: 'App',
    components: {
      myMap
    },
    data: function () {
      return {
        centros: []
      }
    },
    mounted: function () {
      axios.get("https://admin-grupo37.proyecto2020.linti.unlp.edu.ar/api/centros").then((result) => {
        this.centros = result.data;
      })
    }
  }
  </script>
