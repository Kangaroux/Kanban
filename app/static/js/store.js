import Axios from "axios";
import Promise from "promise";
import Qs from "qs";
import Vuex from "vuex";
import Transform from "./transform";


function createStore() {
  return new Vuex.Store({
    state: {
      loggedIn: false,
      projects: [],
      user: null,
    },

    mutations: {
      addProject(state, project) {
        state.projects.push(project)
      },

      addProjects(state, projects) {
        state.projects.concat(projects);
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

    actions: {
      /* Tries to log the user in and if successful sets the user in the store */
      login({ commit }, { email, password }) {
        return new Promise((resolve, reject) => {
          Axios.post(API.session, Qs.stringify({ email, password }))
          .then((resp) => {
            commit("login", Transform.user(resp.data.user));
            resolve();
          })
          .catch((err) => reject(Transform.form(err)));
        });
      },

      /* Logs the user out */
      logout({ commit, state }) {
        if(!state.loggedIn)
          return;

        Axios.delete(API.session)
        .then((resp) => commit("logout"))
        .catch((err) => console.error(err));
      },

      /* Loads the user's session */
      loadSession({ commit }) {
        Axios.get(API.session)
        .then((resp) => {
          if(resp.data.logged_in)
            commit("login", Transform.user(resp.data.user))
        })
        .catch((err) => console.error(err));
      },

      /* Creates a new project */
      createProject({ commit }, { name, description }) {
        return new Promise((resolve, reject) => {
          Axios.post(API.project, Qs.stringify({ name, description }))
          .then((resp) => {
            commit("addProject", Transform.project(resp.data.project));
            resolve();
          })
          .catch((err) => reject(Transform.form(err)));
        });
      },

      /* Gets all projects the current user is a member of */
      getAllProjects({ commit }) {
        return new Promise((resolve, reject) => {
          Axios.get(API.project)
          .then((resp) => {
            commit("addProjects", Transform.project(resp.data.projects));
            resolve();
          })
          .catch((err) => {
            console.error(err);
            reject();
          });
        });
      }
    }
  });
}

export default createStore;