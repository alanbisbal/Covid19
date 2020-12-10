<template>
  <div>
    <!-- recaptcha -->
    <vue-recaptcha
      sitekey="6LeWSfwZAAAAAKK3wJ9QBRpE4ZxnxskEZZMTZz43"
      :loadRecaptchaScript="true"
      v-on:verify="onCaptchaCheck"
    >
    </vue-recaptcha>

    <p v-if="!captchacheck" variant="danger"></p>
    <p v-else variant="success"></p>

    <b-button type="submit" variant="primary" :disabled="!captchacheck"
      >Crear</b-button
    >
    <b-button type="reset" variant="danger">Limpiar</b-button>
  </div>
</template>

<script>
import VueRecaptcha from 'vue-recaptcha';
export default {
  name: 'recaptcha',
  components: {
    VueRecaptcha,
  },
  data() {
    return {
      captchacheck: false,
    };
  },
  methods: {
    onCaptchaCheck(evt) {
      if (evt) {
        this.captchacheck = true;
      }
    },
  },
};
</script>
