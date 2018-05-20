import "./layout/app-nav";
import "./modals/test-modal";
import { pushModal } from "../redux/actions";
import { selectModal } from "../redux/selectors";
import store from "../redux/store";

<app-root>
  <app-nav />

  <!-- Render the top modal on the stack if there is one -->
  <virtual if={ this.currentModal }>
    <div class="dimmer"></div>
    <test-modal show={ this.currentModal.name === 'test-modal' } />
  </virtual>

  <script>
    this.on("mount", () => {
      this.unsubscribe = store.subscribe(() => this.handleUpdate(store.getState()));
      store.dispatch(pushModal("test-modal", null));
    });

    this.on("unmount", () => {
      this.unsubscribe();
    });

    handleUpdate(state) {
      this.update({
        currentModal: selectModal(state)
      });
    }
  </script>
</app-root>