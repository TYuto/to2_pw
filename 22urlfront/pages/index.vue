<template>
  <section>
    <section id="wraper">
      <navbarComp />
      <createUrl @create="$refs.table.update();"/>
      <urlTable ref="table"/>
      <div id="push" />
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
import createUrl from '~/components/createUrl.vue'
import urlTable from '~/components/urlTable.vue'
export default {
  components: {
    navbarComp,
    footerComp,
    createUrl,
    urlTable
  },
  created () {
    this.checkServer()
    setInterval(this.checkServer, 30 * 1000)
  },
  methods: {
    checkServer: async function() {
      try {
        const res = await axios.get('/api/gen_200')
      } catch(e) {
        window.location.href = '/p/maintenance'
      }
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
