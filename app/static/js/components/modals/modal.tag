import { hideModal } from "redux/actions";
import store from "redux/store";


<!--
Options:

onClose :: (optional) Function that is called when the user requests to close the modal.
                      The function must return true for the modal to close
 -->
<modal>
  <div class="modal">
    <div class="modal-content">
      <div class="modal-header">
        <div class="modal-title">{ opts.title }</div>
        <span class="modal-close" onClick={ this.onClose }>X</span>
      </div>
        <div class="modal-body">
          <yield />
        </div>
      </div>
    </div>
  </div>

  <script>
    onClose() {
      if(!opts.onClose || opts.onClose())
        store.dispatch(hideModal());
    }
  </script>
</modal>