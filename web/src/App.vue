<template>
  <div id="app">
    <div id="nav">
      <b-navbar toggleable="md" type="dark" variant="dark">

        <b-container>
          <b-navbar-brand ><img alt="Vue logo" src="./assets/logo.png" width="40" height="40" /></b-navbar-brand>
            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>



            <b-collapse id="nav-collapse" is-nav>
               <b-navbar-nav>
                  <b-nav-item :to="{name:'home'}" exact>Inicio</b-nav-item>
                  <b-nav-item :to="{name:'centros'} "> Centros </b-nav-item>
                  <b-nav-item :to="{name:'cargarCentro'} " >Solicitar Centro</b-nav-item>
                  <b-nav-item :to="{name:'estadisticas'} " >Estadisticas</b-nav-item>
              </b-navbar-nav>
            </b-collapse>
        </b-container>


      </b-navbar>

    </div>
    <router-view />

  </div>
</template>
