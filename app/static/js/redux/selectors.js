import { createSelector } from "reselect";


const currentModal = createSelector(
    state => state.get("currentModal"),
    modal => modal ? modal.toJS() : null
  );


export {
  currentModal,
};