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

function Field(props) {
  return (
    <div className="field-group">
      { props.children }
      <FieldError error={ props.error } />
    </div>
  );
}


export {
  Field,
  FieldError
};