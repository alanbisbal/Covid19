<template>
  <div
    class="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm"
  >
    <crearTurno :turnos="turnos" />
  </div>
</template>

<script>
import axios from 'axios';
import crearTurno from '@/components/Turnos/crearTurno.vue';

export default {
  name: 'App',
  components: {
    crearTurno,
  },

  data: function() {
    return {
      turnos: [],
    };
  },
  mounted: function() {
    axios
      .get(
        'https://admin-grupo37.proyecto2020.linti.unlp.edu.ar/api/centros/19/turnos_disponibles/'
      )
      .then((result) => {
        this.turnos = result.data.turnos;
      });
  },
};
</script>
