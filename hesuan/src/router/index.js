import Vue from 'vue'
import VueRouter from 'vue-router'
import login from '../login/login'
import Main from '../main/main'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'login',
    component: login
  },
  {
    path:'/',
    name:'main',
    component:Main
  }

]

const router = new VueRouter({
  mode:'history',
  routes
})

export default router
