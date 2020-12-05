<template>
<b-container fluid>
  <div class="container col-md-8 col-sm-12">
  <b-card-group deck >
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

      <b-form-group label="Telefono:" >
        <b-form-input
          v-model="form.telefono"
          type="tel"
          required
          placeholder="Ingrese su telefono"
        ></b-form-input>
      </b-form-group>

      <b-form-group label="Hora de inicio:" description="Los turnos son en bloques de 30 minutos" >
        <b-form-select
          v-model="form.hora_inicio"
          :options="hora_inicio"
          required
        ></b-form-select>
      </b-form-group>

      <b-form-group label="Fecha:" >
        <b-form-input
          v-model="form.Fecha"
          type="date"
          readonly=true
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
          email: '',
          telefono: '',
          hora_inicio: null,
          fecha:' '
        },
        hora_inicio: [{ text: 'Selecione una opción', value: null }, 'Carrots', 'Beans', 'Tomatoes', 'Corn'],
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
        this.form.email = ''
        this.form.telefono = ''
        this.form.hora_inicio = null
        this.form.fecha = ''
        // Trick to reset/clear native browser form validation state
        this.show = false
        this.$nextTick(() => {
          this.show = true
        })
      }
    }
  }
</script>
