<template>
  <div
    class="container"
  >
    <torta /><br>

    <barra /><br>

    <anillo /><br>
  </div>
</template>

<script>
import barra from '@/components/Estadisticas/graficoBarra.vue';
import torta from '@/components/Estadisticas/graficoTorta.vue';
import anillo from '@/components/Estadisticas/graficoAnillo.vue';

export default {
  name: 'Estadisticas',
  components: {
    barra,
    torta,
    anillo,
  },
};
</script>
