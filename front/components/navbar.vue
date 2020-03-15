<template>
  <section>
    <b-navbar
      toggleable="md"
      type="light"
      variant="light">

      <b-navbar-toggle target="nav_collapse"/>
      <a href="/">
        <img
          src="~/assets/logo.png"
          class="logo-img">
      </a>
      <b-collapse
        id="nav_collapse"
        is-nav>

        <b-navbar-nav class="ml-auto">
          <div
            v-show="notify.available"
            class="my-2">
            <b-button
              id="popover-target-1"
              @click="onClickNotify">
              New
            </b-button>
            <b-popover
              target="popover-target-1"
              triggers="hover"
              placement="auto">
              {{ notify.title }}
            </b-popover>
          </div>
          <b-nav-item-dropdown
            :text="$t('common.lang')"
            right>
            <b-dropdown-item :href="switchLocalePath('en')">EN</b-dropdown-item>
            <b-dropdown-item :href="switchLocalePath('ja')">JA</b-dropdown-item>
          </b-nav-item-dropdown>

          <b-nav-item right>
            <b-btn
              v-b-modal.loginModal
              v-if="!$store.state.authUser"
              variant="info"
              class="nav-btn"> {{ $t('common.login') }} </b-btn>
            <b-btn
              v-else
              variant="info"
              @click="$store.dispatch('logout')"> {{ $t('common.logout')}} </b-btn>
          </b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <b-modal
      id="loginModal"
      :title="$t('common.login')"
      hide-footer>
      <div class="my-3 mx-2">
        <b-button
          style="width: 100%"
          variant="outline-primary"
          href="/auth/login/twitter">
          <font-awesome-icon :icon="['fab', 'twitter']" />
          {{ $t('common.button.loginWithTwitter')}}
        </b-button>
      </div>
      <div
        class="my-3 mx-2">
        <b-button
          style="width: 100%"
          variant="outline-dark"
          href="/auth/login/github">
          <font-awesome-icon :icon="['fab', 'github']" />
          {{ $t('common.button.loginWithGithub') }}
        </b-button>
      </div>
    </b-modal>
  </section>
</template>

<script>

export default {
  data () {
    return {
      notify: {
        available: false,
        title: '',
        url: ''
      }
    }
  },
  async mounted () {
    const entries = await this.$getEntry('newRelease', 'fields.expiredAt[gte]', (new Date()).toISOString())
    if (entries.length === 0) {
      console.log('length...')
      return
    }
    const item = entries[0].fields

    this.notify.available = true
    this.notify.title = item.title
    this.notify.url = 'release/' + item.urlString
  },
  methods: {
    onClickNotify () {
      window.location = this.notify.url
    }
  }
}
</script>

<style scoped>
.nav-btn {
    width: 100%;
}
.logo-img {
    width:135px;
}
</style>
