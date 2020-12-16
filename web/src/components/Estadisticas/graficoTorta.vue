<template>
  <div class="container col-md-8 col-sm-12">
    <div v-for="municipio in municipios" :key="municipio.id">
      <p>municipio id : {{ municipio.id }}</p>
    </div>

    <div v-for="centro in centros" :key="centro.id">
      <p>centros id: {{ centro.id }}</p>
    </div>

    <b-form inline @submit="onSubmit" @reset="onReset" v-if="show">
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
      chartData: {
        columns: ['date', 'cost', 'profit'],
        rows: [
          { date: 'avellaneda', cost: 123, profit: 3 },
          { date: '01/02', cost: 1223, profit: 6 },
          { date: '01/03', cost: 2123, profit: 90 },
          { date: '01/04', cost: 4123, profit: 12 },
          { date: '01/05', cost: 3123, profit: 15 },
          { date: '01/06', cost: 7123, profit: 20 },
        ],
      },
    };
  },
  mounted: function() {
    axios
      .get('https://api-referencias.proyecto2020.linti.unlp.edu.ar/municipios')
      .then((result) => {
        this.municipios = result.data.data.Town;
      });
    axios
      .get('https://admin-grupo37.proyecto2020.linti.unlp.edu.ar/api/centros')
      .then((result) => {
        this.centros = result.data.centros;
        console.log('entreeeeeeee');
      });
  },

  methods: {
    onSubmit(evt) {
      evt.preventDefault();
    },
    onReset(evt) {
      evt.preventDefault();
      // Reset our form values
      this.form.municipio_id = '';
      // Trick to reset/clear native browser form validation state
      this.show = false;
      this.$nextTick(() => {
        this.show = true;
      });
    },
  },
};
</script>
