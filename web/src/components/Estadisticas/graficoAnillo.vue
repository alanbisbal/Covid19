<template>
    <div class="row d-flex justify-content-between">

      <div class="col-md-4 col-sm-6">
        <b-form @reset="onReset" v-if="show"> Centros:
          <select v-model="form.centro" class="form-control" v-on:change='onInput'>
            <option v-for="centro in centrosPublicados" :key="centro.id" v-bind:value='centro'>
              {{ centro.nombre }}
            </option>
          </select>
          <label class="mr-sm-2" for="inline-form-custom-select-pref"> Fecha:</label>
            <b-calendar v-on:selected='onInput'
              :min="today_min"
              v-model="form.fecha"
              type="date"
              required
            ></b-calendar>

          <b-button type="reset" variant="danger">Limpiar</b-button>
        </b-form>
      </div>

      <div class="col-md-7 col-sm-6">
        <ve-ring
          :data="chartData"
          :loading="loading">
          <div v-if="dataEmpty" class="data-empty">Seleccione un centro y una fecha para ver el gráfico</div>
        </ve-ring>
      </div>

    </div>
</template>

<script>
  import axios from 'axios';
  export default {
    data() {
      const now = new Date();
      const today = new Date(now.getFullYear(), now.getMonth(), now.getDate());

      return {
        turnosDisponibles: '',
        centrosPublicados: [],
        today_min: today,

        form: {
            centro: null,
            fecha: '',
        },
        dataEmpty: true,
        loading: true,
        chartData: {},
        show: true,
      };
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

        if (this.form.centro && this.form.fecha) {
          this.loading= true;
          const url= 'http://127.0.0.1:5000/api/centros/'+this.form.centro.id+'/turnos_disponibles/'+this.form.fecha;
          const resultado= await axios.get(url)

          this.chartData= {
            columns: ['tipo', 'cant'],
            rows: [ { 'tipo': 'Disponible', 'cant': resultado.data.cant },
                    { 'tipo': 'Ocupado', 'cant': 14-resultado.data.cant } ]
          };
           console.log('data:',this.chartData.rows)
          setTimeout(() => { this.loading= false; }, 3000);
          this.dataEmpty= false;
        }
      },

      onReset(evt) {
        evt.preventDefault();
        // Reset our form values
        this.form.centro = null;
        this.form.fecha = '';
        this.dataEmpty= true;
        // Trick to reset/clear native browser form validation state
        this.show = false;
        this.$nextTick(() => {
          this.show = true;
        });
      },
    },

  };
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
