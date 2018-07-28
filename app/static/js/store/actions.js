import Axios from "axios";
import Promise from "promise";
import Qs from "qs";
import Transform from "./transform";


export default {
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

  /* Loads the user's session. This checks if the user is logged in and, if
  they are, grabs their user data and also preloads some project metadata
  */
  loadSession({ commit, dispatch }) {
    return new Promise((resolve, reject) => {
      Axios.get(API.session)
      .then((resp) => {
        if(resp.data.logged_in) {
          dispatch("getUser", { userId: resp.data.user_id })
          .then((user) => {
            commit("login", user);
            dispatch("getAllProjects");
            resolve();
          });
        } else {
          resolve();
        }
      })
      .catch((err) => {
        console.error(err);
        reject();
      });
    });
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

  /* Gets all projects the current user has access to */
  getAllProjects({ commit }) {
    return new Promise((resolve, reject) => {
      Axios.get(API.project)
      .then((resp) => {
        const projects = resp.data.projects.map((k) => Transform.project(k));
        commit("addProjects", projects);
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