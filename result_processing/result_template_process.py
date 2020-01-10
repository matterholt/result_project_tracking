# -*- coding: utf-8 -*-
"""
Since all engineers have excel, csv would be easily update the to allow db insertian
Uses the template file to add results to db.

@author Matterholt, 2020-01-09
"""
import csv
import sys
from Error_comment import sql_header_error

class Template_Values: 
    def __init__ (self, details, results):
        self.details = details
        self.results = results

def detail_column(detail,sql_headers):
    [column_name, column_value, *other ] = detail
    if column_name == sql_headers[0]:
        return column_value
    if column_name == sql_headers[1]:
        return column_value
    if column_name == sql_headers[2]:
        return column_value
    if column_name == sql_headers[3]:
        return column_value
    else:
        print (sql_header_error(column_name))
        sys.exit()

def result_template_extract(file_dir):
    """
    params : model template file that will be updated for the new results
    - model info will be process and clean for database submittion
    """
    detail_values = []
    model_results = []
    sql_headers = ["model_name","base_on","weight_kg","description"]


    with open(file_dir) as entry_data:
        row_data = csv.reader(entry_data)

        switcher_detail_value = True

        for row in row_data:
            if switcher_detail_value == True:
                if row[0] == 'RESULTS':
                    switcher_detail_value = False
                else:
                    # process the detail part of template
                    column_value = detail_column(row,sql_headers)
                    if column_value != False:
                        detail_values.append(column_value)
            else:
                model_results.append(row)

        parsed_template_file = Template_Values(detail_values,model_results)

        print(parsed_template_file.details)
        print( parsed_template_file.results)

        




file_dir = r"/Users/matterholt/projects/fea_results/result_templates/new_model_template.csv"
result_template_extract(file_dir)