<template>
  <section>
    <section id="wraper">
      <navbar />
      <urlshortner />
    </section>
    <footerc />
  </section>
</template>

<script>
import navbar from '~/components/navbar.vue'
import footerc from '~/components/footer.vue'
import urlshortner from '~/components/urlshortner.vue'

export default {
  components: {
    urlshortner,
    navbar,
    footerc
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
