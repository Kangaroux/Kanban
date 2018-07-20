import "./config";
import Vue from "vue";
import Vuex from "vuex";
import VueRouter from "vue-router";
import router from "./routes";

Vue.use(Vuex);
Vue.use(VueRouter);

const store = new Vuex.Store({
  state: {
    user: null
  },
  mutations: {
    setUser(user) {
      state.user = user;
    }
  }
});

const app = new Vue({
  el: "#app",
  router,
  store
});