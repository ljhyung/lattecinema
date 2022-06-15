<template>
  <nav id="navbar" class=" bg-dark text-white">
    <div class="row justify-content-between align-items-center mt-3">
      <div class="justify-content-start col">
        <ul class="float-start row list-unstyled  align-items-center">
          <li class="col-4">
            <router-link :to="{ name: 'movies' }" class="routerLink">
              <img src="@/assets/lattelogo.png" alt="" width="150">
            </router-link>
          </li>
          <li class="col-4 text-center">
            <img src="@/assets/ageselction.png" alt="" width="150">
            <b-form-select v-model="selected" :options="options" id="ageselect"></b-form-select>
          </li>
          <li class="col-2">
            <router-link :to="{ name: 'articles' }" class="routerLink">
              <v-icon size=70 color="green accent-3">mdi-bulletin-board</v-icon>
            </router-link>
          </li>
        </ul>
      </div>
      <div class="col">
        <ul class="float-end row list-unstyled align-items-center">
          <li class="col">
            <v-dialog
              v-model="dialog"
              fullscreen
            >
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  fullscrean
                  elevation="0" 
                  color="#c9e5f5" 
                  width=60
                  height=60
                  v-bind="attrs"
                  v-on="on"
                  plain
                  :rounded='true'
                  :shaped='true'
                >
                  <v-icon size=70 color="green accent-3">mdi-magnify</v-icon>
                </v-btn>
              </template>
              <v-card color="rgba(26, 26, 26, 0.9)">
                <v-card-text>
                  <movie-search-view class="mt-3" @close-search="dialog=false" @cancle-dialog="dialog=false"></movie-search-view>
                </v-card-text>
              </v-card>
            </v-dialog>
          </li>
          <li v-if="!isLoggedIn"  class="col">
            <router-link :to="{ name: 'login' }" class="routerLink">
              <v-icon size=70 color="green accent-3">mdi-login</v-icon>
            </router-link>
          </li>
          <li v-if="!isLoggedIn"  class="col">
            <router-link :to="{ name: 'signup' }" class="routerLink">
              <v-icon size=70 color="green accent-3">mdi-account-plus</v-icon>  
            </router-link>
          </li>

          <li v-if="isLoggedIn"  class="col">
            <span @click="refreshAll">
              <router-link :to="{ name: 'profile', params: { username } }" class="routerLink">
                <v-icon size=70 color="green accent-3">mdi-account</v-icon>
                <!-- {{ currentUser.username }}'s page -->
              </router-link>
            </span>
          </li>
          <li v-if="isLoggedIn"  class="col">
            <router-link :to="{ name: 'logout' }"  class="routerLink">
              <v-icon size=70 color="green accent-3">mdi-logout</v-icon>
              </router-link>
          </li>
        </ul>
      </div>
    </div>

  </nav>
</template>

<script>
  import { mapGetters } from 'vuex'
  import MovieSearchView from '@/views/MovieSearchView.vue'
  export default {
    name: 'NavBar',
    data(){
      return{
        dialog: false,
        selected: null,
        options: [
          { value: null, text: '모든 연대' },
          { value: '2000s', text: '2000s' },
          { value: '1990s', text: '1990s' },
          { value: '1980s', text: '1980s' },
          { value: '1970s', text: '1970s' },
          
        ]
      }
    },
    components:{
      MovieSearchView,
    },
    methods: {
      refreshAll() {
      // 새로고침
      this.$router.go();
      }
    },
    computed: {
      ...mapGetters(['isLoggedIn', 'currentUser']),
      username() {
        return this.currentUser.username ? this.currentUser.username : 'guest'
      },
    },
  }
</script>

<style>
.routerLink {
  text-decoration: none;
  color: inherit;
}
.navbar {
  background-color: black;
}

</style>
