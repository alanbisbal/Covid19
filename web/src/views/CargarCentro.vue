<template>
  <div
    class="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm"
  >
    <cargarCentro :tipos="tipos" />

  </div>
</template>

<script>
import axios from 'axios';
import cargarCentro from '@/components/Centros/cargarCentro.vue';

export default {
  name: 'App',
  components: {
    cargarCentro,
    
  },

  data: function() {
    return {
      tipos: [],
    };
  },
  mounted: function() {
    axios
      .get(
        'https://admin-grupo37.proyecto2020.linti.unlp.edu.ar/api/centros/tipos'
      )
      .then((result) => {
        this.tipos = result.data.tipos;
      });
  },
};
</script>
