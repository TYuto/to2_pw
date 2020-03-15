<template>
  <div>
    <b-overlay :show="inProgress" rounded="sm">
      <b-card class="card mx-auto my-3" :aria-hidden="inProgress ? 'true' : null">
        <b-input-group class="my-1 mx-2" :prepend="$t('common.yourUrl')">
          <b-form-input
            v-model="selectedOriginalUrl"
            :state="isOriginalUrlValid"
            for="type-url"
            />
        </b-input-group>
        <b-dropdown
          class="mx-2 my-3 float-left"
          :text="(selectedPeriod && $t('common.' + selectedPeriod))|| $t('common.period')"
          variant="info">
          <b-dropdown-item
            v-for="p in period"
            :key="p"
            @click="selectedPeriod = p">
            {{ $t('common.' + p) }}
          </b-dropdown-item>
        </b-dropdown>
        <b-dropdown
          class="mx-2 my-3 float-left"
          :text="selectedDomain.host || $t('common.domain')"
          variant="info">
          <b-dropdown-item
            v-for="domain in domains"
            :key="domain.host"
            @click="selectedDomain = domain">
            {{ domain.host}} </b-dropdown-item>
        </b-dropdown>
        <p class="float-left mx-2 my-3">
          {{ $t('createUrl.urlLen') }}: {{ urlLen }}
        </p>
        <b-button @click="onClickCreate" class="float-right my-3" style="min-width: 100px;" variant="info" :disabled="!isAllValid"> {{ $t('common.create') }} </b-button>
      </b-card>
    </b-overlay>

    <b-card
      v-if="shortenUrls.length > 0"
      style="max-width: 700px"
      class="mx-auto my-3">
      <span
        class="d-inline-block text-truncate"
        style="width: 55%">
        {{ $t('common.originalUrl') }}
      </span>
      <span
        class="d-inline-block text-truncate"
        style="width: 30%">
        {{ $t('common.shortenUrl') }}
      </span>
      <div
        v-for="(url, i) in shortenUrls"
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
          style="width: 23%">
          <b-link
            :href="'https://' + url.shorten_url"
            class="text-dark">
            {{ url.shorten_url }}
          </b-link>
        </span>
        <span>
          <b-btn
            @click="addToClipBoard(url)"
            v-b-popover.hover.top="$t('common.copy')"
            variant="outline-info"
            class="px-0 py-0 mx-1 my-1 float-right">
            <b-icon-documents font-scale="1"/>
          </b-btn>
          <b-btn
            @click="showQr(url)"
            v-b-popover.hover.top="$t('message.showQr')"
            variant="outline-info"
            class="px-0 py-0 mx-1 my-1 float-right">
            <b-icon-box-arrow-up-right font-scale="1"/>
          </b-btn>
          <b-btn
            @click="openDeleteModal(url)"
            v-b-popover.hover.top="$t('common.delete')"
            variant="outline-info"
            class="px-0 py-0 mx-1 my-1 float-right">
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
    <b-modal
      v-model="isDeleteModalOpen"
      @ok="deleteUrl">
      <p> {{ delUrl }}を削除します</p>
    </b-modal>
    <b-modal
      v-model="isQrViewModalOpen"
      :ok-only="true">
      <h1 class="mx-5">
        <a
          :href="'https://' + selectedShortenUrl"
          class="text-dark">
          {{ selectedShortenUrl }}
        </a>
      </h1>
      <div style="text-align: center">
        <svg
          height="400px"
          width="400px"
          v-html="svgCode" />
      </div>
    </b-modal>
  </div>
</template>

<script>
import QRCode from 'qrcode'

export default {
  data () {
    return {
      selectedPeriod: '',
      selectedDomain: '',
      selectedOriginalUrl: '',
      period: [
        'hour',
        'days',
        'month'
      ],
      inProgress: false,
      isDeleteModalOpen: false,
      isQrViewModalOpen: false,
      delUrl: '',
      selectedShortenUrl: '',
      svgCode: ''
    }
  },
  props: [
    'shortenUrls',
    'domains'
  ],
  async mounted () {
    await this.$recaptcha.init()
  },
  computed: {
    urlLen () {
      let len = this.$store.state.authUser ? 0 : 1
      switch (this.selectedPeriod) {
        case 'hour':
          len += 2
          break
        case 'days':
          len += 3
          break
        case 'month':
          len += 4
          break
        default:
          return '-'
      }
      return this.$t('message.domainPlus') + String(len)
    },
    isAllValid () {
      return this.isOriginalUrlValid && this.isDomainValid && this.isPeriodValid
    },
    isPeriodValid () {
      return this.period.includes(this.selectedPeriod)
    },
    isDomainValid () {
      return this.domains.includes(this.selectedDomain)
    },
    isOriginalUrlValid () {
      if (this.selectedOriginalUrl === '') {
        return null
      }
      /* eslint no-useless-escape: 0 */
      return /^(http\:\/\/|https\:\/\/)(.{1,})\.(.{2,})$/.test(this.selectedOriginalUrl)
    }
  },
  watch: {
    selectedDomain () {
      if (this.selectedDomain === '') { return }
      this.period = this.selectedDomain.period
      if (!this.isPeriodValid) {
        this.selectedPeriod = ''
      }
    }
  },
  methods: {
    validateAll () {
      return true
    },
    async onClickCreate () {
      this.inProgress = true
      const data = {
        original: this.selectedOriginalUrl,
        period: this.selectedPeriod,
        recaptcha: await this.$recaptcha.execute('create'),
        domain_id: this.selectedDomain.pk
      }
      this.$axios.post('/api/urls/', data)
        .then((res) => {
          this.initData()
          this.updateUrls()
          this.inProgress = false
        }).catch((e) => {
          this.inProgress = false
          console.log(e.response)
          if (!e.response.data.status) {
            this.showToast(e.response.data.message)
          }
        })
    },
    openDeleteModal (url) {
      this.delUrl = url.shorten_url
      this.isDeleteModalOpen = true
    },
    deleteUrl () {
      const params = new URLSearchParams()
      params.append('shorten_url', this.delUrl)
      this.$axios.delete('/api/urls', { data: params })
        .then(() => {
          this.updateUrls()
        })
    },
    initData () {
      this.selectedPeriod = ''
      this.selectedDomain = ''
      this.selectedOriginalUrl = ''
    },
    updateUrls () {
      this.$axios.get('/api/urls/')
        .then((res) => {
          this.shortenUrls = res.data
        })
    },
    showToast (message) {
      console.log('func')
      this.$bvToast.toast(message, {
        autoHideDelay: 2000
      })
    },
    addToClipBoard (url) {
      const temp = document.createElement('div')
      temp.appendChild(document.createElement('pre')).textContent = 'https://' + url.shorten_url
      document.body.appendChild(temp)
      document.getSelection().selectAllChildren(temp)
      if (document.execCommand('copy')) {
        this.showToast(this.$t('message.copied'))
      }
      document.body.removeChild(temp)
    },
    showQr (url) {
      this.selectedShortenUrl = url.shorten_url
      QRCode.toString(this.selectedShortenUrl, {
        type: 'svg'
      }, (error, string) => {
        console.log(error)
        this.svgCode = string
      })
      this.isQrViewModalOpen = true
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
