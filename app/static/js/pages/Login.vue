<template>
  <div>
    <router-link :to="{ name: 'landing' }">Landing page</router-link>
    <h1>Login page</h1>
    <p v-if="formError">ERROR: {{ formError }}</p>
    <div>
      <input type="email" v-model="email" placeholder="email" />

      <p v-if="fieldErrors.email">ERROR: {{ fieldErrors.email }}</p>
    </div>
    <div>
      <input type="password" v-model="password" placeholder="password" />

      <p v-if="fieldErrors.password">ERROR: {{ fieldErrors.password }}</p>
    </div>
    <button @click="login">Log in</button>
  </div>
</template>

<script>
  import Actions from "~/actions";

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
      login: function() {
        Actions.login(this.email, this.password)
          .then(() => alert("Logged in successfully"))
          .catch((resp) => {
            this.formError = resp.formError;
            this.fieldErrors = resp.fieldErrors;
          })
          .catch((error) => {
            console.log(error);
          });
      }
    }
  };
</script>