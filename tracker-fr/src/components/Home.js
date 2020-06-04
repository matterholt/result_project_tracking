import React, { Component } from "react";
import { Col, Container, Row } from "reactstrap";
import ResultsList from "./ResultsList";
import NewResultList from "./NewResultModal";

import axios from "axios";

import { API_URL } from "../constraints/index_cons";
class Home extends Component {
  state = {
    results: [],
  };

  componentDidMount() {
    this.resetState();
  }
  getResults = () => {
    axios.get(API_URL).then((res) => this.setState({ results: res.data }));
  };
  resetState = () => {
    this.getResults();
  };

  render() {
    return (
      <Container>
        <Row>
          <Col>
            <ResultsList
              results={this.state.results}
              resetState={this.resetState}
            />
          </Col>
        </Row>
        <Row>
          <Col>
            <NewResultList create={true} resetState={this.resetState} />
          </Col>
        </Row>
      </Container>
    );
  }
}

export default Home;
