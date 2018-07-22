<template>
  <div>
    <ul>
      <li>
        <router-link :to="{ name: 'landing' }">Landing Page</router-link>
      </li>
      <li v-if="!$store.state.loggedIn">
        <router-link :to="{ name: 'login' }">Log in</router-link>
      </li>

      <template v-if="$store.state.loggedIn">
        <li>
          <router-link :to="{ name: 'projects' }">Projects</router-link>
        </li>
        <li>
          <a @click.prevent="logout" href="#">Log out</a>
        </li>
      </template>
    </ul>
  </div>
</template>

<script>
  export default {
    methods: {
      /* Logs the user out and redirects them back to the login page */
      logout() {
        this.$store.dispatch("logout");
        this.$router.push({ name: "login" });
      }
    }
  }
</script>