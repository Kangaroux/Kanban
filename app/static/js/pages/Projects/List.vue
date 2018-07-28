<template>
  <div>
    <h1>Projects page</h1>
    <router-link :to="{ name: 'projects:create' }">Create project</router-link>

    <p v-if="!$store.state.projects">No projects</p>
    <ul v-else>
      <li v-for="project in $store.state.projects">
        {{ project.name }}
      </li>
    </ul>
  </div>
</template>