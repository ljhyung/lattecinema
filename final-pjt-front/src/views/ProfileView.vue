<template>
  <div>
    <div class="container">
    <div class="main-body">
    
      <!-- Breadcrumb -->
      <!-- <nav aria-label="breadcrumb" class="main-breadcrumb">
        <ol class="breadcrumb">
          <li class="breadcrumb-item"><a href="index.html">Home</a></li>
          <li class="breadcrumb-item"><a href="javascript:void(0)">User</a></li>
          <li class="breadcrumb-item active" aria-current="page">User Profile</li>
        </ol>
      </nav> -->
      <!-- /Breadcrumb -->

        <div class="row gutters-sm">
          <div class="col-md-4 mb-3">
            <div class="card">
              <div class="card-body">
                <div class="d-flex flex-column align-items-center text-center">
                  <img src="https://bootdey.com/img/Content/avatar/avatar7.png" alt="Admin" class="rounded-circle" width="150">
                  <div class="mt-3">
                    <h4>{{ profile.username }}</h4>
                    <!-- <p class="text-secondary mb-1">Full Stack Developer</p>
                    <p class="text-muted font-size-sm">Bay Area, San Francisco, CA</p> -->
                    <div v-if="profile.pk!==currentUser.pk">
                      <button class="btn btn-primary" v-if="isFollowed" @click="followProfile(username)">Follow</button>
                      <button class="btn btn-outline-primary" v-if="!isFollowed" @click="followProfile(username)">Unfollow</button>
                      <!-- <button class="btn btn-outline-primary" >Message</button> -->
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="card mt-3">
              <ul class="list-group list-group-flush">
                <li class="list-group-item d-flex justify-content-between align-items-center flex-wrap">
                  <!-- <h6 class="mb-0"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-globe mr-2 icon-inline"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>Website</h6> -->
                  <h6><b-icon icon="file-earmark-text"></b-icon> 작성글</h6>
                  <span class="text-secondary">{{ this.howManyDoc }} 개</span>
                </li>

                <li class="list-group-item d-flex justify-content-between align-items-center flex-wrap">
                  <h6><b-icon icon="chat-left-text"></b-icon> 댓글</h6>
                  <span class="text-secondary"> 개</span>
                </li>

                <li class="list-group-item d-flex justify-content-between align-items-center flex-wrap">
                  <h6><b-icon icon="suit-heart-fill" variant="danger"></b-icon> 좋아요 한 횟수</h6>
                  <span class="text-secondary"> {{ howManyLikedArticle }} 개</span>
                </li>

                <li class="list-group-item d-flex justify-content-between align-items-center flex-wrap">
                  <h6><b-icon icon="person-plus-fill" variant="primary"></b-icon> 팔로워 </h6>
                  <span class="text-secondary"> {{ this.howManyFollower }}개</span>
              
                </li>

                <li class="list-group-item d-flex justify-content-between align-items-center flex-wrap">
                  <h6><b-icon icon="person-check-fill" variant="primary"></b-icon> 팔로잉 </h6>
                  <span class="text-secondary"> {{ this.howManyFollowing }}개</span>
                </li>

              </ul>
            </div>
          </div>
          <div class="col-md-8">
            <div class="card mb-3">
              <div class="card-body">
                <div class="row">
                  <div class="col-sm-3">
                    <h6 class="mb-0">닉네임</h6>
                  </div>
                  <div class="col-sm-9 text-secondary">
                    : {{ profile.username }}
                  </div>
                </div>
                <hr>
                <div class="row">
                  <div class="col-sm-3">
                    <h6 class="mb-0">E-mail</h6>
                  </div>
                  <div class="col-sm-9 text-secondary">
                    : {{ profile.email }}
                  </div>
                </div>
                <hr>
                <div class="row">
                  <div class="col-sm-3">
                    <h6 class="mb-0">성</h6>
                  </div>
                  <div class="col-sm-9 text-secondary">
                    : {{ profile.last_name }}
                  </div>
                </div>
                <hr>
                <div class="row">
                  <div class="col-sm-3">
                    <h6 class="mb-0">이름</h6>
                  </div>
                  <div class="col-sm-9 text-secondary">
                    : {{ profile.first_name }}
                  </div>
                </div>
                <hr>
                <!-- <div class="row">
                  <div class="col-sm-3">
                    <h6 class="mb-0">Address</h6>
                  </div>
                  <div class="col-sm-9 text-secondary">
                    Bay Area, San Francisco, CA
                  </div>
                </div> -->
                <div class="row" v-if="profile.pk===currentUser.pk">
                  <div class="col-sm-12">
                    <router-link class="btn btn-secondary " :to="{ name: 'profileEdit',  params: { username: profile.username, profile: profile } }">edit</router-link>
                    <!-- edit -->
                    <!-- <a class="btn btn-primary " target="__blank" href="https://www.bootdey.com/snippets/view/profile-edit-data-and-skills"><router-link v-if="profile.pk===currentUser.pk" :to="{ name: 'profileEdit',  params: { username: profile.username, profile: profile } }"></router-link>edit</a> -->
                  </div>
                </div>
              </div>
            </div>
            <!-- {{profile}} -->
            <div class="card h-100">
              <div class="card-body">
                <div class="row gutters-sm">
                  <b-tabs >
                    <b-tab title="작성글">
                      <div v-if="isUserArticles">작성된 글이 없습니다.</div>
                      <div v-if="!isUserArticles" class="col-sm-12 mb-3">
                        <b-table
                          :items='profileArticles'
                          :fields='fields'
                          hover
                          perPage= 10
                          small
                          @row-clicked='goDetail'
                          >
                        </b-table>
                      </div>
                    </b-tab>

                    <b-tab title="좋아요 한 글">
                      <div v-if="isUserLikedArticles">좋아요 한 글이 없습니다.</div>
                      <div class="col-sm-12 mb-3" v-if="!isUserLikedArticles">
                        <b-table
                          :items='profileLikedArticles'
                          :fields='fields'
                          hover
                          perPage= 10
                          small
                          @row-clicked='goDetail'
                          >
                        </b-table>
                      </div>
                    </b-tab>
                <!-- <b-tab title="좋아요한 글">
                  <div v-if="isUserLikedArticles">작성된 글이 없습니다.</div>
                  <div v-if="!isUserLikedArticles" class="col-sm-12 mb-3">
                    <div class="card h-100">
                      <div class="card-body">
                        <h6 class="d-flex align-items-center mb-3"><i class="material-icons text-info mr-2">assignment</i>Project Status</h6>
                        <small>Web Design</small>
                        <div class="progress mb-3" style="height: 5px">
                          <div class="progress-bar bg-primary" role="progressbar" style="width: 80%" aria-valuenow="80" aria-valuemin="0" aria-valuemax="100"></div>
                        </div>
                        <small>Website Markup</small>
                        <div class="progress mb-3" style="height: 5px">
                          <div class="progress-bar bg-primary" role="progressbar" style="width: 72%" aria-valuenow="72" aria-valuemin="0" aria-valuemax="100"></div>
                        </div>
                        <small>One Page</small>
                        <div class="progress mb-3" style="height: 5px">
                          <div class="progress-bar bg-primary" role="progressbar" style="width: 89%" aria-valuenow="89" aria-valuemin="0" aria-valuemax="100"></div>
                        </div>
                        <small>Mobile Template</small>
                        <div class="progress mb-3" style="height: 5px">
                          <div class="progress-bar bg-primary" role="progressbar" style="width: 55%" aria-valuenow="55" aria-valuemin="0" aria-valuemax="100"></div>
                        </div>
                        <small>Backend API</small>
                        <div class="progress mb-3" style="height: 5px">
                          <div class="progress-bar bg-primary" role="progressbar" style="width: 66%" aria-valuenow="66" aria-valuemin="0" aria-valuemax="100"></div>
                        </div>
                      </div>
                    </div>
                  </div>
                </b-tab> -->
                </b-tabs>
              </div>
            </div>

              <!-- <div class="col-sm-6 mb-3">
                <div class="card h-100">
                  <div class="card-body">
                    <h6 class="d-flex align-items-center mb-3"><i class="material-icons text-info mr-2">assignment</i>Project Status</h6>
                    <small>Web Design</small>
                    <div class="progress mb-3" style="height: 5px">
                      <div class="progress-bar bg-primary" role="progressbar" style="width: 80%" aria-valuenow="80" aria-valuemin="0" aria-valuemax="100"></div>
                    </div>
                    <small>Website Markup</small>
                    <div class="progress mb-3" style="height: 5px">
                      <div class="progress-bar bg-primary" role="progressbar" style="width: 72%" aria-valuenow="72" aria-valuemin="0" aria-valuemax="100"></div>
                    </div>
                    <small>One Page</small>
                    <div class="progress mb-3" style="height: 5px">
                      <div class="progress-bar bg-primary" role="progressbar" style="width: 89%" aria-valuenow="89" aria-valuemin="0" aria-valuemax="100"></div>
                    </div>
                    <small>Mobile Template</small>
                    <div class="progress mb-3" style="height: 5px">
                      <div class="progress-bar bg-primary" role="progressbar" style="width: 55%" aria-valuenow="55" aria-valuemin="0" aria-valuemax="100"></div>
                    </div>
                    <small>Backend API</small>
                    <div class="progress mb-3" style="height: 5px">
                      <div class="progress-bar bg-primary" role="progressbar" style="width: 66%" aria-valuenow="66" aria-valuemin="0" aria-valuemax="100"></div>
                    </div>
                  </div>
                </div>
              </div> -->
            </div>
          </div>
        </div>

      </div>
    </div>


    <!-- <h1>{{ profile.username }}</h1> -->
    <!-- <p>{{profile}}</p>

    <h2>작성한 글</h2>
    <ul>
      <li v-for="article in profile.articles" :key="article.pk">
        <router-link :to="{ name: 'article', params: { articlePk: article.pk } }">
          {{ article.title }}
        </router-link>
      </li>
    </ul>

    <h2>좋아요 한 글</h2>
    <ul>
      <li v-for="article in profile.like_articles" :key="article.pk">
        <router-link :to="{ name: 'article', params: { articlePk: article.pk } }">
          {{ article.title }}
        </router-link>
      </li>
    </ul> -->
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import _ from 'lodash'

