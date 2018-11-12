<template>
  <b-card
    style="max-width: 600px"
    class="mx-auto my-3">
    <b-input-group prepend="original URL">
      <b-form-input
        for="type-url"/>
    </b-input-group>
    <b-form-radio-group
      id="radios2"
      v-model="selected"
      class="my-2 float-none"
      name="radioSubComponent">
      <b-form-radio value="hour">3hour</b-form-radio>
      <b-form-radio value="days">5Days</b-form-radio>
      <b-form-radio value="month">5Month</b-form-radio>
    </b-form-radio-group>
    <font-awesome-icon
      v-b-tooltip.hover
      :icon="['far', 'question-circle']"
      size="lg"
      title="When you log in, url is shortened by one character!"
      class="mx-auto my-auto px-auto"/> 
    <b-input-group
      id="shorturl"
      prepend="short URL"
      class="float-left mr-1">
      <b-form-input
        :value="url"
        readonly="isLogin"/>
    </b-input-group>
    <b-btn 
      variant="info"
      class="float-right">create</b-btn>
  </b-card>
</template>
<script>
export default {
  data(){
    return {
      isLogin: true,
      url: '',
      selected: 'hour'
    }
  },
  watch: {
    selected: function(){
      this.url = '22ur.tk/' + '0'.repeat(this.urllen())
    }
  },
  created: function(){
    this.url = '22ur.tk/' + '0'.repeat(this.urllen())
  },
  methods: {
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
      if (!this.isLogin) len++
      return len
    }
  }
}
</script>
<style scoped>
#shorturl {
  max-width: 65%;
}
</style>


