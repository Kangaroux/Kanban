import Axios from "axios";
import React from "react";
import ReactDOM from "react-dom";
import { Provider } from "react-redux";

import store from "~/redux/store";
import App from "~/containers/App";


Axios.defaults.headers.common["X-CSRFToken"] = document.getElementsByName("csrftoken")[0].content;


ReactDOM.render(
  <Provider store={ store }>
    <App />
  </Provider>,
  document.getElementById("app-root")
);