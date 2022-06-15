<template>
  <div class="comment-list">
    <div class="card mb-2">
      <div class="card-header bg-light">
        <i class="fa fa-comment fa"></i> 댓글
      </div>
      <div class="card-body">
        <ul class="list-group list-group-flush">
          <comment-list-item 
            v-for="comment in comments" 
            :comment="comment" 
            :key="comment.pk">
          </comment-list-item>        
        </ul>
        <ul class="list-group list-group-flush">
            <!-- <li class="list-group-item">
              <div class="form-inline mb-2">
                <label for="replyId"><i class="fa fa-user-circle-o fa-2x"></i></label>
                <input type="text" class="form-control ml-2" placeholder="Enter yourId" id="replyId">
                <label for="replyPassword" class="ml-4"><i class="fa fa-unlock-alt fa-2x"></i></label>
                <input type="password" class="form-control ml-2" placeholder="Enter password" id="replyPassword">
              </div>
              <textarea class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
              
            </li> -->
        </ul>
      </div>
      <comment-list-form></comment-list-form>
    </div>

  </div>
</template>

<script>
import CommentListItem from '@/components/CommentListItem.vue'
import CommentListForm from '@/components/CommentListForm.vue'
// import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'CommentList',
  components: { CommentListForm, CommentListItem },
  props: { comments: Array },
}
</script>

<style>
/* .comment-list {
  border: 1px solid blue;
} */
</style>