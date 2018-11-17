<template>
  <section>
    <b-btn
      v-b-modal.loginModal
      variant="info">login</b-btn>
    <b-modal 
      id="loginModal"
      title="login"
      hide-footer>
      <div class="login-btn my-1 mx-auto">
        <b-button
          variant="outline-primary"
          href="/auth/login/twitter">
          <font-awesome-icon :icon="['fab', 'twitter']" /> 
          login with Twitter
        </b-button>
      </div>
      <div class="login-btn my-1 mx-auto">
        <b-button variant="outline-danger">
          <font-awesome-icon :icon="['fab', 'google']" /> 
          login with Google
        </b-button>
      </div>
      <div class="login-btn my-1 mx-auto">
        <b-button variant="outline-dark">
          <font-awesome-icon :icon="['fab', 'github']" /> 
          login with Github
        </b-button>
      </div>
    </b-modal>
  </section>
</template>
<script>
export default {
    
}
</script>
<style scoped>
.login-btn {
  max-width: 400px;
}
.btn {width:100%;}
</style>


