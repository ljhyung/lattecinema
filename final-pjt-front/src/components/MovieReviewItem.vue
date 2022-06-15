<template>
  <div>
    <li style="list-style: none;">
      <router-link :to="{ name: 'profile', params: { username: review.user.username } }" class="text-decoration-none">
        {{ review.user.username }}
      </router-link>
      <span v-if="!isEditing">제목: {{ payload.title }} | 리뷰 : {{ payload.content }} |
         </span>
        <p>
          <star-rating active-color="#6ff294" :read-only="true" :inline="true" :star-size="20" :show-rating="false" v-model="payload.rate" :increment="0.5"></star-rating>
        </p>
      <p>
        <button v-if="!isLikedBool" @click="triggerReviewLike(review.id)">리뷰 좋아요</button>
        <button v-if="isLikedBool" @click="triggerReviewLike(review.id)">리뷰 좋아요 취소</button>
        {{userReviewLikedCount}}
      </p>
      <span v-if="isEditing">
        <label for="title">title: </label>
        <input type="text" id="title" v-model="payload.title" required>
        <label for="review">review: </label>
        <input type="text" id="review" v-model="payload.content" required>
        <label for="rate">rate: </label>
        <star-rating active-color="#6ff294" :inline="true" :star-size="20" :show-rating="false" v-model="payload.rate" :increment="0.5"></star-rating> 
        <button @click="onUpdate">Update</button> |
        <button @click="switchIsEditing">Cancle</button>
      </span>

      <span v-if="currentUser.username === review.user.username && !isEditing">
        <button @click="switchIsEditing">Edit</button> |
        <button @click="deleteReview(payload)">Delete</button>
      </span>
    </li>
    <hr>
  </div>
</template>

<script>
import StarRating from 'vue-star-rating'
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'MovieReviewItem',
  props: { review: Object },
  components: { StarRating },
  data() {
    return {
      isEditing: false,
      payload: {
        moviePk: this.review.movie,
        reviewPk: this.review.id,
        title: this.review.title,
        content: this.review.content,
        rate: this.review.rate/2,
      },
      isLikedBool:false,
      userReviewLikedCount: 0,
    }
  },
  computed: {
    ...mapGetters(['currentUser']),
    
  },
  methods: {
    ...mapActions(['updateReview', 'deleteReview', 'reviewLike']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.updateReview(this.payload)
      this.isEditing = false
    },
    triggerReviewLike(reviewId){
      this.isLikedBool = !this.isLikedBool
      this.reviewLike(reviewId)
    }, 
    isLiked(){
      if (this.review.user_review_liked!==undefined){
        for (const liker of this.review.user_review_liked) {
          if (liker.pk===this.currentUser.pk) {
            this.isLikedBool =  false
          }
        }
        this.isLikedBool = true
      } else{
      this.isLikedBool = true
      }
    },

  },
  created(){
    this.isLiked
    this.userReviewLikedCount = this.review.user_review_liked.length
  }

}
</script>

<style>

</style>