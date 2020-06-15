import homepage from './components/homepage.vue'
import addBlog from './components/addBlog.vue'
import blog from './components/blog.vue'

export default [
    { path:'/', component:homepage },
    { path:'/add', component: addBlog },
    { path:'/blog/:id', component: blog }
]