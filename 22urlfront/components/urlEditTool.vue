<template>
  <section>
    <createUrl @create="urlCreated"/>
    <urlTable
      ref="table"
      @openModal="openUrlModal"/>
    <urlView ref="urlModal"/>
    <div id="push" />
  </section>
</template>

<script>
import axios from 'axios'
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

import createUrl from '~/components/createUrl.vue'
import urlTable from '~/components/urlTable.vue'
import urlView from '~/components/urlView.vue'
import description from '~/components/md/description.vue'
export default {
  components: {
    createUrl,
    urlTable,
    urlView,
  },
  methods: {
    urlCreated: function(shortenUrl) {
      this.$refs.table.update();
      this.$refs.urlModal.open(shortenUrl)
    },
    openUrlModal: function(shortenUrl){
      this.$refs.urlModal.open(shortenUrl)
    }
  }
}
</script>
