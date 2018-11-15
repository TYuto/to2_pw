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
          {{ url.original_URL }}
        </b-link>
      </span>
      <span
        class="d-inline-block text-truncate"
        style="width: 30%">
        <b-link
          :href="'https://' + url.url"
          class="text-dark">
          {{ url.url }}
        </b-link>
      </span>
      <font-awesome-icon
        v-b-tooltip.hover
        :icon="['far','copy']"
        title="copy"
        class="my-auto mx-auto"
        @click="doCopy(url.url)"/>
      <div 
        class="progress" 
        style="height: 3px;width: 100%">
        <div 
          class="progress-bar" 
          role="progressbar" 
          style="width: 50%;" 
          aria-valuenow="10" 
          aria-valuemin="0" 
          aria-valuemax="100"/>
      </div>
    </div>
  </b-card>
</template>
<script>
export default {
  data: function() {
    return {
      urls: [
        { original_URL: 'https://example.com/hogefugapio?hoge=hoge&fuga=fuga', expairation_date: '2018-02-01 16:00' ,url: '22ur.tk/xx' },
        { original_URL: 'https://example.com/hoge', expairation_date: '2018-02-01 16:00' ,url: '22ur.tk/xx' },
        { original_URL: 'https://example.com/hoge', expairation_date: '2018-02-01 16:00' ,url: '22ur.tk/xx' },
        { original_URL: 'https://example.com/hoge', expairation_date: '2018-02-01 16:00' ,url: '22ur.tk/xx' }
      ]
    }
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

