<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-primary bg-gradient">
    <div class="container-fluid">
      <router-link class="navbar-brand pb-2" aria-current="page" :to="{ name: 'home' }">epm0dev.me
      </router-link>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
              aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse d-lg-flex justify-content-end" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <router-link class="nav-link active" aria-current="page" :to="{ name: 'projects' }">Projects</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link active" aria-current="page" :to="{ name: 'blog' }">Blog</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link active" aria-current="page" :to="{ name: 'feed' }">Feed</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link active" aria-current="page" :to="{ name: 'contact' }">Contact</router-link>
          </li>
        </ul>
      </div>
    </div>


    <!--
    <ul class="navbar-nav mr-auto">
      <li class="nav-item" v-if="accessToken=null">
        <router-link :to="{ name:'login' }">Login</router-link>
      </li>
      <li class="nav-item" v-if="accessToken!=null">
        <router-link :to="{ name:'logout' }">Logout</router-link>
      </li>
    </ul>
    -->
  </nav>
</template>

<script>
import {mapState} from 'vuex'

export default {
  name: 'Navbar',
  computed: mapState(['accessToken'])
}
</script>

<style scoped>

</style>