<template>
  <div class="container col-md-8 col-sm-12">
    <div v-for="municipio in municipios" :key="municipio.id">
      <p>municipio: {{ municipio.name }} id : {{ municipio.id }}</p>
    </div>

    <div v-for="centro in centros" :key="centro.id">
      <p>
        centrossssssss id: {{ centro.id }} municip: {{ centro.municipio_id }}
      </p>
    </div>

    <b-form inline @submit="onSubmit" v-if="show">
      <label class="mr-sm-2" for="inline-form-custom-select-pref"
        >Municipio:</label
      >
      <select v-model="form.municipio_id" class="form-control" required>
        <option v-for="municipio in municipios" :key="municipio.id">
          {{ municipio.name }}
        </option>
      </select>

      <b-button type="submit" variant="primary">Crear</b-button>
      <b-button type="reset" variant="danger">Limpiar</b-button>
    </b-form>
    <div class="container mt-4 text-center">
      <p><strong> Canitidad de centros por municipio</strong></p>
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
      infoChartData: [],
      chartData: {
        columns: ['municipio', 'cantidadCentros'],
        rows: [],
      },
    };
  },
  mounted: function() {
    axios
      .get('https://api-referencias.proyecto2020.linti.unlp.edu.ar/municipios')
      .then((result) => {
        this.municipios = result.data.data.Town;
      });
    axios.get('http://127.0.0.1:5000/api/centros').then((result) => {
      this.centros = result.data.centros;
    });
  },

  methods: {
    onSubmit(evt) {
      evt.preventDefault();
      console.log('entreeeeee', this.centros);

      this.centros.forEach((c) => {
        console.log('id de municipio', c.municipio_id);
        if (!this.cantCentros[c.municipio_id]) {
          this.cantCentros[c.municipio_id] = 1;
          console.log('cant', this.cantCentros[c.municipio_id]);
        } else {
          this.cantCentros[c.municipio_id] += 1;
          console.log('cant', this.cantCentros[c.municipio_id]);
        }
      });
      console.log('result', this.cantCentros);

      this.cantCentros.forEach(function(valor, indice) {
        console.log('entreeeee al for');
        console.log('indice', indice);
        console.log('valor', valor);
        console.log('tmunicipio', this.municipios[indice].name);
        console.log('this.cantCentros[indice]', this.cantCentros[indice]);
        this.infoChartData.push({
          municipio: this.municipios[indice].name,
          cantidadCentros: this.cantCentros[indice],
        });
      });
      this.chartData.rows = this.infoChartData;
      console.log('chartData.rows', this.chartData.rows);
      console.log('infochartData.rows', this.infoChartData);
    },
  },
};
</script>
