import { API_URL } from "../constraints/index_cons";
import React, { Component } from "react";
import { Modal, ModalHeader, Button, ModalFooter } from "reactstrap";
import Axios from "axios";

class ConfirmRemovalModal extends Component {
  state = {
    modal: false,
  };
  toggle = () => {
    this.setState((pervious) => ({
      modal: !pervious.modal,
    }));
  };
  deleteStudent = (pk) => {
    Axios.delete(API_URL + pk).then(() => {
      this.props.resetState();
      this.toggle();
    });
  };
  render() {
    return (
      <Modal>
        <Button>Remove</Button>
        <ModalHeader>Do you really want delete the results</ModalHeader>

        <ModalFooter>
          <Button type="button" onClick={() => this.toggle()}>
            Cancel
          </Button>
          <Button
            type="button"
            color="primary"
            onClick={() => this.deleteStudent(this.props.pk)}
          >
            Yes
          </Button>
        </ModalFooter>
      </Modal>
    );
  }
}
export default ConfirmRemovalModal;
