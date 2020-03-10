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
            class="my-2">
            <b-button
              class="nav-btn"
              id="popover-target-1">
              New
            </b-button>
            <b-popover
              target="popover-target-1"
              triggers="hover"
              placement="auto">
              title
            </b-popover>
          </div>
          <b-nav-item-dropdown
            :text="$t('common.lang')"
            right>
            <b-dropdown-item :href="switchLocalePath('en')">EN</b-dropdown-item>
            <b-dropdown-item :href="switchLocalePath('ja')">JA</b-dropdown-item>
          </b-nav-item-dropdown>

          <b-nav-item right>
            <b-btn variant="info" class="nav-btn"> {{ $t('common.login') }} </b-btn>
          </b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </section>
</template>

<script>

export default {
}
</script>

<style scoped>
.nav-btn {
    width: 100%;
}
.logo-img {
    width:180px;
}
</style>
