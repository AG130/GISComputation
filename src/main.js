import Vue from 'vue'
import App from './App.vue'
import './plugins/element.js'
import router from './router'
import * as turf from '@turf/turf'

Vue.config.productionTip = false
new Vue({
  router,
  render: function (h) { return h(App) }
}).$mount('#app')
Vue.prototype.$turf =turf