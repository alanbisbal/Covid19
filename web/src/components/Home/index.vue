<template>
  <div>
  <b-jumbotron >
    
    
    <template #header >Donaciones Covid19</template>

    <template #lead>
      <br>
      En el contexto de pandemia por el cual atravesamos los más vulnerables son los mas perjudicados.
      Solicita tu turno para donar ropa ,plasma y sangre en tu centro más cercano.
      <br>
      También podes recibir donaciones en caso de necesitarlo
    </template>

    

    <p>Contacto: Covid19@donaciones.com</p>
     <div class="form-inline">
    <div class="col-auto my-1">
      <b-button variant="primary" :to="{name:'centros'}">Reservar Turno</b-button>
    </div>
    <b-button variant="success" :to="{name:'cargarCentro'} ">Solicitar Centro</b-button>
     </div>

    
  </b-jumbotron>
</div>

 
</template>


