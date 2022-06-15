import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

import articles from './modules/articles'
import accounts from './modules/accounts'
import movies from './modules/movies'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  modules: { accounts, articles, movies },
})
