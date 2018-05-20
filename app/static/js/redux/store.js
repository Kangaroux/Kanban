import { Map } from "immutable";
import { createStore } from "redux";

import reducers from "./reducers";

module.exports = createStore(reducers, Map());