<template>
    <div class="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm">
    <Estadisticas/>
  </div>


</template>


  <script>
  import Estadisticas from '@/components/Estadisticas.vue'

  export default {
    name: 'App',
    components: {
      Estadisticas
    }
  }
  </script>
