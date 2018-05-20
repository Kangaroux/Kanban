import { createSelector } from "reselect";


const selectModal = createSelector(
    state => state.get("modals").last(),
    modal => modal ? modal.toJS() : null
  );


module.exports = {
  selectModal,
}