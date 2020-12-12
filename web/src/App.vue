<template>
  <div id="app">
    <div id="nav">
      <b-navbar toggleable="md" type="dark" variant="dark">
        <b-container>
          <b-navbar-brand
            ><img alt="Vue logo" src="./assets/logo.png" width="40" height="40"
          /></b-navbar-brand>
          <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

          <b-collapse id="nav-collapse" is-nav>
            <b-navbar-nav>
              <b-nav-item :to="{ name: 'home' }" exact>Inicio</b-nav-item>
              <b-nav-item :to="{ name: 'centros' }"> Centros </b-nav-item>
              <b-nav-item :to="{ name: 'cargarCentro' }"
                >Solicitar Centro</b-nav-item
              >
              <b-nav-item :to="{ name: 'estadisticas' }"
                >Estadisticas</b-nav-item
              >
            </b-navbar-nav>
          </b-collapse>
        </b-container>
      </b-navbar>
    </div>

    <flash-message
      transitionIn="animated swing"
      class="myCustomClass"
    ></flash-message>
    <router-view />

    <footer class="footer-copyright text-center py-3">
      <p class="p-1">
        Grupo37 &copy; Proyecto de Software, 2020 |
        <a
          href="https://www.info.unlp.edu.ar/"
          alt="Facultad de informatica unlp"
          target="_blank"
          >Facultad de Informática |
        </a>
        <a href=" https://unlp.edu.ar/" alt="UNLP" target="_blank">UNLP</a>
      </p>
    </footer>
  </div>
</template>

<script>
require('vue-flash-message/dist/vue-flash-message.min.css');
</script>
