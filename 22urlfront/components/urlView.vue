<template>
  <b-modal
    v-model="isModalOpen"
    :ok-only="true">
    <h1 class="mx-5">
      <a
        :href="'https://' + shorten_url"
        class="text-dark">
        {{ shorten_url }}
      </a>
    </h1>
    <h3
      :href="original_url"
      class="mx-5 my-1">
      <span
        class="d-inline-block text-truncate"
        style="width: 100%">
        <a
          :href="original_url"
          class="text-muted">
          {{ original_url }}
        </a>
      </span>
    </h3>
    <div
      class="mx-4"
      style="height: 400px; width: 400px ">
      <svg
        ref="qrcode"
        class="mx-0 my-0"
        height="400px"
        width="400px"
        v-html="svgCode" />
    </div>
  </b-modal>
</template>
<script>
import QRCode from 'qrcode'

export default {
  data(){
    return {
      original_url: '',
      shorten_url: '',
      isModalOpen: false,
      svgCode: ''
    }
  },
  watch: {
  },
  methods: {
    open: function(url) {
      this.isModalOpen = true;
      this.original_url =url.original_url;
      this.shorten_url = url.shorten_url;
      QRCode.toString(this.shorten_url, {
        type: 'svg',
        color: {
          light: '#0001'
        }
      }, (error, string) => {
        this.svgCode = string
      })
    }
  }
}
</script>
<style scoped>
</style>


