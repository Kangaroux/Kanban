import React from "react";

import AppNav from "components/layout/AppNav";

const Fragment = React.Fragment;


export default class AppRoot extends React.Component {
  renderModal() {
    let modal = this.props.modal.component;
    let modalProps = this.props.modal.props;

    // Pass an `onHideModal` prop that the modal can call to hide itself
    modalProps.onHideModal = this.props.hideModal;

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