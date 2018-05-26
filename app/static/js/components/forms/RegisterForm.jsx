import React from "react";
import Serialize from "@f/serialize-form";

import { hideModal } from "~/redux/actions";
import Store from "~/redux/store";
import { registerUser } from "~/actions";
import PasswordField from "./fields/PasswordField";
import TextField from "./fields/TextField";


class RegisterForm extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      fieldErrors: {},
      formError: null
    };
  }

  onSubmit(e) {
    e.preventDefault();

    registerUser(Serialize(e.target))
      .then(() => Store.dispatch(hideModal()))
      .catch((err) => {
        this.setState({
          formError: err.msg,
          fieldErrors: err.fields,
        });
      });
  }

  render() {
    const err = this.state.fieldErrors;

    return (
      <form onSubmit={ (e) => this.onSubmit(e) } className="form-tight">
        { this.state.formError &&
          <p className="text-danger">{ this.state.formError }</p>
        }

        <TextField name="first_name" placeholder="First Name" lpignore={ true }
          error={ err.first_name } />
        <TextField name="last_name" placeholder="Last Name (optional)" lpignore={ true }
          error={ err.last_name } />
        <TextField name="email" placeholder="Email" error={ err.email } />
        <PasswordField name="password" placeholder="Password" error={ err.password } />
        <PasswordField name="confirm_password" placeholder="Password (again)"
          error={ err.confirm_password } />

        <div className="button-group">
          <input className="btn btn-block" type="submit" value="Create Account" />
        </div>
      </form>
    );
  }
}


export default RegisterForm;