import Vue from 'vue'
import VueRouter from 'vue-router'
import SignIn from '../login/signIn'
import Main from '../main/main'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'signIn',
    component: SignIn
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
