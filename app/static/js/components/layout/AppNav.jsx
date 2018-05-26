import React from "react";

import Modals from "~/modals";
import { showModal } from "~/redux/actions";
import Store from "~/redux/store";


class AppNav extends React.Component {
  render() {
    return (
      <div className="nav-container">
        <div className="nav-title">Kanban</div>

        <ul className="nav-items">
          <li className="nav-item">
            <a className="btn btn-brand-outline"
            onClick={ () => Store.dispatch(showModal(Modals.REGISTER))}>
              Register
            </a>
          </li>
        </ul>
      </div>
    );
  }
}


export default AppNav;