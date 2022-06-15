<template>
  <div class="justify-content-center bg-dark text-white">
    <div class="container">
      <h1 class="text-center">오늘의 영화</h1>
      <div class="container">
        <div class="justify-content-center">
          <div v-if="trailer" class="iframebox">
            <iframe :src="trailer" frameborder="0"></iframe>
          </div>
          <div v-if="!trailer">
            <img src="@/assets/no_trailer.png" alt="no_trailer" width="400">
          </div>
          <!-- <div class="iframebox ">
            <iframe :src="trailer" frameborder="0"></iframe>
          </div> -->
        </div>

      </div>

      <div class="justify-content-center ">
        <div class="container row" >
          <div v-for="movie in dailyMovie" :key="movie.pk"  class="col-12 col-sm-6 col-md-3 p-1">
            <div class="g-3">
              <b-card
                bg-variant="dark" text-variant="white"
                :title="movie.title"
                :img-src='getSrc(movie.poster_path)'
                img-alt="Image"
                img-top
                tag="article"
                class="mb-2 cursor text-center"
                @click="$router.push({ name: 'movie', params: {moviePk: movie.id} })"
              >
                <!-- <b-button href="#" variant="primary">Go somewhere</b-button> -->
              </b-card>
            </div>
          </div>
        </div>
      </div>
      
      <!-- <ul>
        <li v-for="movie in dailyMovie" :key="movie.pk">
          <router-link 
            :to="{ name: 'movie', params: {moviePk: movie.id} }">
            {{ movie.title }}
          </router-link>
        
        </li>
      </ul> -->
    </div>
    <hr>
    <div class="container">
      <h3>{{ genreName[0] }}</h3>
      <router-link :to="{ name: 'genremovies', params: {genrePk: genre[0]} }" class="text-decoration-none">
        더보기
      </router-link>
      <div class="justify-content-center ">
        <div class="container row" >
          <div v-for="movie in genreMovie1Four" :key="movie.pk"  class="col-12 col-sm-6 col-md-3 p-1">
            <div class="g-3 bg-dark">
              <b-card
                bg-variant="dark" text-variant="white"
                :title="movie.title"
                :img-src='getSrc(movie.poster_path)'
                img-alt="Image"
                img-top
                tag="article"
                class="mb-2 cursor text-center"
                @click="$router.push({ name: 'movie', params: {moviePk: movie.id} })"
              >
                <!-- <b-button href="#" variant="primary">Go somewhere</b-button> -->
              </b-card>
            </div>
          </div>
        </div>
      </div>
    </div>


    <div class="container">
      <h3>{{ genreName[1] }}</h3>
      <router-link :to="{ name: 'genremovies', params: {genrePk: genre[1]} }" class="text-decoration-none">
        더보기
      </router-link>
      <div class="justify-content-center ">
        <div class="container row" >
          <div v-for="movie in genreMovie2Four" :key="movie.pk"  class="col-12 col-sm-6 col-md-3 p-1">
            <div class="g-3">
              <b-card
                bg-variant="dark" text-variant="white"
                :title="movie.title"
                :img-src='getSrc(movie.poster_path)'
                img-alt="Image"
                img-top
                tag="article"
                class="mb-2 cursor text-center"
                @click="$router.push({ name: 'movie', params: {moviePk: movie.id} })"
              >
                <!-- <b-button href="#" variant="primary">Go somewhere</b-button> -->
              </b-card>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!--  -->
    <div class="container">
      <h3>{{ genreName[2] }}</h3>
      <router-link :to="{ name: 'genremovies', params: {genrePk: genre[2]} }" class="text-decoration-none">
        더보기
      </router-link>
      <div class="justify-content-center ">
        <div class="container row" >
          <div v-for="movie in genreMovie3Four" :key="movie.pk"  class="col-12 col-sm-6 col-md-3 p-1">
            <div class="g-3">
              <b-card
                bg-variant="dark" text-variant="white"
                :title="movie.title"
                :img-src='getSrc(movie.poster_path)'
                img-alt="Image"
                img-top
                tag="article"
                class="mb-2 cursor text-center"
                @click="$router.push({ name: 'movie', params: {moviePk: movie.id} })"
              >
                <!-- <b-button href="#" variant="primary">Go somewhere</b-button> -->
              </b-card>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!--  -->
    <div class="container">
      <h3>{{ genreName[3] }}</h3>
      <router-link :to="{ name: 'genremovies', params: {genrePk: genre[3]} }" class="text-decoration-none">
        더보기
      </router-link>
      <div class="justify-content-center ">
        <div class="container row" >
          <div v-for="movie in genreMovie4Four" :key="movie.pk"  class="col-12 col-sm-6 col-md-3 p-1">
            <div class="g-3">
              <b-card
                bg-variant="dark" text-variant="white"
                :title="movie.title"
                :img-src='getSrc(movie.poster_path)'
                img-alt="Image"
                img-top
                tag="article"
                class="mb-2 cursor text-center"
                @click="$router.push({ name: 'movie', params: {moviePk: movie.id} })"
              >
                <!-- <b-button href="#" variant="primary">Go somewhere</b-button> -->
              </b-card>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!--  -->
  </div>
