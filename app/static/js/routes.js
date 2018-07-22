import VueRouter from "vue-router";


const routes = [
  { name: "landing", path: "/", component: require("./pages/Landing").default },
  { name: "login", path: "/login", component: require("./pages/Login").default },
  { name: "projects", path: "/projects", component: require("./pages/Projects").default },
];

const pageTitles = {
  landing: "Landing Page",
  login: "Login Page",
  projects: "Projects Page",
};

const router = new VueRouter({ routes });

router.afterEach((to, from) => {
  document.title = pageTitles[to.name];
});

export default router;