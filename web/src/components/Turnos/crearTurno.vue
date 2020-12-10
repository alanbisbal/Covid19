<template>
  <b-container fluid>
    <div v-for="turno in turnos" :key="turno.id">
      {{ turno.hora_inicio }}
    </div>

    <div class="container col-md-8 col-sm-12">
      <b-card-group deck>
        <b-card
          bg-variant="ligth"
          header="Crear Turno"
          class="text-center"
          header-tag="header"
          header-bg-variant="primary"
          header-text-variant="white"
          style="max-width: 50rem;"
          align="center"
        >
          <b-form @submit="onSubmit" @reset="onReset" v-if="show">
            <b-form-group label="Email:">
              <b-form-input
                v-model="form.email"
                type="email"
                required
                placeholder="Ingrese email"
              ></b-form-input>
            </b-form-group>

            <b-form-group label="Telefono:">
              <b-form-input
                v-model="form.telefono"
                type="tel"
                required
                placeholder="Ingrese su telefono"
              ></b-form-input>
            </b-form-group>

            <b-form-group
              label="Hora de inicio:"
              description="Nota:Los turnos se realizan en bloques de 30 minutos"
            >
              <select
                v-model="form.hora_inicio"
                class="form-control"
                id="turno.id"
                required
              >
                <option v-for="turno in turnos" :key="turno.id">
                  {{ turno.hora_inicio }}
                </option>
              </select>
            </b-form-group>

            <b-form-group label="Fecha:">
              <b-form-input v-model="form.fecha" type="date"></b-form-input>
            </b-form-group>

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
  components: {
    recaptcha,
  },
  props: {
    turnos: Array,
  },
  data() {
    return {
      form: {
        centro_id: '19',
        email: '',
        telefono: '',
        hora_inicio: null,
        hora_fin: '10:00',
        fecha: '',
      },
      show: true,
    };
  },
  methods: {
    onSubmit(evt) {
      evt.preventDefault();
      const url =
        'https://admin-grupo37.proyecto2020.linti.unlp.edu.ar/api/centros/19/reserva';
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
      this.form.email = '';
      this.form.telefono = '';
      this.form.hora_inicio = null;
      this.form.fecha = '';
      // Trick to reset/clear native browser form validation state
      this.show = false;
      this.$nextTick(() => {
        this.show = true;
      });
    },
  },
};
</script>
