import Actions from "./actions";
import Vuex from "vuex";


function createStore() {
  return new Vuex.Store({
    state: {
      loggedIn: false,
      projects: {},
      user: null,
      users: {}
    },

    mutations: {
      addProject(state, project) {
        state.projects[project.id] = project;
      },

      addProjects(state, projects) {
        for(let project of projects)
          state.projects[project.id] = project;
      },

      addUser(state, user) {
        state.users[user.id] = user;
      },

      login(state, user) {
        state.user = user;
        state.loggedIn = true;
      },

      logout(state) {
        state.user = null;
        state.loggedIn = false;
      }
    },

    actions: Actions
  });
}

export default createStore;