<template>
  <div>
    <h1>Create board page</h1>
    <router-link :to="{ name: 'projects:view', params: { id: project().id } }">
      Go back to project
    </router-link>
  </div>
</template>

<script>
  const board = () => this.$store.state.boards[this.id];

  export default {
    props: {
      id: Number
    },
    computed: {
      project() {
        const board = this.$store.state.boards[this.id];
        return this.$store.state.projects[board.project];
      },

      board() {
        return this.$store.state.boards[this.id];
      }
    }
  };
</script>