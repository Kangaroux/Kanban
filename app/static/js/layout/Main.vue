<template>
  <div>
    <Loading v-if="!$store.state.ready" />

    <template v-else>
      <AppNav />
      <router-view></router-view>
    </template>
  </div>
</template>

<script>
  import AppNav from "~/components/AppNav";
  import Loading from "~/views/Loading";

  export default {
    components: { AppNav, Loading }
  };
</script>