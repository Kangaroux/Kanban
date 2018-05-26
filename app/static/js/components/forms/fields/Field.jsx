import React from "react";


function FieldError(props) {
  if(!props.error)
    return null;

  return (
    <div className="field-error">
      { props.error }
    </div>
  );
}

class Field extends React.Component {
  render() {
    const cls = [
      "field-group",
      this.props.className || "",
      this.props.error ? "field-group-error" : ""
    ];

    return (
      <div className={ cls.join(" ") }>
        { this.props.children }
        <FieldError error={ this.props.error } />
      </div>
    );
  }
}


export {
  Field,
  FieldError
};