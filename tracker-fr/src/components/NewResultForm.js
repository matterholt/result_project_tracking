import React from "react";
import { Button, Form, FormGroup, Input, Label } from "reactstrap";

import axios from "axios";

import { API_URL } from "../constraints/index_cons";

class NewResultForm extends React.Component {
  state = {
    pk: 0,
    base_model_name: "",
    cm_model_name: "",
    cm_model_description: "",
  };
  componentDidMount() {
    if (this.props.result) {
      const {
        pk,
        base_model_name,
        cm_model_name,
        cm_model_description,
      } = this.props.result;
      this.setState({
        pk,
        base_model_name,
        cm_model_name,
        cm_model_description,
      });
    }
  }
  onChange = (e) => {
    this.setState({ [e.target.name]: e.target.value });
  };
  createResult = (e) => {
    e.preventDefault();
    axios.post(API_URL + this.state).then(() => {
      this.props.resetState();
      this.props.toggle();
    });
  };
  editResult = (e) => {
    e.preventDefault();
    axios.put(API_URL + this.state.pk, this.state).then(() => {
      this.props.resetState();
      this.props.toggle();
    });
  };
  defaultIfEmpty = (value) => {
    return value === "" ? "" : value;
  };
  render() {
    return (
      <div
        style={{
          width: "350px",
          margin: "15px",
          padding: "15px",
          backgroundColor: "lightgray",
        }}
      >
        <Form
          onSubmit={this.props.result ? this.editResult : this.createResult}
        >
          <FormGroup>
            <Label for="base_model_name">Base Model Name:</Label>
            <Input
              type="text"
              name="base_model_name"
              onChange={this.onChange}
              value={this.defaultIfEmpty(this.state.name)}
            />
          </FormGroup>
          <FormGroup>
            <Label for="cm_model_name"> Cm Model Name</Label>
            <Input
              type="text"
              name="cm_model_name"
              onChange={this.onChange}
              value={this.defaultIfEmpty(this.state.name)}
            />
          </FormGroup>
          <FormGroup>
            <Label for="cm_model_description">Cm Model Description:</Label>
            <Input
              type="textarea"
              name="cm_model_description"
              onChange={this.onChange}
              value={this.defaultIfEmpty(this.state.name)}
            />
          </FormGroup>
          <Button>Send</Button>
        </Form>
      </div>
    );
  }
}

export default NewResultForm;
