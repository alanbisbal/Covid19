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
      path:'/centro',
      name:'centro',
      component: () => import('./views/Centro.vue')
   },
   {
      path:'/estadisticas',
      name:'estadisticas',
      component: () => import('./views/Estadisticas.vue')
   },
   {
      path:'/centros',
      name:'centros',
      component: () => import('./views/Centros.vue')
   }
 ]
})
