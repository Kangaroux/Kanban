import VueRouter from "vue-router";


const routes = [
  {
    path: "/",
    component: require("./layout/Main").default,
    children: [
      {
        name: "landing",
        path: "",
        component: require("./pages/Landing").default,
        meta: {
          title: "Landing Page"
        }
      },
      {
        name: "login",
        path: "login",
        component: require("./pages/Login").default,
        meta: {
          title: "Login Page"
        }
      },
      {
        name: "projects",
        path: "projects",
        component: require("./pages/Projects").default,
        meta: {
          title: "Projects Page",
          loginRequired: true
        }
      },
    ]
  }
];

const router = new VueRouter({ routes });

router.beforeEach((to, from, next) => {
  // Redirect the user to the login page if they try to visit a page and aren't
  // logged in
  if(to.meta.loginRequired && !window.store.state.loggedIn) {
    next({ name: "login" });
  } else {
    next();
  }
});

router.afterEach((to, from) => {
  // Set the page title when the route changes
  document.title = to.meta.title;
});

export default router;