</template>

<script>
import axios from 'axios'
import drf from '@/api/drf'
import _ from 'lodash'
import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'MovieListView',
  data(){
    return {
      genre: _.sampleSize([12,14,16,18,27,28,35,36,37,53,80,99,878,9648,10402,10749,10751,10752,10770],4),
      genreName: [],
    }
  },
  computed: {
    ...mapGetters(['movies', 'dailyMovie', 'genreMovie1', 'genreMovie2', 'genreMovie3', 'genreMovie4', 'trailer', 'authHeader']),
    genreMovie1Four(){
      return _.sampleSize(this.genreMovie1,4)
      // return this.genreMovie1.slice(0,4)
    },
    genreMovie2Four(){
      return _.sampleSize(this.genreMovie3,4)
    },
    genreMovie3Four(){
      return _.sampleSize(this.genreMovie3,4)
    },
    genreMovie4Four(){
      return _.sampleSize(this.genreMovie4,4)
    },
    getSrc(){
      return (poster_path) => {
        if (poster_path!==null){
          return "https://www.themoviedb.org/t/p/w300_and_h450_bestv2" + `${poster_path}`
        }
        else{
          this.moviePosterSrc = require('@/assets/no_poster.png')
        }
      }
    }
  },
  methods: {
    ...mapActions(['fetchMovies', 'fetchDailyMovie', 'fetchGenreMovies', 'fetchGenreMovies2', 'fetchGenreMovies3', 'fetchGenreMovies4', 'fetchMovieTrailer']),
    getGenreName(genreNum){
      axios({
        url: drf.movies.genre_name(genreNum),
        method: 'get',
        headers: this.authHeader,
      })
        .then(res => {
          this.genreName.push(res.data[0].name)
          // commit('SET_GENRE_MOVIES', res.data)
          })
        .catch(err => console.error(err.response))
    },
    makeTitle(){
      document.title = 'Latte cinema'
    }
  },
  created() {
    // this.fetchMovies()
    this.fetchDailyMovie()
    this.fetchGenreMovies(this.genre[0])
    this.fetchGenreMovies2(this.genre[1])
    this.fetchGenreMovies3(this.genre[2])
    this.fetchGenreMovies4(this.genre[3])
    this.getGenreName(this.genre[0])
    this.getGenreName(this.genre[1])
    this.getGenreName(this.genre[2])
    this.getGenreName(this.genre[3])
  },
  mounted(){
    this.fetchMovieTrailer(this.dailyMovie[0])
    this.makeTitle()
  }
    
}
</script>

<style>
.cursor {cursor: pointer;}
html {
  overflow: hidden !important;
  scrollbar-width: none;
  -ms-overflow-style: none;
}

html::-webkit-scrollbar {
  width: 0;
  height: 0;
}
</style>