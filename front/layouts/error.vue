<template>
  <section>
    <section id="wraper">
      <navbar />
      <notFound v-if="error.statusCode===404" />
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
import notFound from '~/components/404.vue'

export default {
  props: ['error'],
  components: {
    VRuntimeTemplate,
    navbar,
    footerc,
    notFound
  },
  async asyncData ({ req, app }) {
    const about = await app.$getContents('staticContents', 'fields.id', 'about')
    return {
      about
    }
  },
  async fetch ({ store, req, app }) {
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
