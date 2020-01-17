<template>
  <b-card 
    v-show="show"
    style="max-width: 700px"
    class="mx-auto my-3">
    <b-modal
      v-model="isDeleteModalOpen"
      @ok="deleteUrl">
      <p> {{ delUrl.shorten_url }}を削除します</p>
    </b-modal>
    <span
      class="d-inline-block text-truncate"
      style="width: 55%"> 短縮元 URL
    </span>
    <span
      class="d-inline-block text-truncate"
      style="width: 30%"> 短縮後 URL
    </span>
    <div
      v-for="(url, i) in urls" 
      :key="url.url"
      :class="{'color-light-1': i%2 == 0, 'color-light-2': i%2 == 1}"
      class="my-3">
      <span
        class="d-inline-block text-truncate"
        style="width: 54%">
        <b-link
          :href="url.original_url"
          class="text-dark">
          {{ url.original_url }}
        </b-link>
      </span>
      <span
        class="d-inline-block text-truncate"
        style="width: 27%">
        <b-link
          :href="'https://' + url.shorten_url"
          class="text-dark">
          {{ url.shorten_url }}
        </b-link>
      </span>
      <span
        class="d-inline-block"
        style="width: 14%">
        <font-awesome-icon
          :icon="['far','copy']"
          class="my-auto mx-auto"
          @click="doCopy(url.shorten_url)"/>
        <font-awesome-icon
          :icon="['fas','qrcode']"
          class="my-auto mx-auto"
          @click="$emit('openModal',url)"/>
        <font-awesome-icon
          :icon="['fas','trash']"
          class="my-auto mx-auto"
          @click="openDeleteModal(url)"/>
      </span>
      <div 
        class="progress" 
        style="height: 3px;width: 100%">
        <div 
          :style="'width:'+ url.until + '%' " 
          class="progress-bar" 
          role="progressbar" 
          aria-valuenow="10" 
          aria-valuemin="0" 
          aria-valuemax="100"/>
      </div>
    </div>
  </b-card>
</template>
<script>
import axios from 'axios'
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

import { setInterval } from 'timers';
export default {
  data: function() {
    return {
      urls: [],
      delUrl: {},
      isDeleteModalOpen: false,
      show: false,
    }
  },
  watch: {
    urls: function() {
      this.show = this.urls.length > 0
    }
  },
  mounted: function(){
    axios.get('/api/urls')
    .then(response => {
      this.urls = response.data
    })
  },
  methods: {
      doCopy: function (URL) {
      var temp = document.createElement('div');
      temp.appendChild(document.createElement('pre')).textContent = 'https://' + URL;
      var s = temp.style;
      document.body.appendChild(temp)
      document.getSelection().selectAllChildren(temp)
      if (document.execCommand('copy')) alert('copied')
      document.body.removeChild(temp)
    },
    update: function(){
      axios.get('/api/urls')
      .then(response => {
        this.urls = response.data
      })
    },
    openDeleteModal: function(url) {
      this.delUrl = url
      this.isDeleteModalOpen = true
    },
    deleteUrl: function() {
      const params = new URLSearchParams()
      params.append('shorten_url', this.delUrl.shorten_url)
      axios.delete('/api/urls', {data: params})
      .then(() => {
        this.update()
      })
    }
  }
    
}
</script>

<style scoped>
.color-light-1 {
  background-color: #f7f7f7
}
.color-light-2 {
  background-color: #f1f1f1
}
</style>

