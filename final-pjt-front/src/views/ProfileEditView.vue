<template>
  <!-- <div>
    프로필 수정하기
    <form @submit.prevent="onSubmit">
      <div>
        <label for="username">username: </label>
        <input v-model="newProfile.username" type="text" id="username" />
      </div>
      <div>
        <label for="email">email: </label>
        <textarea v-model="newProfile.email" type="text" id="email"></textarea>
      </div>
      <div>
        <label for="last_name">last_name: </label>
        <textarea v-model="newProfile.last_name" type="text" id="last_name"></textarea>
      </div>
      <div>
        <label for="first_name">first_name: </label>
        <textarea v-model="newProfile.first_name" type="text" id="first_name"></textarea>
      </div>
      <div>
        <button>수정하기</button>
      </div>
    </form>
  </div> -->
  
  <!-- <div class="card">
    <div>
      <div class="d-flex flex-row mt-2 mb-2 align-items-center gap-2">
        <label>Name:</label>
        <input class="form-control" type="text" ref="first_name"  :disabled="!isEditing"
              :class="{view: !isEditing}" :value="user.firstName">      
      </div>
      
      <div class="d-flex flex-row mt-2 mb-2 align-items-center gap-2">
        <label>Username:</label>
        <input class="form-control" type="text" ref="username" :value="user.username" :disabled="!isEditing"
              :class="{view: !isEditing}">  
      </div>
      
      <div class="d-flex flex-row mt-2 mb-2 align-items-center gap-2">
        <label>Email:</label>
        <input class="form-control" type="text" ref="email" :value="user.email" :disabled="!isEditing"
              :class="{view: !isEditing}">  
      </div>
      
      <div class="d-flex flex-row mt-2 align-items-center gap-2">
        <label>Password:</label>
        <input class="form-control" type="password" ref="password" :value="user.password">  
      </div>
      
      
      
      <div class="mt-3 mb-3">
          <button class="btn btn-sm btn-success" @click="isEditing = !isEditing" v-if="!isEditing">
          Edit
          </button>

        <button class="btn btn-sm btn-success me-1" @click="save" v-else-if="isEditing">
          Save
        </button>
        
        <button class="btn btn-sm btn-danger" v-if="isEditing" @click="isEditing = false">Cancel</button>
      </div>
    </div>
  </div> -->
  <div>
    <form @submit.prevent="onSubmit">
      <div class="card">
        <div class="d-flex flex-row mt-2 mb-2 align-items-center gap-2">
          <div>
            <div class="d-flex flex-row mt-2 mb-2 align-items-center gap-2">
              <!-- <label for="username">username: </label> -->
              <input v-model="newProfile.username" type="text" id="username" />
            </div>
            
            <div class="d-flex flex-row mt-2 mb-2 align-items-center gap-2">
              <!-- <label for="email">email: </label> -->
              <textarea v-model="newProfile.email" type="text" id="email"></textarea>
            </div>
            
            <div class="d-flex flex-row mt-2 mb-2 align-items-center gap-2">
              <!-- <label for="last_name">last_name: </label> -->
              <textarea v-model="newProfile.last_name" type="text" id="last_name"></textarea>
            </div>
            
            <div class="d-flex flex-row mt-2 align-items-center gap-2">
              <!-- <label for="first_name">first_name: </label> -->
              <textarea v-model="newProfile.first_name" type="text" id="first_name"></textarea>
            </div>
            <div class="mt-3 mb-3">
            </div>
            <button class="btn btn-sm btn-success">
              Edit
            </button>
          </div>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'ProfileEditView',
  // props: {
  //   profile: Object,
  // },
  computed: {
    ...mapGetters(['profile', 'currentUser']),
    newProfile(){
      const newProfile = this.profile
      return newProfile
    }
  },
  methods: {
    ...mapActions(['updateProfile']),
    onSubmit(){
      this.updateProfile(this.newProfile)
    }
  },
}
</script>

<style scoped>
.view {
  border-color: transparent;
  background-color: initial !important;
  color: initial
}

.form-control{
  outline: none;
  box-shadow: none;
}

.mt-5{
    margin-top:10px;
}

.mb-5{
    margin-bottom:20px;
}

body{
  height:100vh;
  background-color:#eee;
  display:flex;
  justify-content:center;
  align-items:center;
}

.card{
    width:350px;
    background-color:#fff;
    padding:25px;
    border-radius:10px;
    border: none;
}

.btn{
    outline: none;
    box-shadow: none;
}
</style>