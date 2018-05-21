import React from "react";

import Modal from "./Modal";


export default class RegisterModal extends React.Component {
  render() {
    return (
      <Modal title="Register" hideModal={ this.props.hideModal }>
        Some text in the register modal, wowzah
        <input />
      </Modal>
    );
  }
}