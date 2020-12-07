<template>
<b-container fluid>
  <div class="container col-md-8 col-sm-12">
  <b-card-group deck >
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
      <b-form-group label="Nombre:" >
        <b-form-input
          v-model="form.nombre"
          type="text"
          required
          placeholder="Ingrese un nombre"
        ></b-form-input>
      </b-form-group>


      <b-form-group label="Direccion:" >
        <b-form-input
          v-model="form.direccion"
          type="text"
          required
          placeholder="Ingrese una direccion"
        ></b-form-input>
      </b-form-group>

      <b-form-group label="Telefono:" >
        <b-form-input
          v-model="form.telefono"
          type="tel"
          required
          placeholder="Ingrese un telefono"
        ></b-form-input>
      </b-form-group>


      <b-form-group label="Hora de apertura:" >
        <b-form-select
          v-model="form.hora_apertura"
          :options="hora_apertura"
          required
        ></b-form-select>
      </b-form-group>

      <b-form-group label="Hora de cierre:" >
        <b-form-select
          v-model="form.hora_inicio"
          :options="hora_cierre"
          required
        ></b-form-select>
      </b-form-group>

      <b-form-group label="Sitio web:" >
        <b-form-input
          v-model="form.web"
          type="text"
          required
          placeholder="Ingrese sitio web"
        ></b-form-input>
      </b-form-group>

<p>----------------------------------------------------------------------------</p>
      <b-form-group label="Tipo:" >
        <b-form-select
          v-model="form.tipo"
          :options="tipo"
          required
          ></b-form-select>
        </b-form-group>

      <b-form-group label="latitud:" >
        <b-form-input
          v-model="form.latitud"
          type="text"
          required
          placeholder="latitud"
        ></b-form-input>
      </b-form-group>

      <b-form-group label="longitud:" >
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
          required
          placeholder="Ingrese email"
        ></b-form-input>
      </b-form-group>

      <b-button type="submit" variant="primary">Crear</b-button>
      <b-button type="reset" variant="danger">Limpiar</b-button>
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
  export default {
    data() {
      return {
        form: {
          nombre:'',
          direccion:'',
          telefono: '',
          hora_apertura:'',
          hora_cierre:'',
          email: '',
          web: '',
          tipo: null,
          longitud: '',
          latitud: ''

        },
        tipo: [{ text: 'Selecione una opción', value: null }, 'Merendero', 'Colegio'],
        show: true
      }
    },
    methods: {
      onSubmit(evt) {
        evt.preventDefault()
        alert(JSON.stringify(this.form))
      },
      onReset(evt) {
        evt.preventDefault()
        // Reset our form values
        this.form.nombre = ''
        this.form.direccion = ''
        this.form.telefono = ''
        this.form.hora_apertura = null
        this.form.hora_cierre = null
        this.form.web= ''
        this.form.tipo= null
        this.form.longitud= ''
        this.form.latitud= ''
        // Trick to reset/clear native browser form validation state
        this.show = false
        this.$nextTick(() => {
          this.show = true
        })
      }
    }
  }
</script>
