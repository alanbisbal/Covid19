<template>
  <div >
    <p>ACA VA EL MAPA CON LOS CENTROS; cuando selecciona reservar turno deberia primero elegir la fecha</p>
    <div class="form-inline"> 
    <div class="col-auto my-1">
     <b-button variant="success" :to="{name:'centro'}">Crear Centro</b-button>
     </div>
     <div>
      <b-button variant="primary" :to="{name:'turno'}">Reservar Turno</b-button>
      </div>
    </div>
  </div>



</template>
