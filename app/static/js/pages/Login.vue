<template>
  <div>
    <h1>Login page</h1>
    <p v-if="formError">ERROR: {{ formError }}</p>
    <form @submit.prevent="login">
      <div>
        <input type="email" v-model="email" placeholder="email" />

        <p v-if="fieldErrors.email">ERROR: {{ fieldErrors.email }}</p>
      </div>
      <div>
        <input type="password" v-model="password" placeholder="password" />

        <p v-if="fieldErrors.password">ERROR: {{ fieldErrors.password }}</p>
      </div>
      <input type="submit" value="Log in" />
    </form>
  </div>
</template>

<script>
  export default {
    data: () => {
      return {
        email: "",
        password: "",
        formError: "",
        fieldErrors: {},
      };
    },
    methods: {
      login() {
        this.$store.dispatch("login", {
          email: this.email,
          password: this.password
        })
        .then(() => {
          this.$router.push({ path: "projects" });
        })
        .catch((error) => {
          this.formError = error.formError;
          this.fieldErrors = error.fieldErrors;
        });
      }
    }
  };
</script>