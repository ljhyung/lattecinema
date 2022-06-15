<template>
  <div class="container">
    <div class="review-list">
      <ul>
        <movie-review-item 
          v-for="(review,idx) in reviews" 
          :review="review" 
          :key="idx">
        </movie-review-item>        
      </ul>

      <movie-review-form v-if="is_review_wrote"></movie-review-form>
    </div>
  </div>
</template>

<script>
import MovieReviewItem from '@/components/MovieReviewItem.vue'
import MovieReviewForm from '@/components/MovieReviewForm.vue'
import { mapGetters } from 'vuex'


export default {
  name: 'MovieReviewList',
  components: { MovieReviewItem, MovieReviewForm },
  computed: {
    ...mapGetters(['currentUser']),
    is_review_wrote(){
      if (this.reviews!==undefined){
        for (const review of this.reviews) {
          if (review.user.pk===this.currentUser.pk) {
            return false
          }
        }
      }
      return true
    }
  },
  props: { reviews: Array },

}
</script>

<style>
.review-list {
  
  background-color: darkgray;
}
</style>