import { connect } from "react-redux";

import AppRoot from "~/components/layout/AppRoot";
import { hideModal, showModal } from "~/redux/actions";
import { currentModal } from "~/redux/selectors";


function mapStateToProps(state) {
  return {
    modal: currentModal(state)
  };
}

function mapDispatchToProps(dispatch) {
  return {
    hideModal: () => dispatch(hideModal()),
    showModal: (component, props) => dispatch(showModal(component, props)),
  };
}


export default connect(
  mapStateToProps,
  mapDispatchToProps
)(AppRoot);