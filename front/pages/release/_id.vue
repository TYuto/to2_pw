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
import { createClient } from 'contentful'
import { documentToHtmlString } from '@contentful/rich-text-html-renderer'

import VRuntimeTemplate from 'v-runtime-template'
import navbar from '~/components/navbar.vue'
import footerc from '~/components/footer.vue'

const contentfulClient = createClient({
  space: process.env.CTF_SPACE_ID,
  accessToken: process.env.CTF_CDA_ACCESS_TOKEN
})

export default {
  components: {
    navbar,
    footerc,
    VRuntimeTemplate
  },
  props: [
    'contentType'
  ],
  async asyncData ({ params }) {
    const response = await contentfulClient.getEntries({
      content_type: 'newRelease',
      'fields.urlString': params.id,
      limit: 1
    })
    console.log(response.items)
    return { post: '<section>' + documentToHtmlString(response.items[0].fields.body) + '</section>' }
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
