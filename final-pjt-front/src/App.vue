<template>
  <!-- <v-app id="app" class="bg-dark text-white"> -->
  <v-app id="app">
    <nav-bar></nav-bar>

    <router-view></router-view>
  </v-app>
</template>

<script>
  import Vue from 'vue'
  import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

  // Import Bootstrap and BootstrapVue CSS files (order is important)
  import 'bootstrap/dist/css/bootstrap.css'
  import 'bootstrap-vue/dist/bootstrap-vue.css'

  // Make BootstrapVue available throughout your project
  Vue.use(BootstrapVue)
  // Optionally install the BootstrapVue icon components plugin
  Vue.use(IconsPlugin)

  import { mapGetters, mapActions } from 'vuex'
  import NavBar from '@/components/NavBar.vue'



  export default {
    name: 'App',
    components: { NavBar },
    methods: {
      ...mapActions(['fetchCurrentUser']),
    },
    created() {
      this.fetchCurrentUser()
    },
    computed: {
      ...mapGetters(['movie',]),
      imgUrl(){
        return `https://www.themoviedb.org/t/p/w300_and_h450_bestv2/${this.movie.backdrop_path}`
      },
      styleObject(){
        const styleObject = {
          'top': '0',
          'bottom': '0',
          'position': 'fixed',
          'overflow-y':'scroll',
          'overflow-x':'hidden',
          'width': '100%',
          'height': '100%',
          'background-image': this.imgUrl,
          'background-repeat': 'no-repeat',
          'background-size': '100% 100%',
        }
        return styleObject
      }
    },
  }
</script>

<style scoped>
#app{
  top: 0;
  bottom: 0;
  position: fixed;
  overflow-y:scroll; 
  overflow-x:hidden;
  width: 100%;
  height: 100%;
  background-repeat: no-repeat;
  background-size: 100% 100%;
}

</style>
