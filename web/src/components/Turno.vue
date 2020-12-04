<template>
<b-container fluid>
  <div class="container col-md-8 col-sm-12">
  <b-card-group deck >
      <b-card bg-variant="ligth" header="Crear Turno" class="text-center" 
      header-tag="header" style="max-width: 40rem;"  align="center">

  <b-row class="my-1">
    <b-col sm="2">
      <label for="input-small">Email:</label>
    </b-col>
    <b-col sm="10">
      <b-form-input id="input-small" size="sm" type="email" placeholder="Ingrese su email"></b-form-input>
    </b-col>
     <b-col sm="2">
      <label for="input-small">Telefono:</label>
    </b-col>
    <b-col sm="10">
      <b-form-input id="input-small" size="sm" type="tel" placeholder="Ingrese su telefono"></b-form-input>
    </b-col>
     <b-col sm="2">
      <label for="input-small">Hora de inicio:</label>
    </b-col>
    <b-col sm="10">
      <b-form-input id="input-small" size="sm" type="time" placeholder="Ingrese la hora de inicio"></b-form-input>
    </b-col>
     <b-col sm="2">
      <label for="input-small">Fecha:</label>
    </b-col>
    <b-col sm="10">
      <b-form-input id="input-small" size="sm" type="date" readonly=true></b-form-input>
    </b-col>
  </b-row>
  
   
   <div class="form-inline">
          <div
            class="card-body d-flex justify-content-between align-items-center"></div>
          <div class="col-auto my-1">
            <b-button variant="primary"  type="submit"> Crear</b-button>
          </div>
          
        </div>

  </b-card>
  </b-card-group>

  </div>
</b-container>
</template>