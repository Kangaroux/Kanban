<template>
  <div>
    <AppNav />
    <router-view></router-view>
  </div>
</template>

<script>
  import AppNav from "~/components/AppNav";

  export default {
    components: { AppNav }
  };
</script>