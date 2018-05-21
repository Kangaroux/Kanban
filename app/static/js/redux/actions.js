const actions = {
  SHOW_MODAL: "SHOW_MODAL",
  HIDE_MODAL: "HIDE_MODAL",
};

function showModal(name, props = {}) {
  return {
    type: actions.SHOW_MODAL,
    name,
    props,
  };
}

function hideModal() {
  return {
    type: actions.HIDE_MODAL
  };
}


export {
  actions,
  showModal,
  hideModal
};