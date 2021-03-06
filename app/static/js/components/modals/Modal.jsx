import React from "react";

import { hideModal } from "~/redux/actions";
import store from "~/redux/store";


/*
  Props:
  - hideModal: Function which is called when the close button is pressed.
*/
class Modal extends React.Component {
  render() {
    return (
      <div className="modal">
        <div className="modal-content">
          <div className="modal-header">
            <div className="modal-title">{ this.props.title }</div>
            <span className="modal-close" onClick={ this.props.hideModal }>X</span>
          </div>
          <div className="modal-body">
            { this.props.children }
          </div>
        </div>
      </div>
    );
  }
}


export default Modal;