"""
Params: the template file that is being watched and updated
Purpose: Main entry for the program
Process: 
    STAGE 1: UPDATE DB
    1. Read template file that was update with model data.
    2. Take model data and construct them in an Object form,
    3. Add model Object and submit them to the project database.
        -> sql table one: "model_details"
        -> sql table two: "stiffness_results"
    
    STAGE 2: CONSTRUCT REPORT DATA
    1. Retrieve model info from the db table "model_details".
    2. With model ID get all model results from table"stiffness_results".
    3. Repeat for the 3 time with
        model_validated, base_on, target

    STAGE 3: REPORT GENERATION
    1. Generate excel with key project location, that are define in a template file
    2. Append the latest results (validate model) to a "running" excel.
        - This lines up with current group process (2020.01)
"""
from .pkg.result_template_process import result_template_extract

#def execute_process(watch_template_file,database_file):
def execute_process():

    file = r"result_templates/new_model_template.csv"
    database_file = r"/sql_temp.db"

    """
    Before adding to DB need to extract and complie data to add
    will return an object
    """
    print("\nExtract data from Template file")
    # return the 
    update_information = result_template_extract(watch_template_file)

    print(update_information.base_on)
    print(update_information.model_name)

execute_process()
