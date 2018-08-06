<template>
  <div>
    <p v-if="project == null">Project does not exist</p>
    <template v-else>
      <h1>{{ project.name }}</h1>
      <p>{{ project.description }}</p>

      <h2>Boards</h2>
      <p v-if="boards.length == 0">This project has no boards yet.</p>
      <ul v-else>
        <li v-for="board in boards">
          <span v-if="board == null">LOADING...</span>
          <span v-else>{{ board.name }}</span>
        </li>
      </ul>
    </template>
  </div>
</template>

<script>
  import Loading from "~/views/Loading";

  export default {
    components: {
      Loading
    },
    props: {
      id: Number
    },
    computed: {
      project() {
        return this.$store.state.projects[this.id];
      },

      boards() {
        return this.$store.state.projects[this.id].boards.map(
          (boardId) => this.$store.state.boards[boardId]);
      }
    },
    beforeMount() {
      for(const boardId of this.$store.state.projects[this.id].boards)
        this.$store.dispatch("loadBoard", { boardId });
    }
  };
</script>