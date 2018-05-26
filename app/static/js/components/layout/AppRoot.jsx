import React from "react";

import AppNav from "./AppNav";

const Fragment = React.Fragment;


class AppRoot extends React.Component {
  renderModal() {
    let modal = this.props.modal.component;
    let modalProps = this.props.modal.props;

    // Pass a `hideModal` prop that the modal can call to hide itself
    modalProps.hideModal = this.props.hideModal;


    return (
      <Fragment>
        <div className="dimmer" onClick={ this.props.hideModal }></div>
        { React.createElement(modal, modalProps) }
      </Fragment>
    );
  }

  render() {
    return (
      <div className="root">
        { this.props.modal && this.renderModal() }

        <AppNav onShowModal={ this.props.showModal } />
      </div>
    );
  }
}


export default AppRoot;