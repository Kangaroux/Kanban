import Serialize from "@f/serialize_form";
import React from "react";


class Form extends React.Component {
  onSubmit(e) {
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