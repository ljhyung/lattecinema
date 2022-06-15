<template>
  <div class="row justify-content-center">
    <button disabled="disabled" class="btn btn-outline-success col-1">리뷰 작성</button>
    <form 
      @submit.prevent="onSubmit" class="review-list-form text-center">
      <div class="row justify-content-center">
        <label for="title" class="col-1 offset-1">title: </label>
        <input type="text" id="title" v-model="title" required class="col-1 border border-light">
        <label for="review" class="col-1">review: </label>
        <input type="text" id="review" v-model="content" required class="col-4 border border-light">
        <label for="rate" class="col-1">rate: </label>
        <star-rating class="col-1" inactive-color="#6ff294" :inline="true" :star-size="20" :show-rating="false" v-model="rate" :increment="0.5"></star-rating> 
      </div>
        <button class="btn btn-outline-success mt-3">등록</button>
    </form>
  </div>
</template>

<script>
import StarRating from 'vue-star-rating'
import { mapGetters, mapActions } from 'vuex'
export default {
  name: 'MovieReviewForm',
  components: { StarRating },
  data() {
    return {
      content: '',
      title: '',
      rate: '0',
    }
  },
  computed: {
    ...mapGetters(['movie', 'currentUser']),
  },
  methods: {
    ...mapActions(['createReview']),
    onSubmit() {
      this.createReview({ moviePk: this.movie.id, title:this.title, content: this.content, rate: this.rate*2})
    }
  }
}
</script>

<style>
.review-list-form {

  margin: 1rem;
  padding: 1rem;
}
</style>