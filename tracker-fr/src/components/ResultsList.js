import React, { Component } from "react";

import { Table } from "reactstrap";

import NewResultModal from "./NewResultModal";
import ConfirmRemovalModal from "./ConfirmRemovalModal";

class ResultsList extends Component {
  render() {
    const results = this.props.results;
    return (
      <Table>
        <thead>
          <tr>
            <th>Cm Model Name</th>
            <th>Cm Model Description</th>
            <th>Base Model Name</th>
          </tr>
        </thead>
        <tbody>
          {!results || results.length <= 0 ? (
            <tr>
              <td colSpan="6" align="center">
                <b>Ops, no results added</b>
              </td>
            </tr>
          ) : (
            results.map((result) => (
              <tr key={result.id}>
                <td>{result.cm_model_name}</td>
                <td>{result.cm_model_description}</td>
                <td>{result.base_model_name}</td>
                <td align="center">
                  <NewResultModal
                    create={false}
                    result={results}
                    resetState={this.props.resetState}
                  />
                  &nbsp;&nbsp;
                  <ConfirmRemovalModal
                    pk={result.pk}
                    resetState={this.state.props.resetState}
                  />
                </td>
              </tr>
            ))
          )}
        </tbody>
      </Table>
    );
  }
}

export default ResultsList;
