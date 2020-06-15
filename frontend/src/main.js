import Vue from 'vue'
import App from './App.vue'

import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import VueResource from 'vue-resource'
import VueRouter from 'vue-router'
import Routes from './router'
import { ValidationProvider } from 'vee-validate'

Vue.use(VueResource);
Vue.use(VueRouter);
Vue.use('ValidationProvider', ValidationProvider);

const router = new VueRouter({
    routes: Routes,
    mode: 'history'
});

new Vue({
    el: '#app',
    render: h => h(App),
    router: router
})
