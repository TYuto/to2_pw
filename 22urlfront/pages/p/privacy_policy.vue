<template>
  <section>
    <section id="wraper">
      <navbarComp />
      <div style="width: 100%; height: 100%">
        <div
          class="mx-4 mt-5"
          v-html="$md.render(mdStr)" />
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

import mdStr from '~/md/privacy_policy.md'
export default {
  components: {
    navbarComp,
    footerComp,
  },
  computed: {
    mdStr() {
      return  mdStr
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
