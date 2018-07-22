import Axios from "axios";
import Promise from "promise";
import Qs from "qs";
import Vuex from "vuex";
import Util from "./util";


function createStore() {
  return new Vuex.Store({
    state: {
      loggedIn: false,
      user: null,

      projects: [],
    },
    mutations: {
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
      login({ commit }, { email, password }) {
        return new Promise((resolve, reject) => {
          Axios.post(API.session, Qs.stringify({ email, password }))
          .then((resp) => {
            commit("login", resp.data.user);
            resolve();
          })
          .catch((err) => reject(Util.formError(err)));
        });
      },

      getSession({ commit }) {
        Axios.get(API.session)
        .then((resp) => commit("login", resp.data.user))
        .catch((err) => console.error(err));
      }
    }
  });
}

export default createStore;