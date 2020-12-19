<template>
  <div class="container col-md-8 col-sm-12">
    <div class="container mt-4 text-center">
      <p><strong> Cantidad de centros por municipio</strong></p>
    </div>
    <ve-pie :data="chartData"></ve-pie>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      form: {
        municipio: '',
      },
      show: true,
      municipios: [],
      centros: [],
      cantCentros: [],

      chartData: {
        columns: ['municipio', 'cantidadCentros'],
        rows: [],
      },
    };
  },
  async mounted() {
    await axios
      .get('https://api-referencias.proyecto2020.linti.unlp.edu.ar/municipios')
      .then((result) => {
        this.municipios = result.data.data.Town;
      });
    await axios.get('https://admin-grupo37.proyecto2020.linti.unlp.edu.ar/api/centros').then((result) => {
      this.centros = result.data.centros;
    });

    this.centros.forEach((c) => {
      if (!this.cantCentros[c.municipio_id]) {
        this.cantCentros[c.municipio_id] = 1;
      } else {
        this.cantCentros[c.municipio_id] += 1;
      }
    });

    const mun = this.municipios;
    const infoChart = [];
    this.cantCentros.forEach(function(valor, indice) {
      infoChart.push({
        municipio: mun[indice].name,
        cantidadCentros: valor,
      });
    });
    this.chartData.rows = infoChart;
  },
};
</script>
