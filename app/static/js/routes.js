import VueRouter from "vue-router";


const routes = [
  // Root level
  {
    path: "/",
    component: require("./layout/Main").default,
    children: [
      {
        name: "landing",
        path: "",
        component: require("./views/Landing").default,
        meta: {
          title: "Landing Page"
        }
      },
      {
        name: "login",
        path: "login",
        component: require("./views/Account/Login").default,
        meta: {
          title: "Log in Page"
        }
      },
      {
        name: "logout",
        path: "logout",
        component: require("./views/Account/Logout").default,
        meta: {
          title: "Log out Page"
        }
      },
    ],
  },

  // Projects
  {
    path: "/projects",
    component: require("./layout/Main").default,
    children: [
      {
        name: "projects",
        path: "",
        component: require("./views/Projects/List").default,
        meta: {
          title: "Projects Page",
          loginRequired: true
        },
      },
      {
        name: "projects:create",
        path: "create",
        component: require("./views/Projects/Create").default,
        meta: {
          title: "Create Project Page",
          loginRequired: true
        }
      },
      {
        name: "projects:view",
        path: ":id",
        props: true,
        component: require("./views/Projects/View").default,
        meta: {
          title: "View Project Page",
          loginRequired: true
        },
      },
    ]
  }
];

const router = new VueRouter({ routes });

router.beforeEach((to, from, next) => {
  // Redirect the user to the login page if they try to visit a page and aren't
  // logged in
  if(to.meta.loginRequired && window.store.state.ready.session && !window.store.state.loggedIn) {
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