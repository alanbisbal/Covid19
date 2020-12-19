<template>
  <div style="height: 500px; width: 100%" >
    <div class="col-md-4 col-sm-6">
        <b-form @reset="onReset" v-if="show"> Centros:
        <select v-model="form.centro" class="form-control" v-on:change='onInput'>
                 <option v-for="centro in centrosPublicados" :key="centro.id" v-bind:value='centro' >
                 {{ centro.nombre }}
                 </option>
             </select>

        <label class="mr-sm-2" for="inline-form-custom-select-pref"> Fecha:</label>
        <b-button type="reset" variant="danger">Limpiar</b-button>
        </b-form>
    </div>

    <div class="col-md-8 col-sm-6">
      <ve-bar :data="chartData" :settings="chartSettings">
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
      .get('http://127.0.0.1:5000/api/centros').
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
        if (this.form.centro && this.form.year) {
         this.loading= true;
         axios
        .get('http://127.0.0.1:5000/api/centros/turnos_mes/'+this.form.centro.id +'/2020')
        .then((result) => {
          this.result = result.data;
          this.chartData.rows = this.result.data;
        });
        setTimeout(() => { this.loading= false; }, 3000);
         this.dataEmpty= false;
       }
     },

    onReset(evt) {
           evt.preventDefault();
           // Reset our form values
          console.log('form full',this.form);
           this.form.centro = null;
           this.form.year = 2000;
           this.dataEmpty= true;
           // Trick to reset/clear native browser form validation state
           this.show = false;
           this.$nextTick(() => {
             console.log('form vacio',this.form);
             this.show = true;
           });
         },
  },



}


</script>
