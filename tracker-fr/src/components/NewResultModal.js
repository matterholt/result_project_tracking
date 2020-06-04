import React, { Component } from "react";
import { Button, Modal, ModalHeader, ModalBody } from "reactstrap";
import NewResultForm from "./NewResultForm";

class NewResultModal extends Component {
  state = {
    modal: false,
  };
  toggle = () => {
    this.setState((previous) => ({
      modal: !previous.modal,
    }));
  };
  render() {
    const create = this.props.create;

    let title = "Editing Results";
    let button = <Button onClick={this.toggle}>Edit</Button>;
    if (create) {
      title = "Creating New Results";
      button = (
        <Button
          color="primary"
          className="float-right"
          onClick={this.toggle}
          style={{ minWidth: "200px" }}
        >
          Create New
        </Button>
      );
    }

    return (
      <ModalBody>
        {button}
        <Modal isOpen={this.state.modal} toggle={this.toggle}>
          <ModalHeader toggle={this.toggle}>{title}</ModalHeader>
          <NewResultForm
            resetState={this.state.resetState}
            toggle={this.toggle}
            results={this.props.results}
          />
        </Modal>
      </ModalBody>
    );
  }
}

export default NewResultModal;
