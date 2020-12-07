<template>
  <div>
    <myMap/>
    <index/>
  </div>
</template>


  <script>
  import index from '@/components/Centros/index.vue'
  import myMap from '@/components/Maps/myMap.vue'

  export default {
    name: 'App',
    components: {
      index,
      myMap
    }
  }
  </script>
