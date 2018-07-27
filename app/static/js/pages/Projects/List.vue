<template>
  <div>
    <h1>Projects page</h1>
    <router-link :to="{ name: 'createProject' }">Create project</router-link>

    <Form :submit="createProject">
      <TextInput
        v-model="name"
        placeholder="name"
        :fieldError="fieldErrors.name"
        />
      <TextInput
        v-model="description"
        placeholder="description"
        :fieldError="fieldErrors.description"
        />
    </Form>
  </div>
</template>

<script>
  import Form from "~/components/Form";
  import TextInput from "~/components/TextInput";

  export default {
    components: { Form, TextInput },

    data() {
      return {
        name: "",
        description: "",
        formError: "",
        fieldErrors: {}
      };
    },

    methods: {
      createProject() {
        this.$store.dispatch("createProject", {
          name,
          description
        })
        .then(() => this.$router.push({ path: "projects" }))
        .catch((err) => {
          this.formError = err.formError;
          this.fieldErrors = err.fieldErrors;
        });
      }
    }
  };
</script>