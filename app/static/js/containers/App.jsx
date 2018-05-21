import { connect } from "react-redux";

import AppRoot from "./AppRoot";
import { hideModal } from "redux/actions";
import { currentModal } from "redux/selectors";


function mapStateToProps(state) {
  return {
    modal: currentModal(state)
  };
}

function mapDispatchToProps(dispatch) {
  return {
    closeModal: () => dispatch(hideModal())
  };
}


export default connect(
  mapStateToProps,
  mapDispatchToProps
)(AppRoot);