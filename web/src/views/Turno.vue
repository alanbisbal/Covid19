<template>
    <div class="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm">
    <Turno/>
  </div>


</template>


  <script>
  import Turno from '@/components/Turno.vue'

  export default {
    name: 'App',
    components: {
      Turno
    }
  }
  </script>