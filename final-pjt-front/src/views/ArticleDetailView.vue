<template>
  <div class="container">
    <h1>{{ article.title }}</h1>
    <span>작성자: <router-link :to="{ name: 'profile', params: { username: article.user.username } }">
      {{ article.user.username }}
    </router-link></span>
    <hr>
    <p>
      {{ article.content }}
    </p>
    <!-- Article Edit/Delete UI -->
    <div v-if="isAuthor">
      <router-link :to="{ name: 'articleEdit', params: { articlePk } }">
        <button class="btn btn-secondary ">Edit</button>
      </router-link>
      |
      <button @click="deleteArticle(articlePk)" class="btn btn-danger ">Delete</button>
    </div>

    <!-- Article Like UI -->
    <div v-if="!isAuthor">
      Likeit:
      <button
        @click="likeArticle(articlePk)"
      >{{ likeCount }}</button>
    </div>

    <hr />
    <!-- Comment UI -->
    <comment-list :comments="article.comments"></comment-list>

    <hr>
      <router-link :to="{ name: 'articles' }">
        <button class="btn btn-primary">뒤로가기</button>
      </router-link>
    
  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  import CommentList from '@/components/CommentList.vue'


  export default {
    name: 'ArticleDetail',
    components: { CommentList },
    data() {
      return {
        articlePk: this.$route.params.articlePk,
      }
    },
    computed: {
      ...mapGetters(['isAuthor', 'article', 'isLogined']),
      likeCount() {
        return this.article.like_users?.length
      }
    },
    methods: {
      ...mapActions([
        'fetchArticle',
        'likeArticle',
        'deleteArticle',
      ]),
    },
    created() {
      this.fetchArticle(this.articlePk)
    },
    mounted(){
    },
  }
</script>

<style></style>
