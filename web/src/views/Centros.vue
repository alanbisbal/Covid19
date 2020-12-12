<template>
  <div>
    <div class="container mt-4 text-center">
      <h1>Centros de Ayuda Social</h1>
      <p>
        Para reservar un turno debe seleccionar un centro disponible
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
