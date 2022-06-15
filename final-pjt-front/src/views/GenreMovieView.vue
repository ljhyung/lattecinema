<template>
  <div class="bg-dark text-white">
      <div>
       <div class="d-flex flex-wrap">
          <div v-for="movie in genreMovie1" :key="movie.pk" class="col-12 col-sm-6 col-md-3 p-3">
            <div>
              <b-card
                :title="movie.title"
                :img-src='getSrc(movie.poster_path)'
                img-alt="Image"
                img-top
                tag="article"

                class="mb-2 cursor"
                @click="$router.push({ name: 'movie', params: {moviePk: movie.id} })"
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
  name: 'GenreMovieView',
  data() {
    return {
      genrePk: this.$route.params.genrePk,
    }
  },
  computed: {
    ...mapGetters(['movies', 'genreMovie1', 'trailer']),
    getSrc(){
      return (poster_path) => {
        if(poster_path!==null){
          return "https://www.themoviedb.org/t/p/w300_and_h450_bestv2" + `${poster_path}`
        }
        else{
          return require('@/assets/no_poster.png')
        }
      }
    }
  },
  methods: {
    ...mapActions(['fetchMovies', 'fetchGenreMovies', 'fetchMovieTrailer'])
  },
  created() {
    this.fetchGenreMovies(this.genrePk)
  },
}
</script>

<style>
.cursor {cursor: pointer;}
</style>