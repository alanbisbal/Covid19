<template>
  <div>
    <div class="container mt-4 text-center">
      <h1>Centros de Ayuda Social</h1>
      <p>
        Para reservar un turno debe seleccionar un centro disponible y una fecha
        para la reserva del mismo
      </p>
    </div>
    <myMap />
  </div>
</template>

<script>
import myMap from '@/components/Maps/myMap.vue';

export default {
  name: 'App',
  components: {
    myMap,
  },
};
</script>
