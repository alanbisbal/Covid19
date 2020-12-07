<template>
  <div class="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm">
    <crearTurno/>
  </div>
</template>


<script>
  import crearTurno from '@/components/Turnos/crearTurno.vue'

  export default {
    name: 'App',
    components: {
      crearTurno
    }
  }
</script>
