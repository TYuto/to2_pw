<template>
  <section>
    <section id="wraper">
      <navbarComp />
      <div style="width: 100%; height: 100%">
        <urlEditTool />
        <b-card
          style="max-width: 700px"
          class="mx-auto my-3">
          <div v-html="post" />
        </b-card>
      </div>
    </section>
    <footerComp />
  </section>
</template>

<script>
import axios from 'axios'
import {createClient} from 'contentful'
import { documentToHtmlString } from '@contentful/rich-text-html-renderer'



const contentful_client = createClient({
  space: process.env.CTF_SPACE_ID,
  accessToken: process.env.CTF_CDA_ACCESS_TOKEN,
});
import navbarComp from '~/components/navbarComp.vue'
import footerComp from '~/components/footerComp.vue'
import urlEditTool from '~/components/urlEditTool.vue'

export default {
  components: {
    navbarComp,
    footerComp,
    urlEditTool,
  },
  data: function() {
    return {
      post: ''
    }
  },
  mounted: function () {
    let id = this.$route.params.id
    contentful_client.getEntries({
      'content_type' : 'newRelease',
      'fields.urlString': id,
      'limit' : 1
    })
    .then((response) => {
      console.log(response.items)
      if(response.items.length === 0) {
        window.location.href = '/'
      }
      this.post = documentToHtmlString(response.items[0].fields.body)
    }).catch(console.error)
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
