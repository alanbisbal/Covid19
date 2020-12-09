<template>
  <div class="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm">
    <cargarCentro/>
  </div>
</template>


<script>
  import cargarCentro from '@/components/Centros/cargarCentro.vue'

  export default {
    name: 'App',
    components: {
      cargarCentro,
    }
  }
</script>
