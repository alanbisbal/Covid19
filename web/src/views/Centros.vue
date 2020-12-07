<template>
  <div>
    <myMap/>
    <centros/>
  </div>
</template>


  <script>
  import centros from '@/components/Centros/centros.vue'
  import myMap from '@/components/Maps/myMap.vue'

  export default {
    name: 'App',
    components: {
      centros,
      myMap
    }
  }
  </script>
