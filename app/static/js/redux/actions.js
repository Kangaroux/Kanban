const actions = {
  PUSH_MODAL: "PUSH_MODAL",
  POP_MODAL: "POP_MODAL",
};

/*
  Pushes a modal on the stack. The modal component with the given name will be
  rendered with the given opts.
*/
function pushModal(name, opts) {
  return {
    type: actions.PUSH_MODAL,
    name,
    opts,
  }
}

/*
  Hides the top modal on the stack.
*/
function hideModal() {
  return {
    type: actions.POP_MODAL
  }
}


module.exports = Object.assign(actions, {
  pushModal,
  hideModal
});