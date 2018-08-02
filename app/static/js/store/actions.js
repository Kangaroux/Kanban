import Axios from "axios";
import Promise from "promise";
import Qs from "qs";
import Transform from "./transform";


export default {
  /* Verifies the user's credentials and then loads the user's data */
  login({ commit }, { email, password }) {
    return new Promise((resolve, reject) => {
      Axios.post(API.session, Qs.stringify({ email, password }))
      .then((resp) => {
        commit("login", Transform.user(resp.data.user));

        // Load the user's data
        dispatch("loadAppData")
        .then((resp) => resolve(resp))
        .catch((err) => reject(err));
      })
      .catch((err) => reject(Transform.form(err)));
    });
  },

  /* Logs the user out */
  logout({ commit, state }) {
    return new Promise((resolve, reject) => {
      if(!state.loggedIn) {
        resolve();
        return;
      }

      Axios.delete(API.session)
      .then((resp) => {
        commit("logout");
        resolve();
      })
      .catch((err) => {
        console.error(err)
        reject();
      });
    });
  },

  /* Checks if the user is logged in and then loads their data */
  loadSession({ commit, dispatch }) {
    return new Promise((resolve, reject) => {
      Axios.get(API.session)
      .then((resp) => {
        if(resp.data.logged_in) {
          commit("login", Transform.user(resp.data.user));
          commit("ready", "session");
          dispatch("loadAppData");
          resolve();
        } else {
          commit("ready", "session");
          resolve();
        }
      })
      .catch((err) => {
        console.error(err);
        reject();
      });
    });
  },

  /* Loads the current user and their projects */
  loadAppData({ commit, dispatch }) {
    return Promise.all([
      dispatch("getAllProjects")
    ]);
  },

  /* Creates a new project */
  createProject({ commit }, { name, description }) {
    return new Promise((resolve, reject) => {
      Axios.post(API.project, Qs.stringify({ name, description }))
      .then((resp) => {
        const project = Transform.project(resp.data.project);
        commit("addProject", project);
        resolve(project);
      })
      .catch((err) => reject(Transform.form(err)));
    });
  },

  /* Gets all projects the current user has access to */
  getAllProjects({ commit }) {
    return new Promise((resolve, reject) => {
      Axios.get(API.project)
      .then((resp) => {
        const projects = resp.data.projects.map((k) => Transform.project(k));
        commit("addProjects", projects);
        commit("ready", "projects");
        resolve();
      })
      .catch((err) => {
        console.error(err);
        reject();
      });
    });
  },

  /* Gets information about a user */
  getUser({ commit }, { userId }) {
    return new Promise((resolve, reject) => {
      Axios.get(API.user + userId)
      .then((resp) => {
        const user = Transform.user(resp.data.user);
        commit("addUser", user);
        resolve(user);
      })
      .catch((err) => {
        console.error(err);
        reject();
      });
    });
  }
};