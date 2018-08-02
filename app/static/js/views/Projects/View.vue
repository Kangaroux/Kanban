<template>
  <div>
    <h1>{{ project.name }}</h1>
    <p>{{ project.description }}</p>
  </div>
</template>

<script>
  export default {
    props: {
      id: Number
    },
    computed: {
      project() {
        return this.$store.state.projects[this.id];
      }
    }
  };
</script>