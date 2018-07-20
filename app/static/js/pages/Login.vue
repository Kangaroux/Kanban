<template>
  <div>
    <router-link :to="{ name: 'landing' }">Landing page</router-link>
    <h1>Login page</h1>
    <input type="email" v-model="email" placeholder="email" />
    <input type="password" v-model="password" placeholder="password" />
    <button @click="login">Log in</button>
  </div>
</template>

<script>
  export default {
    data: () => {
      return {
        email: "",
        password: ""
      };
    }
  };
</script>