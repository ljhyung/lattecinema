<template>
  <div class="bg-dark text-white">
    <div>
      <section class="movie">
        <div class="movie__container" >
          <header class="movie__header" :class="{'movie__header--page': type=='page'}" :style="{ 'background-image': 'url(' + movieBackdropSrc + ')' }">
            <div class="movie__wrap movie__wrap--header" :class="{'movie__wrap--page': type=='page'}">
              <figure class="movie__poster">
                <img v-if="moviePosterSrc" class="movie__img" :src="moviePosterSrc" v-img="moviePosterSrc">
                <img v-if="!moviePosterSrc" class="movies-item__img is-loaded" src="@/assets/no_poster.png">
              </figure>
              <div class="movie__title">
                <h1 class="movie__title-text strong fs-1 fw-bold">
                  {{ movie.title }}                  
                  <span v-if="movie.tagline">{{ movie.tagline }}</span>
                </h1>
                <div>
                  <h2 class="movie__details-title">
                    Rate
                  </h2>
                  <div class="movie__details-text">
                      <star-rating :show-rating="false" :increment="0.01" :rating="starRating(movie.vote_average)" :read-only="true" :star-size="20"></star-rating>
                  </div>
                </div>
                <br>
                <div>
                  <h2 class="movie__details-title">
                    User Rate
                  </h2>
                  <div class="movie__details-text">
                      <star-rating :show-rating="false" :increment="0.01" :rating="starRating(userRate)" :read-only="true" :star-size="20" active-color="#6ff294"></star-rating>
                  </div>
                </div>
                <br>
                <v-icon large color="green accent-3" v-b-modal.modal-1 id="playButton" @click="fetchMovieTrailer(movie)">mdi-play-circle</v-icon>
                <span v-b-modal.modal-1 @click="fetchMovieTrailer(movie)">예고편 재생</span>
                <b-modal id="modal-1" :title="movie.title" size="xl" centered
                header-bg-variant="dark"
                header-text-variant="white"
                body-bg-variant="dark"
                body-text-variant="white"
                hide-footer="true"
                hide-header="true"
                >
                  <div v-if="trailer" class="iframebox">
                    <iframe :src="trailer" frameborder="0"></iframe>
                  </div>
                  <div v-if="!trailer">
                    <img src="@/assets/no_trailer.png" alt="no_trailer">
                  </div>
                </b-modal>
              </div>
            </div>
          </header>
          <div class="movie__main">
            <div class="movie__wrap movie__wrap--main" :class="{'movie__wrap--page': type=='page'}">
              <div class="movie__info">
                <div v-if="movie.overview" class="movie__description">
                  <h2 class="movie__details-title">
                      Overview
                  </h2>
                  {{ movie.overview }}
                </div>
                <div class="movie__details">
                  <div v-if="movie.genres.length" class="movie__details-block">
                    <h2 class="movie__details-title">
                      Genres
                    </h2>
                    <div class="movie__details-text">
                      {{ nestedDataToString(movie.genres) }}
                    </div>
                  </div>
                  <div v-if="movie.release_date" class="movie__details-block">
                    <h2 class="movie__details-title">
                      Release Date
                    </h2>
                    <div class="movie__details-text pb-5">{{movie.release_date}}</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
    <div id="review-list" class="">
      <movie-review-list :reviews="movie.movie_reviews"></movie-review-list>
    </div>
  </div>
</template>

<script>

import StarRating from 'vue-star-rating'
import { mapActions, mapGetters } from 'vuex'
import MovieReviewList from '@/components/MovieReviewList.vue'
export default {
  name: 'MovieDetailView',
  components: { MovieReviewList, StarRating },
  data() {
    return {
      // moviePk: this.$route.params.moviePk,
      check: require('@/assets/no_poster.png'),
      movieLoaded: false,
      moviePosterSrc: '',
      movieBackdropSrc: '',
      moviePk : this.$route.params.moviePk
    }
  },
  computed: {
    ...mapGetters(['movie', 'crew', 'trailer', 'userRate', 'bridgePk']),
    // moviePk(){
    //   return this.$route.params.moviePk
    // },
    movieGenre(){
      return (GenreList) => {
        const res = []
        for (const gen of GenreList){
          res.push(gen.name)
        }
        return res
      }
    },
    starRating(){
      return (rating) => {
        return  rating/2
      }
    }
  },
  watch: {
    movie(){
      this.moviePk = this.$route.params.moviePk
      console.log(this.moviePk)
    }
  },
  methods: {
    ...mapActions(['fetchMovie', 'fetchCrew', 'fetchMovieTrailer', 'fetchUserRate']),
    fetchPage(){
          this.poster();
          this.backdrop();
          // Change Page title
          document.title = this.movie.title
    },
    getMoviePk(){
      this.moviePk = this.$route.params.moviePk
    },
    poster() {
      if(this.movie.poster_path!==null){
        this.moviePosterSrc = 'https://image.tmdb.org/t/p/w600_and_h900_bestv2' + this.movie.poster_path;
      }
      else{
        this.moviePosterSrc = require('@/assets/no_poster.png')
      }
    },
    backdrop(){
      if(this.movie.backdrop_path){
        this.movieBackdropSrc = 'https://image.tmdb.org/t/p/w500' + this.movie.backdrop_path;
      }
    },
    nestedDataToString(data) {
      let nestedArray = [], resultString;
      data.forEach((item) => nestedArray.push(item.name));
      resultString = nestedArray.join(', ');
      return resultString;
    },
  },
  created() {
    this.fetchMovie(this.moviePk)
    this.fetchPage()
    this.fetchCrew(this.moviePk)
    this.fetchUserRate(this.moviePk)
    this.fetchMovieTrailer(this.movie)
    console.log(`created ${this.moviePk}`)
  },
  mounted(){
    this.fetchPage()
    console.log(`moounted ${this.moviePk}`)
  },
  updated(){
    // this.fetchPage()
    console.log(`updated ${this.moviePk}`)
  },
  // after(){
  //   // this.fetchPage()
  //   this.fetchMovieTrailer(this.movie)
  //   console.log(`after ${this.moviePk}`)
  // },
  beforeRouteUpdate(){
    this.fetchMovie(this.bridgePk)
    this.fetchPage()
    console.log('이동 시 실행')
    console.log(this.$route.params.moviePk)
  }
}
</script>

