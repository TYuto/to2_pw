<template>
  <b-card 
    style="max-width: 600px"
    class="mx-auto my-3">
    <span
      class="d-inline-block text-truncate"
      style="width: 60%"> orignal Url
    </span>
    <span
      class="d-inline-block text-truncate"
      style="width: 30%"> shorten url
    </span>
    <div
      v-for="(url, i) in urls" 
      :key="url.url"
      :class="{'color-light-1': i%2 == 0, 'color-light-2': i%2 == 1}"
      class="my-3">
      <span
        class="d-inline-block text-truncate"
        style="width: 60%">
        <b-link
          :href="url.original_URL"
          class="text-dark">
          {{ url.original_url }}
        </b-link>
      </span>
      <span
        class="d-inline-block text-truncate"
        style="width: 30%">
        <b-link
          :href="'https://' + url.shorten_url"
          class="text-dark">
          {{ url.shorten_url }}
        </b-link>
      </span>
      <font-awesome-icon
        v-b-tooltip.hover
        :icon="['far','copy']"
        title="copy"
        class="my-auto mx-auto"
        @click="doCopy(url.shorten_url)"/>
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
export default {
  data: function() {
    return {
      urls: []
    }
  },
  mounted: function(){
    axios.get('/api/urls')
    .then(response => {
      console.log(response.data)
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
      console.log('update called')
      axios.get('/api/urls')
      .then(response => {
        console.log(response.data)
        this.urls = response.data
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

