import Vue from 'vue';
import App from './App.vue';
import router from './router'; // Router being imported
import 'leaflet/dist/leaflet.css';
import { LMap, LTileLayer, LMarker } from 'vue2-leaflet';
import { Icon } from 'leaflet';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue';
import VueFlashMessage from 'vue-flash-message';
import VCharts from 'v-charts'

Vue.use(VCharts)
Vue.component('l-map', LMap);
Vue.component('l-tile-layer', LTileLayer);
Vue.component('l-marker', LMarker);
Vue.use(BootstrapVue);
Vue.use(IconsPlugin);
Vue.use(VueFlashMessage);

delete Icon.Default.prototype._getIconUrl;
Icon.Default.mergeOptions({
  iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
  iconUrl: require('leaflet/dist/images/marker-icon.png'),
  shadowUrl: require('leaflet/dist/images/marker-shadow.png'),
});

Vue.config.productionTip = false;

new Vue({
  router, // router added to the Vue instance
  render: function(h) {
    return h(App);
  },
}).$mount('#app');
