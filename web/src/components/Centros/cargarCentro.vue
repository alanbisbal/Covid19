<template>
  <b-container fluid>
    <div v-for="tipo in tipos" :key="tipo.id">
      {{ tipo.nombre }}
    </div>
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
                v-model="form.hora_inicio"
                type="time"
                required
              ></b-form-input>
            </b-form-group>

            <b-form-group label="Hora de cierre:">
              <b-form-input
                v-model="form.hora_fin"
                type="time"
                required
              ></b-form-input>
            </b-form-group>

            <b-form-group label="Sitio web:">
              <b-form-input
                v-model="form.web"
                type="text"
                placeholder="Ingrese sitio web"
              ></b-form-input>
            </b-form-group>

            <b-form-group label="Tipo:">
              <select v-model="selected" class="form-control">
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
            <pre class="m-0">{{ form }}</pre>
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
        nombre: '',
        direccion: '',
        telefono: '',
        hora_inicio: '',
        hora_fin: '',
        email: '',
        web: '',
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
        'http://127.0.0.1:5000/api/centros';
      axios({
        method: 'POST',
        url,
        headers: {
          'Content-Type': 'application/json',
        },
        data: {
         "nombre": this.form.nombre,
         "direccion": this.form.direccion,
         "telefono": this.form.telefono,
         "hora_apertura": this.form.hora_inicio,
         "hora_cierre": this.form.hora_fin,
         "tipo": this.selected,
         "web": this.form.web,
         "email": this.form.email,
         "latitud": this.form.latitud,
         "longitud": this.form.longitud
        },

      })
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          if (error.response) {
            console.log('Error! response:', error.response.data);
            for (let key in error.response.data) {
              error.response.data[key].forEach((element) => {
                console.log(key, ':', element);
              });
            }
          } else if (error.request) {
            console.log('Error! request:', error.response);
          } else {
            // eslint-disable-next-line
            console.log(error);
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
