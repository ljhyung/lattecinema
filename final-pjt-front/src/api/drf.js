const HOST = 'http://localhost:8000/api/v1/'

const ACCOUNTS = 'accounts/'
const ARTICLES = 'articles/'
const COMMENTS = 'comments/'
const MOVIES = 'movies/'

export default {
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    // Token 으로 현재 user 판단
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    // username으로 프로필 제공
    profile: username => HOST + ACCOUNTS + 'profile/' + `${username}/`,
    follow: username => HOST + ACCOUNTS + 'follow/' + `${username}/`,
  },
  articles: {
    // /articles/
    articles: () => HOST + ARTICLES,
    // /articles/1/
    article: articlePk => HOST + ARTICLES + `${articlePk}/`,
    likeArticle: articlePk => HOST + ARTICLES + `${articlePk}/` + 'like/',
    likeComment: (articlePk, commentPk) => HOST + ARTICLES + `${articlePk}/`+ COMMENTS + `${commentPk}/` + 'like/',
    comments: articlePk => HOST + ARTICLES + `${articlePk}/` + COMMENTS,
    comment: (articlePk, commentPk) =>
      HOST + ARTICLES + `${articlePk}/` + COMMENTS + `${commentPk}/`,
  },
  movies: {
    movies: () => HOST,
    search_movies: keyword => HOST + MOVIES + `search/${keyword}/`,
    genre_movie: genre_pk => HOST + MOVIES + `genre/${genre_pk}/`,
    genre_name: genre_pk => HOST + MOVIES + `genre/${genre_pk}/name/`,
    movie: moviePk => HOST + MOVIES + `${moviePk}/`,
    crew: moviePk => HOST + MOVIES + `${moviePk}/` + 'crew/',
    reviews: moviePk => HOST + MOVIES + `${moviePk}/` + 'reviews/',
    review: (moviePk, reviewPk) => HOST + MOVIES + `${moviePk}/` + 'reviews/' + `${reviewPk}/`,
    review_like: reviewPk => HOST + MOVIES  + 'reviews/' + `${reviewPk}/`,
    rate: moviePk => HOST + MOVIES + `${moviePk}/rate/`,
  },

}
