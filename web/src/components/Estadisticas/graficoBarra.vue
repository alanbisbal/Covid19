<template>
  <div style="height: 500px; width: 100%" >
    <div class="col-md-4 col-sm-6">
        <b-form  v-if="show"> Centros:
        <select v-model="this.centro" v-bind='centrosPublicados' class="form-control" v-on:change='onInput'>
                 <option v-for="centro in centrosPublicados" :key="centro.id" v-bind='centro' >
                 {{ centro.nombre }}
                 </option>
             </select>
        <label class="mr-sm-2" for="inline-form-custom-select-pref"> Fecha:</label>
        <b-button type="reset" variant="danger">Limpiar</b-button>
        </b-form>
    </div>

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
         centrosPublicados: [],
         chartData: {
          columns: [ 'mes', 'cantidad'],
          rows: [],
        },

        centro:'19',
        year: '2020',
        result:null,
        show: true,
      }
    },

    mounted: function() {
    axios
      .get('https://admin-grupo37.proyecto2020.linti.unlp.edu.ar/api/centros').
      then((result) => {
        this.centrosPublicados= result.data.centros;
      });
    },

    created() {
      axios
        .get('http://127.0.0.1:5000/api/centros/turnos_mes/19/2020')
        .then((result) => {
          this.result = result.data;
          this.chartData.rows = this.result.data;
        });
    },
    methods: {
      async onInput(){
      axios
        .get('http://127.0.0.1:5000/api/centros/turnos_mes/19/2020')
        .then((result) => {
          this.result = result.data;
          this.chartData.rows = this.result.data;
        });

    }
  }}


</script>
