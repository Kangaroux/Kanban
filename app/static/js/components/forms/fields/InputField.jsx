import React from "react";

import { Field, FieldError } from "./Field";


class InputField extends React.Component {
  constructor(props) {
    super(props);
    this.state = { value: this.props.value || "" };
  }

  getClassName() {
    let cls = "field";

    if(this.props.error)
      cls += " field-error";

    return cls;
  }

  render() {
    return (
      <Field error={ this.props.error }>
        <input
          type={ this.props.type }
          name={ this.props.name }
          placeholder={ this.props.placeholder }
          className={ this.getClassName() }
          value={ this.state.value }
          onChange={ (e) => this.setState({ value: e.target.value }) }
          data-lpignore={ this.props.lpignore ? "true" : null }
          />
      </Field>
    );
  }
}


export default InputField;