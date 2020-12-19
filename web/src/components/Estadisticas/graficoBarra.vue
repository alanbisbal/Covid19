<template>
  <div style="height: 500px; width: 100%" >
    <div class="col-md-4 col-sm-6">
        <b-form @reset="onReset" v-if="show"> Centros:
        <select v-model="form.centro" class="form-control" v-on:change='onInput'>
                 <option v-for="centro in centrosPublicados" :key="centro.id" v-bind:value='centro' >
                 {{ centro.nombre }}
                 </option>
             </select>

    <select v-model="form.year" class="form-control" v-on:change='onInput' >
       <option>Year:</option>
       <option v-for="year in getCurrentYear()" :key="year.id" v-bind:value="year">
         {{ year }}</option>
     </select>



        <label class="mr-sm-2" for="inline-form-custom-select-pref"> Fecha:</label>
        <b-button type="reset" variant="danger">Limpiar</b-button>
        </b-form>
    </div>
    <div class="col-md-8 col-sm-6">
      <ve-bar :data="chartData" :settings="chartSettings">
      <div v-if="dataEmpty" class="data-empty">Seleccione un centro y una fecha para ver el gráfico</div>
      </ve-bar>
    </div>

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
        form:{
          centro:null,
          year: '2020',
        },
        result:null,
        show: true,
        dataEmpty: true,
        loading: true,

      }
    },

    mounted: function() {
    axios
      .get('https://admin-grupo37.proyecto2020.linti.unlp.edu.ar/api/centros').
      then((result) => {
        this.centrosPublicados= result.data.centros;
      });
    },

    methods: {

      async onInput(){
        if (this.form.centro && this.form.year) {
         this.loading= true;
         axios
        .get('https://admin-grupo37.proyecto2020.linti.unlp.edu.ar/api/centros/turnos_mes/'+this.form.centro.id +'/'+this.form.year)
        .then((result) => {
          this.result = result.data;
          this.chartData.rows = this.result.data;
        });
        setTimeout(() => { this.loading= false; }, 3000);
         this.dataEmpty= false;
       }
     },
        getCurrentYear() {
           const year = new Date().getFullYear()+200;
           return Array.from({length: year - 1999}, (value, index) => 2000 + index)
      },

    onReset(evt) {
           evt.preventDefault();
           // Reset our form values
           this.form.centro = null;
           this.form.year = 2020;
           this.dataEmpty= true;
           this.chartData.rows= [],
           // Trick to reset/clear native browser form validation state
           this.show = false;
           this.$nextTick(() => {
             this.show = true;
           });
         },
  },



}


</script>

<style>
  .data-empty {
    position: absolute;
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: rgba(0, 0, 0, .3);
    color: #000;
    padding: 20px;
    font-size: 28px;
  }
</style>
