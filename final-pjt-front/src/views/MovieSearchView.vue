<template>
  <div class='container mt-5' style="max-width: 1000px;">
    <div class="row justify-content-center">
      <b-form-input autofocus style="max-width: 1000px" class="mt-5 border border-white text-decoration-none" type="text" v-model="keyword" @keyup="fetchSearchMovies(keyword)" @keyup.delete="fetchSearchMovies(keyword)" placeholder="영화 제목 입력"></b-form-input>
      <div class="d-flex flex-row justify-content-center mt-3">
        <v-btn variant="danger" @click="showResults=true" class="me-2">
          검색
        </v-btn>
        <v-btn @click="cancleDialog">
          취소
        </v-btn>
      </div>
        <ul><li>검색 결과가 없습니다</li></ul>
      <div v-if="showSearch">
        <div class="d-flex flex-wrap">
          <div v-for="movie in searchMovies" :key="movie.pk" class="col-12 col-sm-6 col-md-3 p-3">
            <b-card
              overlay
              :img-src='getSrc(movie.poster_path)'
              img-alt="Image"                
              tag="article"
              class="mb-2 cursor bg-secondary"
              @click="goToMovie(movie.id)"                
            >                
            </b-card>
          </div>
        </div>
      </div>
    </div>
  </div>
  
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'MovieSearchView',
  data(){
    return {
      keyword: '',
    }
  },
  computed: {
    ...mapGetters(['searchMovies', 'showSearch', 'fetchMovie', 'bridgePk']),
    getSrc(){
      return (poster_path) => {
        if (poster_path!==null){
          return "https://www.themoviedb.org/t/p/w300_and_h450_bestv2" + `${poster_path}`
        }
        else{
          return require('@/assets/no_poster.png')
        }
      }
    }
  },
  methods: {
    ...mapActions(['fetchSearchMovies', 'setBridgePk']),
    inputChange(input){
      this.keyword = input
    },
    cancleDialog() {
      this.$emit('cancle-dialog')
    },
    goToMovie(movieId){
      console.log(`select card ${movieId}`)
      this.setBridgePk(movieId)
      this.keyword= ''
      this.$emit('cancle-dialog')
      this.$router.push({ name: 'movie', params: {moviePk: movieId} })
      // this.fetchMovie(movieId)
    },
  },
}
</script>

<style>

</style>