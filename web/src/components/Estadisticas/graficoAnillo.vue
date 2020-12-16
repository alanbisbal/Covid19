<template>
  <div class="container col-md-8 col-sm-12">

    <b-form  @submit="onSubmit" @reset="onReset" v-if="show"> Centros:
      <select v-model="form.centro" class="form-control" required>
        <option v-for="centro in centrosPublicados" :key="centro.id" v-bind:value='centro'>
          {{ centro.nombre }}
        </option>
      </select>
      <label class="mr-sm-2" for="inline-form-custom-select-pref"> Fecha:</label>
        <b-calendar
          :min="today_min"
          v-model="form.fecha"
          type="date"
          required
        ></b-calendar>

      <b-button type="submit" variant="primary"
          >Crear</b-button
      >
      <b-button type="reset" variant="danger">Limpiar</b-button>
    </b-form>

    <ve-ring :data="chartData"></ve-ring>

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
            centro: {},
            fecha: '',
        },
        chartData: {},
        centerAndDate: false,
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
      onSubmit(evt){
        evt.preventDefault();
        const url= 'http://127.0.0.1:5000/api/centros/'+this.form.centro.id+'/turnos_disponibles/'+this.form.fecha;
        axios
        .get(url).then((result) => {
          this.turnosDisponibles = result.data.cant;
          console.log('GET RESULTADO: ', result.data.cant);
          console.log('EL THIS: ', this.turnosDisponibles);
        });
        const d= {'d': this.turnosDisponibles, 'o': 14-this.turnosDisponibles}
        this.setearGrafico(d);
      },
      setearGrafico(d){
        this.chartData= {
          columns: ['tipo', 'cant'],
          rows: [ { 'tipo': 'Disponible', 'cant': d.d },
                  { 'tipo': 'Ocupado', 'cant': d.o } ]
        }
      },
      onReset(evt) {
        evt.preventDefault();
        // Reset our form values
        this.form.centro = {};
        this.form.fecha = '';
        // Trick to reset/clear native browser form validation state
        this.show = false;
        this.$nextTick(() => {
          console.log('entre');
          this.show = true;
        });
      },
    },

  };
</script>
