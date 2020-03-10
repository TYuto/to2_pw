<template>
  <section>
    <section id="wraper">
      <navbar />
      <urlshortner />
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
  async asyncData (context) {
    const about = await context.app.$getContents('staticContents', 'fields.id', 'about')
    return { about }
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
