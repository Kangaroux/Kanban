import Actions from "./actions";
import Vue from "vue";
import Vuex from "vuex";


function createStore() {
  return new Vuex.Store({
    state: {
      loggedIn: false,
      ready: false,
      projects: {},
      user: null,
      users: {}
    },

    mutations: {
      addProject(state, project) {
        Vue.set(state.projects, project.id, project);
      },

      addProjects(state, projects) {
        for(let project of projects)
          Vue.set(state.projects, project.id, project);
      },

      addUser(state, user) {
        Vue.set(state.users, user.id, user);
      },

      login(state, user) {
        Vue.set(state.users, user.id, user);
        state.user = user;
        state.loggedIn = true;
      },

      logout(state) {
        state.user = null;
        state.loggedIn = false;
      },

      ready(state) {
        state.ready = true;
      }
    },

    actions: Actions
  });
}

export default createStore;