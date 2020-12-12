<template>
  <b-container fluid>
    <div class="container col-md-8 col-sm-12">
      <b-card-group deck>
        <b-card
          bg-variant="ligth"
          header="Cargar Centro"
          class="text-center"
          header-tag="header"
          header-bg-variant="primary"
          header-text-variant="white"
          style="max-width: 50rem;"
          align="center"
        >
          <b-form @submit="onSubmit" @reset="onReset" v-if="show">
            <b-form-group label="Nombre:">
              <b-form-input
                v-model="form.nombre"
                type="text"
                required
                placeholder="Ingrese un nombre"
              ></b-form-input>
            </b-form-group>

            <b-form-group label="Direccion:">
              <b-form-input
                v-model="form.direccion"
                type="text"
                required
                placeholder="Ingrese una direccion"
              ></b-form-input>
            </b-form-group>

            <b-form-group label="Telefono:">
              <b-form-input
                v-model="form.telefono"
                type="tel"
                required
                placeholder="Ingrese un telefono"
              ></b-form-input>
            </b-form-group>

            <b-form-group label="Hora de apertura:">
              <b-form-input
                v-model="form.hora_apertura"
                required
              ></b-form-input>
            </b-form-group>

            <b-form-group label="Hora de cierre:">
              <b-form-input v-model="form.hora_cierre" required></b-form-input>
            </b-form-group>

            <b-form-group label="Sitio web:">
              <b-form-input
                v-model="form.web"
                type="text"
                placeholder="Ingrese sitio web"
              ></b-form-input>
            </b-form-group>

            <b-form-group label="Tipo:">
              <select v-model="form.tipo" class="form-control">
                <option v-for="tipo in tipos" :key="tipo.id" required>
                  {{ tipo.nombre }}
                </option>
              </select>
            </b-form-group>

            <b-form-group label="latitud:">
              <b-form-input
                v-model="form.latitud"
                type="text"
                required
                placeholder="latitud"
              ></b-form-input>
            </b-form-group>

            <b-form-group label="longitud:">
              <b-form-input
                v-model="form.longitud"
                type="text"
                required
                placeholder="longitud"
              ></b-form-input>
            </b-form-group>

            <b-form-group label="Email:">
              <b-form-input
                v-model="form.email"
                type="email"
                placeholder="Ingrese email"
              ></b-form-input>
            </b-form-group>

            <!-- recaptcha -->
            <recaptcha />
          </b-form>

          <b-card class="mt-3" header="Form Data Result">
            <pre class="m-0">{{ JSON.stringify(this.form) }}</pre>
          </b-card>
        </b-card>
      </b-card-group>
    </div>
  </b-container>
</template>

<script>
import recaptcha from '@/components/Centros/recaptcha.vue';

import axios from 'axios';
export default {
  name: 'crearCentro',
  props: {
    tipos: Array,
  },
  components: {
    recaptcha,
  },
  data() {
    return {
      form: {
        nombre: 'TestApi',
        direccion: 'TestApi',
        telefono: 'TestApi',
        hora_apertura: '10:00',
        hora_cierre: '10:30',
        email: 'TestApi@TestApi',
        web: 'TestApi@TestApi',
        tipo: '',
        latitud: '-34.9759',
        longitud: '-57.9324',
      },
      show: true,
    };
  },
  methods: {
    onSubmit(evt) {
      evt.preventDefault();
      const url =
        'https://admin-grupo37.proyecto2020.linti.unlp.edu.ar/api/centros';
      axios({
        method: 'POST',
        url,
        headers: {
          'Content-Type': 'application/json',
        },
        data: JSON.stringify(this.form),
      })
        .then((response) => {
          console.log(response);
          this.flash('El centro se creo de manera exitosa!', 'success');
          this.$router.push({ name: 'home' });
        })
        .catch((error) => {
          if (error.response) {
            console.log('Error! response:', error.response.data);
            this.flash(error.response.data, 'error');
          }
        });
    },
    onReset(evt) {
      evt.preventDefault();
      // Reset our form values
      this.form.nombre = '';
      this.form.direccion = '';
      this.form.telefono = '';
      this.form.hora_apertura = '';
      this.form.hora_cierre = '';
      this.form.web = '';
      this.form.tipo = '';
      this.form.longitud = '';
      this.form.latitud = '';
      // Trick to reset/clear native browser form validation state
      this.show = false;
      this.$nextTick(() => {
        this.show = true;
      });
    },
  },
};
</script>
