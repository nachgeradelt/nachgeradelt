import Vue from 'vue'
import Router from 'vue-router'
import Tour from '@/components/Tour'
import List from '@/components/List'
import About from '@/components/About'
import Contact from '@/components/Contact'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      component: Tour
    },
    {
      path: '/list',
      component: List
    },
    {
      path: '/about',
      component: About
    },
    {
      path: '/contact',
      component: Contact
    }
  ],
  mode: 'history'
})
