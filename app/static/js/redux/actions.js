export const actions = {
  SHOW_MODAL: "SHOW_MODAL",
  HIDE_MODAL: "HIDE_MODAL",
};


export function showModal(component, props = {}) {
  return {
    type: actions.SHOW_MODAL,
    component,
    props,
  };
}

export function hideModal() {
  return {
    type: actions.HIDE_MODAL
  };
}