import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Post from '@/components/Post'
import HttpError from '@/components/HttpError'
import Meta from 'vue-meta'

Vue.use(Router)
Vue.use(Meta)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/posts/:id',
      name: 'Post',
      component: Post
    },
    {
      path: '/oops/:errCode',
      name: 'HttpError',
      component: HttpError
    }
  ]
})
