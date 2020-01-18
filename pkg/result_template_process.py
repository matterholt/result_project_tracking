# -*- coding: utf-8 -*-
"""
Since all engineers have excel, csv would be easily update the to allow db insertian
Uses the template file to add results to db.

@author Matterholt, 2020-01-09
"""
import csv
#from error_comments import sql_header_error
from .error_comments import sql_header_error


class Template_Values:
    def __init__(self, details, results):
        self.details = details
        self.results = results

    def base_on(self):
        return self.details[1]

    def model_name(self):
        return self.details[0]


def detail_column(detail, sql_headers):
    [column_name, column_value, *other] = detail
    if column_name == sql_headers[0]:
        return column_value
    if column_name == sql_headers[1]:
        return column_value
    if column_name == sql_headers[2]:
        return float(column_value)
    if column_name == sql_headers[3]:
        return column_value
    else:
        sql_header_error(column_name)


def result_template_extract(file_dir):
    """
    params : model template file that will be updated for the new results
    - model info will be process and clean for database submittion
    """
    detail_values = []
    model_results = []
    # TODO , have a better way to add sql header column
    sql_headers = ["model_name", "base_on", "weight_kg", "description"]

    with open(file_dir) as entry_data:
        row_data = csv.reader(entry_data)

        switcher_detail_value = True

        for row in row_data:
            if switcher_detail_value == True:
                if row[0] == 'Stiffness':
                    switcher_detail_value = False
                else:
                    # process the detail part of template
                    column_value = detail_column(row, sql_headers)
                    if column_value != False:
                        detail_values.append(column_value)
            else:
                model_results.append(row)

        parsed_template_file = Template_Values(detail_values, model_results)

        return parsed_template_file
