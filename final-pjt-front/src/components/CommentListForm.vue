<template>
  <form @submit.prevent="onSubmit" class="comment-list-form">
    <!-- <label for="comment">comment: </label>
    <input type="text" id="comment" v-model="content" required>
    <button>Comment</button> -->
    <p>작성자 : {{ currentUser.username }}</p>
    <b-form-textarea
      id="comment"
      v-model="content"
      placeholder="댓글 내용을 작성해 주세요..."
      rows="2"
      max-rows="5"
    ></b-form-textarea>
    <button class="btn btn-dark mt-3" onClick="">post reply</button>
  </form>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommentListForm',
  data() {
    return {
      content: ''
    }
  },
  computed: {
    ...mapGetters(['article', 'currentUser']),
  },
  methods: {
    ...mapActions(['createComment']),
    onSubmit() {
      this.createComment({ articlePk: this.article.pk, content: this.content, })
      this.content = ''
    }
  }
}
</script>

<style>
.comment-list-form {
  /* border: 1px solid black; */
  margin: 1rem;
  padding: 1rem;
}
</style>