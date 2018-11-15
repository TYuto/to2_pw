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
      style="width: 35%"> shorten url
    </span>
    <section
      v-for="url in urls" 
      :key="url.url">
      <span
        class="d-inline-block text-truncate"
        style="width: 60%"> {{ url.original_URL }}
      </span>
      <span
        class="d-inline-block text-truncate"
        style="width: 35%"> {{ url.url }}
      </span>
      <div 
        class="progress" 
        style="height: 3px;width: 100%">
        <div 
          class="progress-bar" 
          role="progressbar" 
          style="width: 10%;" 
          aria-valuenow="10" 
          aria-valuemin="0" 
          aria-valuemax="100"/>
      </div>
    </section>
  </b-card>
</template>
<script>
export default {
  data: function() {
    return {
      urls: [
        { original_URL: 'https://example.com/hoge', expairation_date: '2018-02-01 16:00' ,url: 'https://22ur.tk/xx' },
        { original_URL: 'https://example.com/hoge', expairation_date: '2018-02-01 16:00' ,url: 'https://22ur.tk/xx' },
        { original_URL: 'https://example.com/hoge', expairation_date: '2018-02-01 16:00' ,url: 'https://22ur.tk/xx' },
        { original_URL: 'https://example.com/hoge', expairation_date: '2018-02-01 16:00' ,url: 'https://22ur.tk/xx' }
      ]
    }
  }
    
}
</script>

