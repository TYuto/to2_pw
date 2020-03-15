<template>
  <section>
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
      {{ $t('message.notFound') }}
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
  </section>
</template>

<script>

export default {
  components: {
  },
  data () {
    return {
      url: '',
      host: '',
      toPath: '',
      recomends: []
    }
  },
  mounted () {
    this.url = this.$route.query.url || window.location.href
    if (this.url.length > 0) {
      this.host = this.url.split('/').slice(0, 3).join('/') + '/'
      this.toPath = this.url.split('/').slice(3).join('/')
      console.log(this.toPath);

      ['(', ')', '（', '）', '-', ':'].forEach((key) => {
        if (this.toPath.includes(key)) {
          const d = this.toPath.split(key)[0]
          this.recomends.push(this.host + d)
        }
      })
    }
  },
  methods: {
    click () {
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
