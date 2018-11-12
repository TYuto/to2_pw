<template>
  <section>
    <section id="wraper">
      <navbarComp />
      <createUrl />
      <urlTable />
      <div id="push" />
    </section>
    <footerComp />
  </section>
</template>

<script>
import navbarComp from '~/components/navbarComp.vue'
import footerComp from '~/components/footerComp.vue'
import createUrl from '~/components/createUrl.vue'
import urlTable from '~/components/urlTable.vue'
export default {
  components: {
    navbarComp,
    footerComp,
    createUrl,
    urlTable
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
