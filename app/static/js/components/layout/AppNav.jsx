import React from "react";

import modals from "app";
import { showModal } from "redux/actions";
import store from "redux/store";


export default class AppNav extends React.Component {
  render() {
    return (
      <div className="nav-container">
        <div className="nav-title">Kanban</div>

        <ul className="nav-items">
          <li className="nav-item">
            <a className="btn btn-brand-outline"
            onClick={ () => store.dispatch(showModal("register"))}>
              Register
            </a>
          </li>
        </ul>
      </div>
    );
  }
}
