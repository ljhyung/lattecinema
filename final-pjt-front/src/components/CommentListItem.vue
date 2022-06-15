<template>
  <li class="list-group-item">
    <router-link :to="{ name: 'profile', params: { username: comment.user.username } }">
      {{ comment.user.username }}
    </router-link>: 
    
    <span v-if="!isEditing">{{ payload.content }}</span>

    <span v-if="isEditing">
      <input type="text" v-model="payload.content">
      <button @click="onUpdate">Update</button> |
      <button @click="switchIsEditing">Cancle</button>
    </span>

    <span v-if="currentUser.username !== comment.user.username && !isEditing">
      <button @click="likeComment(payload)">좋아요!</button> 
      <span>{{ commentLikeCount }}</span>
      <!-- <button @click="likeComment(payload)" v-if="commentLikeCount == '1'">좋아요 취소!!</button>  -->
      <!-- <span>따흐기</span> -->
    </span>

    <span v-if="currentUser.username === comment.user.username && !isEditing">
      <button class="btn btn-secondary" @click="switchIsEditing">Edit</button> |
      <button class="btn btn-danger" @click="deleteComment(payload)">Delete</button>
    </span>

  </li>
</template>

<script>
import axios from 'axios'
import { mapGetters, mapActions ,mapMutations } from 'vuex'
import drf from '@/api/drf'


export default {
  name: 'CommentListItem',
  props: { comment: Object },
  data() {
    return {
      isEditing: false,
      payload: {
        articlePk: this.comment.article,
        commentPk: this.comment.pk,
        content: this.comment.content,
      },
      ACCOUNTS: 'accounts/',
      ARTICLES: 'articles/',
      COMMENTS: 'comments/',
      MOVIES: 'movies/',
      commentLikeCount: '0',
    }
  },
  computed: {
    ...mapGetters(['currentUser', 'article','authHeader']),
  },
  methods: {
    ...mapMutations(['SET_ARTICLE_COMMENTS']),
    ...mapActions(['updateComment', 'deleteComment',]),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.updateComment(this.payload)
      this.isEditing = false
    },
    likeComment() {
      axios({
        url: drf.articles.likeComment(this.payload.articlePk, this.payload.commentPk),
        method: 'post',
        headers: this.authHeader,
      })
      .then(res => {
        this.commentLikeCount = res.data['user_liked'].length
      })  
      .catch(err => console.error(err))
    }
  },
  created() {
    this.commentLikeCount = this.comment['user_liked'].length
  }
}
</script>

<style>
.comment-list-item {
  border: 1px solid green;

}
</style>
