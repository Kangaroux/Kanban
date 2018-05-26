import React from "react";

import Modal from "./Modal";
import RegisterForm from "../forms/RegisterForm";


class RegisterModal extends React.Component {
  onSubmit(e) {
    e.preventDefault();
    console.log(e.target);
    console.log(SerializeForm(e.target));
  }

  render() {
    return (
      <Modal title="Register" hideModal={ this.props.hideModal }>
        <RegisterForm />
      </Modal>
    );
  }
}


export default RegisterModal;