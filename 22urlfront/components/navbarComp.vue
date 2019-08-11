<template>
  <b-navbar 
    toggleable="md" 
    type="light" 
    variant="light">

    <b-navbar-toggle target="nav_collapse"/>
    <a href="/">
      <img 
        src="~/assets/logo.png"
        class="logo-img">
    </a>
    <b-collapse 
      id="nav_collapse" 
      is-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">

        <!--
        <b-nav-item-dropdown 
          text="Lang" 
          right>
          <b-dropdown-item href="#">EN</b-dropdown-item>
          <b-dropdown-item href="#">JA</b-dropdown-item>
        </b-nav-item-dropdown>
        -->

        <b-nav-item right>
          <login />
        </b-nav-item>
      </b-navbar-nav>

    </b-collapse>
  </b-navbar>
</template>
<script>
import login from '~/components/login.vue'
import axios from 'axios'
import { mapState, mapMutations } from 'vuex'
export default {
  components: {
    login
  },
  created: function() {
    axios.get('/api/user')
    .then(response => {
      if (response.data.authed) {
        this.SET_USER(response.data.username)
      }
    })
  },
  methods: {
    ...mapMutations({
      SET_USER: 'SET_USER'
    })
  }
}
</script>

<style scoped>
.logo-img {
    width:80px;
}
</style>
