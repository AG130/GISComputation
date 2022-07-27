import Vue from 'vue'
import VueRouter from 'vue-router'
import login from '../login/login'
import Main from '../main/main'
import PersonalInf from '../main/aside/personalInf'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'login',
    component: login
  },
  {
    path: '/login',
    name: login,
    component: login
  },
  {
    path: '/main/:username',
    name: 'main',
    component: Main
  },
  {
    path: '/personalInf',
    name: 'personalInf',
    component: PersonalInf
  }

]

const router = new VueRouter({
  mode: 'history',
  routes
})

router.beforeEach((to, from, next) => {
  if (to.path == '/login') {
    return next()
  };
  const isLogin = window.sessionStorage.getItem('isLogin');
  if (isLogin == null) {
    return next('/login')
  }
  next()
})

export default router
