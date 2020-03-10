<template>
  <section>
    <section id="wraper">
      <navbar />
      <div style="width: 100%; height: 100%">
        <b-card
          style="max-width: 700px"
          class="mx-auto my-3">
          <VRuntimeTemplate :template="post" />
        </b-card>
      </div>
    </section>
    <footerc />
  </section>
</template>

<script>
import VRuntimeTemplate from 'v-runtime-template'
import navbar from '~/components/navbar.vue'
import footerc from '~/components/footer.vue'

export default {
  components: {
    navbar,
    footerc,
    VRuntimeTemplate
  },
  async asyncData ({ params, app }) {
    const post = await app.$getContents('pages', 'fields.urlString', params.id)
    return { post }
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
