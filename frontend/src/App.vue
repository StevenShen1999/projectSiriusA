<template>
  <div id="app">
    <navbar></navbar>
    <br>
    <router-view></router-view>
  </div>
</template>

<script>
import navbar from './components/navbar.vue'
export default {
  name: 'app',
  components: {
    navbar: navbar
  },
  data () {
    return {
    }
  }
}
</script>

<style>

</style>
