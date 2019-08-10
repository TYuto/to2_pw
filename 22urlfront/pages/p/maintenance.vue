<template>
  <section>
    <section id="wraper">
      <navbarComp />
      <div style="width: 100%; height: 100%">
        <div
          class="ml-5 mt-5">
          <h1>
            現在メンテンナス中です
            <font-awesome-icon
              :icon="['fas', 'hammer']"/>
          </h1>
        </div>
      </div>
    </section>
    <footerComp />
  </section>
</template>

<script>
import axios from 'axios'
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'


import navbarComp from '~/components/navbarComp.vue'
import footerComp from '~/components/footerComp.vue'
export default {
  components: {
    navbarComp,
    footerComp,
  },
  created() {
    this.checkServer()
    setInterval(this.checkServer, 1000 * 30)
  },
  methods: {
    checkServer: function() {
      axios.get('/api/gen_200').then(response => {
        if(response.status == 200) {
          window.location.href = '/'
        }
      }).catch(e=>{})
    }
  }
}
</script>

<style>
html, body {
  height: 100%;
  margin: 0
}
#wraper {
  min-height: calc(100vh - 80px);
}
</style>
