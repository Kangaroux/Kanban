import React from "react";
import Serialize from "@f/serialize-form";

import TextField from "./fields/TextField";
import PasswordField from "./fields/PasswordField";


class RegisterForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  onSubmit(e) {
    e.preventDefault();
    console.log(Serialize(e.target));
  }

  render() {
    return (
      <form onSubmit={ this.onSubmit }>
        <TextField name="first_name" placeholder="First Name" lpignore={ true } />
        <TextField name="last_name" placeholder="Last Name (optional)" lpignore={ true } />
        <TextField name="email" placeholder="Email" />
        <PasswordField name="password" placeholder="Password" />
        <PasswordField name="confirm_password" placeholder="Password (again)" />

        <input type="submit" />
      </form>
    );
  }
}


export default RegisterForm;