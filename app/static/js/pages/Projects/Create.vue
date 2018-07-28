<template>
  <div>
    <h1>Create project page</h1>

    <Form :formError="formError" @submit="createProject">
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
      <input type="submit" value="Create Project" />
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
          name: this.name,
          description: this.description
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