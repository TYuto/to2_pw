<template>
  <div>
    <b-card class="card mx-auto my-3">
      <b-input-group class="my-1 mx-2" prepend="your url">
        <b-form-input />
        <b-dropdown text="period" variant="info">
          <b-dropdown-item>Action A</b-dropdown-item>
          <b-dropdown-item>Action B</b-dropdown-item>
        </b-dropdown>
        <b-dropdown text="domain" variant="info">
          <b-dropdown-item>Action A</b-dropdown-item>
          <b-dropdown-item>Action B</b-dropdown-item>
        </b-dropdown>
      </b-input-group>
      <b-input-group class="my-2 float-left mx-2" style="max-width: 75%" prepend="shorten url">
        <b-form-input :readonly="true"/>
        <b-button variant="info"> copy </b-button>
      </b-input-group>
      <b-button class="col-2 my-2 float-right " variant="info"> create </b-button>
    </b-card>

    <b-card
      style="max-width: 700px"
      class="mx-auto my-3">
      <span
        class="d-inline-block text-truncate"
        style="width: 55%"> original url
      </span>
      <span
        class="d-inline-block text-truncate"
        style="width: 30%"> shorten url
      </span>
      <div
        v-for="(url, i) in shorten_urls"
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
          <b-btn variant="outline-info" class="px-0 py-0 mx-1 my-1 float-right">
            <b-icon-documents font-scale="1"/>
          </b-btn>

          <b-btn variant="outline-info" class="px-0 py-0 mx-1 my-1 float-right">
            <b-icon-box-arrow-up-right font-scale="1"/>
          </b-btn>

          <b-btn variant="outline-info" class="px-0 py-0 mx-1 my-1 float-right">
            <b-icon-trash font-scale="1"/>
          </b-btn>
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
  </div>
</template>

<script>
export default {
  data () {
    return {
      shorten_urls: [
        {
          original_url: 'https://github.com/afsdkfjalsdkfja;sldkj',
          shorten_url: 'to2.pw/aaaa'
        },
        {
          original_url: 'https://github.com/afsdkfjalsdkfja;sldkj',
          shorten_url: 'to2.pw/aa'
        }
      ]
    }
  }
}
</script>

<style>

.card {
    max-width: 700px
}

.color-light-1 {
  background-color: #f7f7f7
}
.color-light-2 {
  background-color: #f1f1f1
}

</style>
