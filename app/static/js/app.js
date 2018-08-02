import "./config";
import Vue from "vue";
import Vuex from "vuex";
import VueRouter from "vue-router";


Vue.use(Vuex);
Vue.use(VueRouter);

import router from "./routes";
import createStore from "./store/store";

window.store = createStore();
const app = new Vue({
  router,
  store
});

// Load the user's session and destroy the loading placeholder
store.dispatch("loadSession")
.then(() => {
  const $el = document.getElementById("app");
  $el.innerHTML = "<router-view></router-view>";

  document.getElementById("loading-placeholder").remove();
  app.$mount($el);
});