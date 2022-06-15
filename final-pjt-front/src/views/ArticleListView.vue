<template>
  <div class="container">
    <br>
    <h1>Community</h1>
    <br>
    <!-- <div>{{ items }}</div> -->
    <!-- <router-link :to="{ name: 'article' }">최신순</router-link> | 
    <router-link :to="{ name: 'articleLike' }">인기순</router-link> -->

    <!-- <ul>
      <li v-for="article in articles" :key="article.pk">
        <router-link 
          :to="{ name: 'article', params: {articlePk: article.pk} }">
          {{ article.title }}
        </router-link>
        ({{ article.comment_count }})  ♥{{ article.like_count }}
        작성자: {{ article.user.username }}
      </li>
    </ul> -->

        <!-- 작성자 -->
        <!-- 글 이동 링크 (제목) -->
        <!-- 댓글 개수/좋아요 개수 -->
    <!-- id="my-table" -->


    <!-- <b-table
      :items="items"
      :per-page="perPage"
      :current-page="currentPage"
      small
      :fields="fields"
      hover
      striped
    >
    </b-table> -->
<!-- 
    <b-pagination
      v-model="currentPage"
      :total-rows="items.length"
      :per-page="perPage"
      first-text="First"
      prev-text="Prev"
      next-text="Next"
      last-text="Last"
    ></b-pagination> -->
    <!-- <span @click="newly">최신순</span> | 
    <span @click="likely">인기순</span> -->

    <b-card no-body class="container">
      <br>
      <span>
        <b-form-select v-model="perPage">
          <option>5</option>
          <option>10</option>
          <option>15</option>
          <option>20</option>
          <option>30</option>
          <option>50</option>
        </b-form-select>
      </span>
                  <!-- v-model="filter" -->


      <br>

      <b-tabs card>
        <b-tab title="최신순" @click="newly">
          <div v-if="isArticle">작성된 글이 없습니다.</div>
          <b-table
            :items="items"
            :per-page="perPage"
            :current-page="currentPage"
            small
            :fields="fields"
            hover
            @row-clicked="goDetail"
            :filter="filter"
            :filter-included-fields="filterOn"
            @filtered="onFiltered"
          >
            <template slot="actions" slot-scope="row">{{row.item}}</template>
          </b-table>

        </b-tab>
        <b-tab title="인기순" @click="likely">
          <div v-if="isArticle">작성된 글이 없습니다.</div>
          <b-table
            :items="items"
            :per-page="perPage"
            :current-page="currentPage"
            small
            :fields="fields"
            hover
            @row-clicked="goDetail"
            :filter="filter"
            :filter-included-fields="filterOn"
            @filtered="onFiltered"
          >
          
          </b-table>
        </b-tab>
        
      </b-tabs>
      <span>
        <b-input-group>
          <b-form-input
            id="filter-input"
            type="search"
            placeholder="Type to Search"
            v-model="filter"
          ></b-form-input>
          <b-input-group-append>
            <b-button :disabled="!filter" @click="filter = ''">Clear</b-button>
          </b-input-group-append>
        </b-input-group>
      </span>
      <br>
      <b-pagination
        v-model="currentPage"
        :total-rows="items.length"
        :per-page="perPage"
        first-text="First"
        prev-text="Prev"
        next-text="Next"
        last-text="Last"
      ></b-pagination>
    </b-card>

    <br><br>
    <router-link :to="{ name: 'articleNew' }" v-if="isLoggedIn">
      <button class="btn btn-secondary ">글쓰기</button>
    </router-link>
    <!-- fileds = 'title, user, 좋아요 개수, 리뷰개수 ' -->

  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import _ from 'lodash'

  export default {
    name: 'ArticleList',
    computed: {
      ...mapGetters({
        articlesList: 'articles',
        isArticle: 'isArticle',
        isLoggedIn: 'isLoggedIn',
      }),
      rows(){
        return this.articles.length
      }
    },
    methods: {
      ...mapActions(['fetchArticles']),
      newly(){
        if (this.newLike !== 1){
          this.newLike = 1
          this.items = _.orderBy(this.articlesList, ['pk'], ['desc'])
        }
      },
      likely(){
        if (this.newLike !== 2){
          this.newLike = 2
          this.items = _.orderBy(this.articlesList, ['like_count'], ['desc'])
        }
      },
      goDetail(item){
        this.$router.push({name: 'article', params:{articlePk: item.pk}})
      },
      onFiltered(filteredItems) {
        // Trigger pagination to update the number of buttons/pages due to filtering
        this.totalRows = filteredItems.length
        this.currentPage = 1
      },
      goSearch(){

      }
    },
    created() {
      this.items = this.articlesList
      this.fetchArticles()
    },
    data(){
      return {
        items:[],
        perPage: 20,
        currentPage: 1,
        newLike: 1,
        fields:[
          { 'key': 'pk', label: '글 번호'},
          { 'key': 'title', label: '글 제목'},
          { 'key': 'user.username', label: '작성자' },
          { 'key': 'like_count', label: '추천수'}
        ],
        filter: null,
        filterOn: [],
        // checkBool: true,
      }
    },
    mounted() {
      this.items = this.articlesList
      this.fetchArticles()
      // this.checkBool = true
    },
    // updated(){
    //   if(this.checkBool){
    //     this.$router.go()
    //     this.checkBool=false
    //   }
    // }
  }
</script>

<style>
</style>

<style>
</style>
