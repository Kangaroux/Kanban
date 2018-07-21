import "./config";
import Vue from "vue";
import Vuex from "vuex";
import VueRouter from "vue-router";


Vue.use(Vuex);
Vue.use(VueRouter);

import router from "./routes";
import createStore from "./store";

const store = createStore();
const app = new Vue({
  el: "#app",
  router,
  store
});