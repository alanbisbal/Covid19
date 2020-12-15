<template>
  <div
    class="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm"
  >
  <barra/>
  <torta/>
  <torta2/>
</div>
</template>

<script>
import barra from '@/components/Estadisticas/graficoBarra.vue';
import torta from '@/components/Estadisticas/graficoTorta.vue';
import torta2 from '@/components/Estadisticas/graficoTorta2.vue';


export default {
  name: 'Estadisticas',
  components: {
    barra,
    torta,
    torta2

  },
};
</script>
