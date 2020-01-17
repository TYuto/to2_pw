<template>
  <b-card
    style="max-width: 700px"
    class="mx-auto my-3">
    <b-input-group prepend="短縮元 URL">
      <b-form-input
        v-model="originalUrl"
        :state="varridate"
        for="type-url"/>
    </b-input-group>
    <b-dropdown
      :text="selectedDomain.host"
      variant="info">
      <b-dropdown-item
        v-for="domain in domains"
        :key="domain.host"
        @click="onSelectDomain(domain)"
      >{{ domain.host }}</b-dropdown-item>
    </b-dropdown>
    <b-form-radio-group
      id="radios2"
      v-model="selected"
      class="my-2 float-none"
      name="radioSubComponent">
      <b-form-radio
        :disabled="!selectedDomain.enable_hour"
        value="hour"
      >3時間</b-form-radio>
      <b-form-radio
        :disabled="!selectedDomain.enable_week"
        value="days"
      >5日間</b-form-radio>
      <b-form-radio
        :disabled="!selectedDomain.enable_months"
        value="month"
      >5ヶ月間</b-form-radio>
    </b-form-radio-group>
    <font-awesome-icon
      v-b-tooltip.hover
      :icon="['far', 'question-circle']"
      size="lg"
      title="ログインすると1文字短い短縮URLを作成できるようになります"
      class="mx-auto my-auto px-auto"/> 
    <b-input-group
      id="shorturl"
      prepend="短縮後 url"
      class="float-left mr-1">
      <b-form-input
        :value="url"
        :readonly="true"/>
    </b-input-group>
    <b-btn 
      variant="info"
      class="float-right"
      @click="create">作成</b-btn>
  </b-card>
</template>
<script>
import axios from 'axios'
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
export default {
  data: function(){
    return {
      url: '',
      originalUrl: '',
      selected: 'hour',
      varridate: null,
      recaptcha: '',
      domains: [],
      selectedDomain: { host: ''},
    }
  },
  watch: {
    selected: function(){
      this.resetUrl()
    },
    originalUrl: function(){
      this.varridate = /^(http\:\/\/|https\:\/\/)(.{4,})$/.test(this.originalUrl)
      this.resetUrl()
    },
    selectedDomain:function() {
      this.resetUrl()
      this.selected = 'hour'
    }
  },
  mounted: async function() {
    this.initDomains()
    await this.$recaptcha.init()
    await this.updateRecaptcha()
  },
  methods: {
    resetUrl: function() {
      this.url = this.selectedDomain.host + 'o'.repeat(this.urllen())
    },
    initDomains: function() {
      axios.get('/api/domains/').then(response =>{
        this.domains = response.data
        this.selectedDomain = response.data[0]
      })
    },
    onSelectDomain: function(domain) {
      this.selectedDomain = domain
    },
    urllen: function(){
      let len = 0
      switch(this.selected){
        case 'hour':
          len = 2
          break
        case 'days':
          len = 3
          break
        case 'month':
          len = 4
      }
      if (!this.$store.state.authUser) len++
      return len
    },
    create: async function(){
      if (!this.varridate){ 
        alert('有効なURLを入力してください')
        return
      }
      let data = {
        original: this.originalUrl,
        period: this.selected,
        recaptcha: this.recaptcha,
        domain_id: this.selectedDomain.pk,
      }
      axios.post('/api/urls/',data)
      .then(response => {
        if (response.data.status){
            this.url = response.data.shorten_url
            this.$emit('create', {shorten_url: this.url, original_url: this.originalUrl})
            this.updateRecaptcha()
        } else {
          alert(response.data.message)
        }
      })
    },
    updateRecaptcha: async function() {
      this.recaptcha = await this.$recaptcha.execute('create')
    }
  }
}
</script>
<style scoped>
#shorturl {
  max-width: 65%;
}
</style>


