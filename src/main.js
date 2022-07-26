import Vue from 'vue'
import App from './App.vue'
import './plugins/element.js'
import router from './router'

Vue.config.productionTip = false

new Vue({
  router,
  render: function (h) { return h(App) }
}).$mount('#app')

router.beforeEach((to,from,next)=>{
  let isLogin = window.sessionStorage.getItem('isLogin');
  if(to.path=='/Logout'){
    window.sessionStorage.clear();
    next('/login');
  }else if(to.path == '/login'){
    if(isLogin !=null){
      next('/main');
    }
  }else if(isLogin==null){
    next('/login');
  }
  next();
})
