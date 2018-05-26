import React from "react";
import SerializeForm from "@f/serialize-form";

import Modal from "./Modal";


export default class RegisterModal extends React.Component {
  onSubmit(e) {
    e.preventDefault();
    console.log(e.target);
    console.log(SerializeForm(e.target));
  }

  render() {
    return (
      <Modal title="Register" hideModal={ this.props.hideModal }>
        <form onSubmit={ this.onSubmit }>
          <input
            type="text"
            name="first_name"
            placeholder="First name"
            data-lpignore="true"
            required
            />

          <input
            type="text"
            name="last_name"
            placeholder="Last name (optional)"
            data-lpignore="true"
            />

          <input
            type="text"
            name="email"
            placeholder="Email"
            required
            />

          <input
            type="password"
            name="password"
            placeholder="Password"
            required
            />

          <input
            type="password"
            name="confirm_password"
            placeholder="Password (again)"
            required
            />

          <input
            type="submit"
            value="Register"
            />
        </form>
      </Modal>
    );
  }
}