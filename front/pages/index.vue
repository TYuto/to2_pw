<template>
  <section>
    <section id="wraper">
      <navbar />
      <urlshortner
        :shortenUrls="shortenUrls"
        :domains="domains"/>
      <b-card
        style="max-width: 700px"
        class="mx-auto my-3">
        <VRuntimeTemplate :template="about" />
      </b-card>
    </section>
    <footerc />
  </section>
</template>

<script>
import https from 'https'

import VRuntimeTemplate from 'v-runtime-template'

import navbar from '~/components/navbar.vue'
import footerc from '~/components/footer.vue'
import urlshortner from '~/components/urlshortner.vue'

export default {
  components: {
    VRuntimeTemplate,
    urlshortner,
    navbar,
    footerc
  },
  async asyncData ({ req, app }) {
    const agent = new https.Agent({ rejectUnauthorized: false })
    const options = {
      httpsAgent: agent,
      withCredentials: true
    }
    if (process.server) { options.headers = req.headers }

    const about = await app.$getContents('staticContents', 'fields.id', 'about')
    const urlsres = await app.$axios.get('/api/urls/', options)
    const domainsres = await app.$axios.get('/api/v2/domains/', options)
    return {
      about,
      shortenUrls: urlsres.data,
      domains: domainsres.data
    }
  },
  async fetch ({ store, req, app }) {
    const agent = new https.Agent({ rejectUnauthorized: false })
    const options = {
      httpsAgent: agent,
      withCredentials: true
    }
    if (process.server) { options.headers = req.headers }
    const userres = await app.$axios.get('/api/user/', options)
    if (userres.data.authed) {
      store.commit('SET_USER', userres.data.username)
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
  min-height: calc(100vh - 60px);
}
</style>
