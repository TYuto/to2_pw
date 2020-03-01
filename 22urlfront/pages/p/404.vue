<template>
  <section>
    <section id="wraper">
      <navbarComp />
      <b-card
        style="max-width: 700px"
        class="mx-auto my-3">
        <h1
          style="max-width: 600px"
          class="mx-auto">
          <p class="text-center">
            <font-awesome-icon
              :icon="['fas', 'question']"/>
            404 URL Not Found
          </p>
        </h1>
        以下のページは見つかりませんでした, 大文字小文字等ご確認いただき, アクセスお願いします.
        <b-input-group
          :prepend="host"
          class="my-3">
          <b-form-input v-model="toPath"/>
          <b-button @click="click">アクセスする</b-button>
        </b-input-group>
        <b-card
          v-if="recomends.length > 0"
          calss="my-auto">
          <p>もしかして...</p>
          <a 
            v-for="recomend in recomends"
            :key="recomend.path"
            :href="recomend">{{ recomend }} </a>
        </b-card>
      </b-card>
      <b-card
        style="max-width: 700px"
        class="mx-auto my-3">
        <description />
      </b-card>
      <urlEditTool />
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
import urlEditTool from '~/components/urlEditTool.vue'
import description from '~/components/md/description.vue'

export default {
  components: {
    navbarComp,
    footerComp,
    urlEditTool,
    description,
  },
  data() {
      return {
          url: '',
          host: '',
          toPath: '',
          recomends: []
      }
  },
  mounted() {
      console.log(this.$route)
      if (this.$route.path != '/p/404'){
        window.location.href = '/p/404?url=' + window.location.href
      } else {
        this.url = this.$route.query.url
        if (this.url.length > 0) {
            this.host = this.url.split('/').slice(0, 3).join('/') + '/'
            this.toPath = this.url.split('/').slice(3).join('/')
            console.log(this.toPath);

            ['(',')', '（', '）', '-', ':'].forEach(key =>{
                if(this.toPath.includes(key)){
                    var d = this.toPath.split(key)[0]
                    this.recomends.push(this.host + d)
                }
            })
        }
      }
  },
  methods: {
      click: function() {
          window.location.href = this.host + this.toPath
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