export default {
  name: 'ProfileView',
  computed: {
    ...mapGetters(['profile', 'currentUser',]),
    username(){
      return this.profile.username
    },
    followers(){
      return this.profile.followers
    },
    followings(){
      return this.profile.followings
    },
    followersNum(){
      if (this.followers!==undefined){
        return this.profile.followers.length
      } else{
        return 0
      }
    },
    followingsNum(){
      if (this.followers!==undefined){
        return this.profile.followings.length
      } else{
        return 0
      }
    },
    isFollowed(){
      if (this.followers!==undefined){
        for (const follow of this.followers) {
          // console.log('??')
          // console.log(follow)
          if (follow.pk===this.currentUser.pk) {
            // console.log()
            return false
          }
        }
        return true
      } else{
      return true
      }
    },
    howManyDoc(){
      return this.profile.articles.length
    },
    howManyLikedArticle(){
      return this.profile.like_articles.length
    },
    howManyFollower(){
      return this.profile.followers.length
    },
    howManyFollowing(){
      return this.profile.followings.length
    },
    isUserArticles(){
      return _.isEmpty(this.profile.articles)
    },
    isUserLikedArticles(){
      return _.isEmpty(this.profile.like_articles)
    },
    profileArticles(){
      return this.profile.articles
    },
    profileLikedArticles(){
      return this.profile.like_articles
    }
    // howManyLikedArticle(){
    //   return this.profile.
    // }
  },
  methods: {
    ...mapActions(['fetchProfile', 'followProfile']),
      goDetail(item){
        this.$router.push({name: 'article', params:{articlePk: item.pk}})
      },
  },
  mounted() {
    const payload = { username: this.$route.params.username }
    // this.fetchProfile(payload)
    // console.log(this.currentUser)
    this.fetchProfile(payload)
  },
  // beforeUpdate(){
  //   const payload = { username: this.$route.params.username }
  //   this.fetchProfile(payload)
  // }
  data(){
    return {
      fields: [
        { 'key': 'title', label: '글 제목'},
      ]
    }
  },
}
</script>

<style scoped>
body{
    margin-top:20px;
    color: #1a202c;
    text-align: left;
    background-color: #e2e8f0;    
}
.main-body {
    padding: 15px;
}
.card {
    box-shadow: 0 1px 3px 0 rgba(0,0,0,.1), 0 1px 2px 0 rgba(0,0,0,.06);
}

.card {
    position: relative;
    display: flex;
    flex-direction: column;
    min-width: 0;
    word-wrap: break-word;
    background-color: #fff;
    background-clip: border-box;
    border: 0 solid rgba(0,0,0,.125);
    border-radius: .25rem;
}

.card-body {
    flex: 1 1 auto;
    min-height: 1px;
    padding: 1rem;
}

.gutters-sm {
    margin-right: -8px;
    margin-left: -8px;
}

.gutters-sm>.col, .gutters-sm>[class*=col-] {
    padding-right: 8px;
    padding-left: 8px;
}
.mb-3, .my-3 {
    margin-bottom: 1rem!important;
}

.bg-gray-300 {
    background-color: #e2e8f0;
}
.h-100 {
    height: 100%!important;
}
.shadow-none {
    box-shadow: none!important;
}
</style>