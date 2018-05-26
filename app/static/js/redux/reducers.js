import { List, Map } from "immutable";
import { combineReducers } from "redux-immutable";

import { actions } from "./actions";
import RegisterModal from "~/components/modals/RegisterModal";


function currentModal(state = null, action) {
  switch(action.type) {
    case actions.SHOW_MODAL:
      return Map({
        component: action.component,
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