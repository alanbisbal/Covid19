<template>
  <div style="height: 500px; width: 100%" >
    <ve-bar :data="chartData" :settings="chartSettings">
    </ve-bar>
  </div>
</template>

<script>
import axios from 'axios';
  export default {
    data () {
      this.chartSettings = {
        dimension: ['mes'],
        metrics: ['cantidad']
      }
      return {
        chartData: {
          columns: [ 'mes', 'cantidad'],
          rows: [],
        },
        result:null
      }
    },
    created() {
      axios
        .get('http://127.0.0.1:5000/api/centros/turnos_mes/19/2020-12-12')
        .then((result) => {
          this.result = result.data;
          this.chartData.rows = this.result.data;
        });
    },
  }
</script>