<style lang="scss">
.review-list {
  
  background-color: gainsboro;
}
@import "./src/scss/variables";
@import "./src/scss/media-queries";
.iframebox {
  position: relative;
  width: 100%;
  padding-bottom: 56.25%;
}
.iframebox iframe {
  position: absolute;
  width: 100%;
  height: 100%;
}



.movie{
  &__wrap{
    display: flex;
    &--page{
      max-width: 768px;
      position: relative;
      margin: 0 auto;
    }
    &--header{
      align-items: center;
      height: 100%;
    }
    &--main{
      display: flex;
      flex-wrap: wrap;
      flex-direction: column;
      background: rgba($c-dark, 0.85);
      @include tablet-min{
        flex-direction: row;
      }
    }
  }
  &__header{
    height: 250px;
    position: relative;
    background-size: cover;
    background-repeat: no-repeat;
    background-position: 50% 50%;
    background-color: $c-dark;
    @include tablet-min{
      height: 350px;
      &--page{
        height: 384px;
      }
    }
    &:before{
      content: "";
      display: block;
      position: absolute;
      top: 0;
      left: 0;
      z-index: 0;
      width: 100%;
      height: 100%;
      background: rgba($c-dark, 0.85);
    }
  }
    &__poster{
      display: none;
      @include tablet-min{
        background: $c-dark;
        display: block;
        position: absolute;
        width: 20%;
        top: 40px;
        left: 380px;
      }
    }
      &__img{
        display: block;
        width: 100%;
        // opacity: 0;
        transform: scale(0.97) translateZ(0);
        transition: opacity 0.5s ease, transform 0.5s ease;
        opacity: 1;
        transform: scale(1);
      }
    &__title{
      position: relative;
      padding: 20px;
      color: $c-green;
      text-align: center;
      width: 100%;
      @include tablet-min{
        width: 55%;
        text-align: left;
        margin-left: 45%;
        padding: 30px 30px 30px 40px;
      }
      &-text{
        font-weight: 500;
        line-height: 1.4;
        font-size: 24px;
        @include tablet-min{
          font-size: 30px;
        }
        span{
          display: block;
          font-size: 14px;
          font-weight: 300;
          color: rgba($c-white, 0.7);
          margin-top: 10px;
        }
      }
    }
  &__main{
    background: $c-light;
    min-height: calc(100vh - 250px);
    @include tablet-min{
      min-height: 0;
    }
  }
    &__actions{
      text-align: center;
      width: 100%;
      order: 2;
      padding: 20px;
      border-top: 1px solid rgba($c-dark, 0.05);
      @include tablet-min{
        order: 1;
        width: 45%;
        padding: 185px 0 40px 40px;
        border-top: 0;
      }
      &-link{
        display: flex;
        align-items: center;
        text-decoration: none;
        text-transform: uppercase;
        color: rgba($c-dark, 0.5);
        transition: color 0.5s ease;
        font-size: 11px;
        padding: 10px 0;
        border-bottom: 1px solid rgba($c-dark, 0.05);
        &:hover{
          color: rgba($c-dark, 0.75);
        }
        &.active{
          color: $c-dark;
        }
      }
      &-icon{
        width: 16px;
        height: 16px;
        margin: 0 10px 0 0;
        fill: rgba($c-dark, 0.5);
        transition: fill 0.5s ease, transform 0.5s ease;
        &.waiting{
          transform: scale(0.8, 0.8);
        }
      }
      &-link:hover &-icon{
        fill: rgba($c-dark, 0.75);
      }
      &-link.active &-icon{
        fill: $c-green;
      }
      &-text{
        display: block;
        padding-top: 2px;
      }
    }
    &__info{
      width: 100%;
      padding: 20px;
      order: 1;
      @include tablet-min{
        order: 2;
        padding: 40px;
        width: 55%;
        margin-left: 45%;
      }
    }
    &__actions + &__info{
      margin-left: 0;
    }
      &__description{
        font-weight: 300;
        font-size: 13px;
        line-height: 1.8;
        margin-bottom: 20px;
        @include tablet-min{
          margin-bottom: 30px;
          font-size: 14px;
        }
      }
      &__details{
        &-block:not(:last-child){
          margin-bottom: 20px;
          @include tablet-min{
            margin-bottom: 30px;
          }
        }
        &-title{
          margin: 0;
          font-weight: 400;
          text-transform: uppercase;
          font-size: 14px;
          color: $c-green;
          @include tablet-min{
            font-size: 16px;
          }
        }
        &-text{
          font-weight: 300;
          font-size: 14px;
          margin-top: 5px;
        }
      }
}



</style>