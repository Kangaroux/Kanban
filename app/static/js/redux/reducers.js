import { List, Map } from "immutable";
import { combineReducers } from "redux-immutable";

import { actions } from "./actions";
import RegisterModal from "~/components/modals/RegisterModal";


function currentModal(state = null, action) {
  switch(action.type) {
    case actions.SHOW_MODAL:
      let modal;

      if(action.name === "register")
        modal = RegisterModal;
      else
        throw Error("Unknown modal name: " + action.name);

      return Map({
        component: modal,
        props: action.props
      });

    case actions.HIDE_MODAL:
      return null;

    default:
      return state;
  }
}


export default combineReducers({
  currentModal
});