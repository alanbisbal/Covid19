import Vue from 'vue'
import Router from 'vue-router'
Vue.use(Router)


export default new Router({
 mode: 'history',
 base: process.env.BASE_URL,
 routes:[
   {
      path:'/',
      name:'home',
      component: () => import('./views/Home.vue')
   },
   {
      path:'/cargarCentro',
      name:'cargarCentro',
      component: () => import('./views/CargarCentro.vue')
   },
   {
      path:'/estadisticas',
      name:'estadisticas',
      component: () => import('./views/Estadisticas.vue')
   },
   {
      path:'/turno/:id/:fecha',
      name:'turno',
      component: () => import('./views/Turno.vue')
   },
   {
      path:'/centros',
      name:'centros',
      component: () => import('./views/Centros.vue')
   }
 ]
})
