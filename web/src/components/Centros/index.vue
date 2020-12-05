<template>
  <div >
    <p>---CONSULTA DE TEST DE AXIOS-----</p>
    <div class="content">
      <p>Nombre: {{ result.centros[1].nombre }}</p>

    </div>
    <p>---FIN-----</p>


    <p>ACA VA EL MAPA CON LOS CENTROS; cuando selecciona reservar turno deberia primero elegir la fecha</p>
    <div class="form-inline">
    <div class="col-auto my-1">
      <b-button variant="primary" :to="{name:'turno'}">Reservar Turno</b-button>
      </div>
    </div>
  </div>



</template>



<script>
import axios from "axios";
export default {
  data: () => ({
    result: null
  }),
  created() {
    axios.get("https://admin-grupo37.proyecto2020.linti.unlp.edu.ar/api/centros").then((result) => {
      this.result = result.data;
    })
  }
};
</script>

<style scoped lang="scss">

</style>
