<template>
  <section>
    <navbarComp />
    <createUrl />
    <footerComp />
  </section>
</template>

<script>
import navbarComp from '~/components/navbarComp.vue'
import footerComp from '~/components/footerComp.vue'
import createUrl from '~/components/createUrl.vue'
export default {
  components: {
    navbarComp,
    footerComp,
    createUrl
  }
}
</script>

<style>
</style>
