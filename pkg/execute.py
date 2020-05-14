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
    1. Generate excel with key project location, that are define in a template 
    file
    2. Append the latest results (validate model) to a "running" excel.
        - This lines up with current group process (2020.01)

TODO:
    1. how to handle error from the sql for string not located in db
    2. add a capitalization to the sql, inserts, to be able to control
    3. improve class , minimize the code, (result_template_process, model_info)
"""
from .result_template_process import result_template_extract
from .sql_commands.sql_commands import (add_sql_model_details,
                                        add_sql_model_stiffness,
                                        get_sql_modelName_detail,
                                        get_sql_modelID_stiffness)
from .model_info import model_construct
from .percentTarget_cal import percentTarget
from .panda_actions import build_Report


def execute_process(watch_template_file, db):
    """
    Addingthe template file to the database
    """
    # STAGE 1 #####

    """
    Before adding to DB need to extract and complie data to add
    will return an object
    """
    print("\nExtract data from Template file")

    # object to get started
    update_information = result_template_extract(watch_template_file)

    base_on_model_name = update_information.base_on()
    validated_model_name = update_information.model_name()

    # Add data to data base
    print('adding details to database')
    validated_model_id = add_sql_model_details(db, update_information.details)
    add_sql_model_stiffness(db, update_information.results, validated_model_id)

    print('COMPLETED!!')

    # STAGE 2 #####
    # -> OEM supplied targets,
    target_model = model_construct(db, 'Target')
    target_model_stiffness = target_model.newton_mm_values()

    # -> validated model
    validated_model = model_construct(db, validated_model_name)
    print(validated_model)
    validated_model_stiffness = validated_model.newton_mm_values()
    validated_modelvalue_percent = percentTarget(
        target_model_stiffness, validated_model_stiffness)

    # -> model to which the validation model is base on
    base_model = model_construct(db, base_on_model_name)
    base_model_stiffness = base_model.newton_mm_values()
    base_modelValue_percent = percentTarget(
        target_model_stiffness, base_model_stiffness)
    # create a dictionary with the data above and send that to make Report
    report_data = {
        'row_labels': validated_model.result_locationDir_column(),
        'target_stiff': target_model_stiffness,
        'base_stiff_vals': list(base_modelValue_percent),
        'model_stiff_vals':  list(validated_modelvalue_percent)
    }
    build_Report(report_data, validated_model)
