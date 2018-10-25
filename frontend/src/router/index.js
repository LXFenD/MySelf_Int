import Vue from 'vue'
import Router from 'vue-router'
import MS_Home from '../components/MS_Home'
import BG_Home from '../components/BG_Home'
import MA_Home from '../components/MA_Home'
import Blog_Write from '../components/Blog-Write'
import blog_video from '../components/blog_video'

Vue.use(Router);

import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.min.js'

export default new Router({
  routes: [
    {
      path: '/',
      name: 'MA_Home',
      component: MA_Home
    },
    {
      path: '/blog/',
      name: 'BG_Home',
      component: BG_Home
    },
    {
      path: '/ms/',
      name: 'MS_Home',
      component: MS_Home
    }
    ,
    {
      path: '/bw/',
      name: 'Blog_Write',
      component: Blog_Write
    },
     {
      path: '/bv/',
      name: 'blog_video',
      component: blog_video
    },
  ],
  mode:'history'
})
