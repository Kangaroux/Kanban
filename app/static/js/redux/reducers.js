import { List, Map } from "immutable";
import { combineReducers } from "redux-immutable";

import { PUSH_MODAL, POP_MODAL } from "./actions";


function modals(state = List(), action) {
  switch(action.type) {
    case PUSH_MODAL:
      return state.push(Map({
        name: action.name,
        opts: action.opts
      }));

    case POP_MODAL:
      return state.pop();

    default:
      return state;
  }
}


module.exports = combineReducers({
  modals
});