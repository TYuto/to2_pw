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
        <div
          v-show="notify.available"
          class="my-2">
          <b-button
            id="popover-target-1"
            :href="notify.url">
            New
          </b-button>
          <b-popover
            target="popover-target-1"
            triggers="hover"
            placement="auto">
            {{ notify.title }}
          </b-popover>
        </div>
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
import {createClient} from 'contentful'
import { mapState, mapMutations } from 'vuex'

const contentful_client = createClient({
  space: process.env.CTF_SPACE_ID,
  accessToken: process.env.CTF_CDA_ACCESS_TOKEN,
});

export default {
  components: {
    login
  },
  data: function() {
    return {
      notify : {
        available: false,
        title: '',
        url: '',
      }
    }
  },
  created: function() {
    this.setNotify()
    axios.get('/api/user')
    .then(response => {
      if (response.data.authed) {
        this.SET_USER(response.data.username)
      }
    })
  },
  methods: {
    setNotify: function() {
      contentful_client.getEntries({
        'content_type' : 'newRelease',
        'fields.expiredAt[gte]': (new Date()).toISOString(),
        'limit' : 1
      })
      .then((response) => {
        console.log(response.items)
        if (response.items.length === 0) {
          return
        }
        const item = response.items[0].fields
        this.notify.available = true
        this.notify.title = item.title
        this.notify.url = 'release/' + item.urlString
      })
    },
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
