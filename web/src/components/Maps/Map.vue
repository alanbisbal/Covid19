<template>
  <div>

      <LMap/>
      <LTileLayer/>
      <LMarker/>
  </div>
</template>

<script>

  
    import { LMap, LTileLayer, LMarker } from 'vue2-leaflet';

    export default {
        name: 'MyAwesomeMap',
        components: {
            LMap,
            LTileLayer,
            LMarker,
          },
        };


</script>
