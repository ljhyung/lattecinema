import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'

import _ from 'lodash'
// import accounts from './accounts'

export default {
  // namespaced: true,
  state: {
    movies: [],
    searchMovies: [],
    movie: {},
    dailyMovie: [],
    genreMovie1: [],
    genreMovie2: [],
    genreMovie3: [],
    genreMovie4: [],
    crew: {},
    trailer: [],
    reviews: [],
    showSearch: false,
    userRate: 0,
    bridgePk: null,
  },

  getters: {
    movies: state => state.movies,
    searchMovies: state => state.searchMovies,
    movie: state => state.movie,
    dailyMovie: state => state.dailyMovie,
    crew: state => state.crew,
    trailer: state => state.trailer,
    genreMovie1: state => state.genreMovie1,
    genreMovie2: state => state.genreMovie2,
    genreMovie3: state => state.genreMovie3,
    genreMovie4: state => state.genreMovie4,
    showSearch: state => state.showSearch,
    userRate: state => state.userRate,
    bridgePk: state => state.bridgePk,
    
    // isAuthor: (state, getters) => {
    //   return state.article.user?.username === getters.currentUser.username
    // },
  },

  mutations: {
    SET_MOVIES: (state, movies) => state.genreMovie1 = movies,
    SET_SEARCH_MOVIES: (state, searchMovies) => state.searchMovies = searchMovies,
    SET_GENRE_MOVIES: (state, movies) => state.genreMovie1 = movies,
    SET_GENRE_MOVIES2: (state, movies) => state.genreMovie2 = movies,
    SET_GENRE_MOVIES3: (state, movies) => state.genreMovie3 = movies,
    SET_GENRE_MOVIES4: (state, movies) => state.genreMovie4 = movies,
    SET_MOVIE: (state, movie) => state.movie = movie[0],
    // SET_MOVIE_COMMENTS: (state, comments) => (state.movie.comments = comments),
    SET_DAILY_MOVIE: (state, dailyMovie) => state.dailyMovie = dailyMovie,
    SET_CREW: (state, crew) => state.crew = crew[0],
    SET_TRAILIER: (state, trailer) => state.trailer = trailer,
    SET_MOVIE_REVIEWS: (state, reviews) => (state.movie.movie_reviews = reviews),
    SET_SHOW_SEARCH: (state, showSearch) => state.showSearch = showSearch,
    SET_USER_RATE: (state, userRate) => state.userRate = userRate,
    SET_BRIDGE_PK: (state, bridgePk) => state.bridgePk = bridgePk,
    
  },

  actions: {
    fetchMovies({ commit, getters }) {
      /* ????????? ?????? ????????????
      GET: articles URL (token)
        ????????????
          ???????????? ?????? ??????????????? state.articles??? ??????
        ????????????
          ?????? ????????? ??????
      */
      axios({
        url: drf.movies.movies(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_MOVIES', res.data))
        .catch(err => console.error(err.response))
    },
    fetchGenreMovies({ commit, getters }, genre_pk) {
      axios({
        url: drf.movies.genre_movie(genre_pk),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          // console.log(res.data)
          commit('SET_GENRE_MOVIES', res.data)})
        .catch(err => console.error(err.response))
    },
    fetchGenreMovies2({ commit, getters }, genre_pk) {
      axios({
        url: drf.movies.genre_movie(genre_pk),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          // console.log(res.data)
          commit('SET_GENRE_MOVIES2', res.data)})
        .catch(err => console.error(err.response))
    },
    fetchGenreMovies3({ commit, getters }, genre_pk) {
      axios({
        url: drf.movies.genre_movie(genre_pk),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          // console.log(res.data)
          commit('SET_GENRE_MOVIES3', res.data)})
        .catch(err => console.error(err.response))
    },
    fetchGenreMovies4({ commit, getters }, genre_pk) {
      axios({
        url: drf.movies.genre_movie(genre_pk),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          // console.log(res.data)
          commit('SET_GENRE_MOVIES4', res.data)})
        .catch(err => console.error(err.response))
    },
    fetchSearchMovies({ commit, getters }, keyword) {
      console.log(keyword)
      // if (keyword==='')
      axios({
        url: drf.movies.search_movies(keyword),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_SHOW_SEARCH', true)
          commit('SET_SEARCH_MOVIES', res.data)})
        .catch(err => {
          commit('SET_SHOW_SEARCH', false)
          console.error(err.response)})
    
    },
    fetchMovie({ commit, getters }, moviePk) {
      axios({
        url: drf.movies.movie(moviePk),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_MOVIE', res.data)
        //   console.log(res.data)
        //   const keyword = res.data[0].title
        //   console.log(keyword)
        //   const API_URL = 'https://www.googleapis.com/youtube/v3/search'
        //   const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
        //   axios({
        //     method: 'get',
        //     url: API_URL,
        //     params: {
        //       part: 'snippet',
        //       key: API_KEY,
        //       q: keyword + ' official trailer',
        //       type: 'video',
        //     }
        //   })
        //     .then(res => {
        //       // console.log(res.data.items)
        //       console.log(`https://www.youtube.com/embed/${res.data.items[0].id.videoId}`)
        //       commit('SET_TRAILIER', `https://www.youtube.com/embed/${res.data.items[0].id.videoId}?autoplay=1&mute=1&modestbranding=1&amp;playlist=${res.data.items[0].id.videoId}&loop=1`)})
        //     .catch(err => {
        //       console.error(err.response)
        //       if (err.response.status === 404) {
        //         router.push({ name: 'NotFound404' })
        //       }
        //     })
        // })
        // .catch(err => {
        //   console.error(err.response)
        //   if (err.response.status === 404) {
        //     router.push({ name: 'NotFound404' })
        //   }
        })
    },
    fetchUserRate({ commit, getters }, moviePk) {
      axios({
        url: drf.movies.rate(moviePk),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_USER_RATE', res.data.rate.rate__avg)
        })
    },
    fetchMovieTrailer({ commit }, movie) {
      console.log('!!!!!!!!!!!')
      console.log(movie.trailer)
      if (movie.trailer!==null){
        commit('SET_TRAILIER', `https://www.youtube.com/embed/${movie.trailer.key}`)
      }
      else{
        commit('SET_TRAILIER', null)
      }
    },

    fetchDailyMovie({ commit, getters }) {
      axios({
        url: drf.movies.movies(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          console.log('!!')
          // const lst = [12,14,16,18,27,28,35,36,37,53,80,99,878,9648,10402,10749,10751,10752,10770]
          const toData = _.sampleSize(res.data, 4)
          // console.log(toData)
          commit('SET_DAILY_MOVIE', toData)
        })
        .catch(err => console.error(err.response))
    },

    fetchCrew({ commit, getters }, moviePk) {
      axios({
        url: drf.movies.crew(moviePk),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          // console.log(res.data)
          commit('SET_CREW', res.data)})
        .catch(err => {
          console.error(err.response)
          if (err.response.status === 404) {
            router.push({ name: 'NotFound404' })
          }
        })
    },
    // createArticle({ commit, getters }, article) {
    //   /* ????????? ??????
    //   POST: articles URL (????????? ????????????, token)
    //     ????????????
    //       ???????????? ?????? ???????????? state.article??? ??????
    //       ArticleDetailView ??? ??????
    //     ????????????
    //       ?????? ????????? ??????
    //   */
      
    //   axios({
    //     url: drf.articles.articles(),
    //     method: 'post',
    //     data: article,
    //     headers: getters.authHeader,
    //   })
    //     .then(res => {
    //       commit('SET_ARTICLE', res.data)
    //       router.push({
    //         name: 'article',
    //         params: { articlePk: getters.article.pk }
    //       })
    //     })
    // },

    // updateArticle({ commit, getters }, { pk, title, content}) {
    //   /* ????????? ??????
    //   PUT: article URL (????????? ????????????, token)
    //     ????????????
    //       ???????????? ?????? ???????????? state.article??? ??????
    //       ArticleDetailView ??? ??????
    //     ????????????
    //       ?????? ????????? ??????
    //   */
    //   axios({
    //     url: drf.articles.article(pk),
    //     method: 'put',
    //     data: { title, content },
    //     headers: getters.authHeader,
    //   })
    //     .then(res => {
    //       commit('SET_ARTICLE', res.data)
    //       router.push({
    //         name: 'article',
    //         params: { articlePk: getters.article.pk }
    //       })
    //     })
    // },

    // deleteArticle({ commit, getters }, articlePk) {
    //   /* ????????? ??????
    //   ???????????? ????????? ??????
    //     DELETE: article URL (token)
    //       ????????????
    //         state.article ?????????
    //         AritcleListView??? ??????
    //       ????????????
    //         ?????? ????????? ??????
    //   */
      
    //   if (confirm('?????? ?????????????????????????')) {
    //     axios({
    //       url: drf.articles.article(articlePk),
    //       method: 'delete',
    //       headers: getters.authHeader,
    //     })
    //       .then(() => {
    //         commit('SET_ARTICLE', {})
    //         router.push({ name: 'articles' })
    //       })
    //       .catch(err => console.error(err.response))
    //   }
    // },

    // likeArticle({ commit, getters }, articlePk) {
    //   /* ?????????
    //   POST: likeArticle URL(token)
    //     ????????????
    //       state.article ??????
    //     ????????????
    //       ?????? ????????? ??????
    //   */
    //   axios({
    //     url: drf.articles.likeArticle(articlePk),
    //     method: 'post',
    //     headers: getters.authHeader,
    //   })
    //     .then(res => commit('SET_ARTICLE', res.data))
    //     .catch(err => console.error(err.response))
    // },

		createReview({ commit, getters }, { moviePk, title, content, rate }) {
      /* ?????? ??????
      POST: comments URL(?????? ?????? ??????, token)
        ????????????
          ???????????? state.article??? comments ??????
        ????????????
          ?????? ????????? ??????
      */
      const like  =false
      const review = { title, content, rate, like }

      axios({
        url: drf.movies.reviews(moviePk),
        method: 'post',
        data: review,
        headers: getters.authHeader,
      })
        .then(res => {
          console.log(res.data)
          commit('SET_MOVIE_REVIEWS', res.data)
        })
        .catch(err => {
          console.log('here')
          console.log(review)
          console.error(err.response)})
    },

    updateReview({ commit, getters }, { moviePk, reviewPk, title, content, rate, user_liked }) {
      /* ?????? ??????
      PUT: comment URL(?????? ?????? ??????, token)
        ????????????
          ???????????? state.article??? comments ??????
        ????????????
          ?????? ????????? ??????
      */
      const like  =false
      const review = { title, content, rate, like, user_liked }

      axios({
        url: drf.movies.review(moviePk, reviewPk),
        method: 'put',
        data: review,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_MOVIE_REVIEWS', res.data)
        })
        .catch(err => console.error(err.response))
    },

    deleteReview({ commit, getters }, { moviePk, reviewPk }) {
      /* ?????? ??????
      ???????????? ????????? ??????
        DELETE: comment URL (token)
          ????????????
            ???????????? state.article??? comments ??????
          ????????????
            ?????? ????????? ??????
      */
        if (confirm('?????? ?????????????????????????')) {
          axios({
            url: drf.movies.review(moviePk, reviewPk),
            method: 'delete',
            data: {},
            headers: getters.authHeader,
          })
            .then(res => {
              commit('SET_MOVIE_REVIEWS', res.data)
            })
            .catch(err => console.error(err.response))
        }
      },

      reviewLike({ getters }, reviewPk) {
        /*
        GET: profile URL??? ???????????????
          ????????????
            state.profile??? ??????
        */
        console.log(reviewPk)
        axios({
          url: drf.movies.review_like(reviewPk),
          method: 'post',
          headers: getters.authHeader,
        })
          .then(res => {
            // commit('SET_FOLLOW', res.data)
            console.log(res.data.review_liked)

          })
      },

      setBridgePk({ commit }, { moviePk }){
        commit('SET_BRIDGE_PK', moviePk)
      }
  },
}
