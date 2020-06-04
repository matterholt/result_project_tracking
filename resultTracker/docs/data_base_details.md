# Data base structure for project

## wk 22 (may25-31-2020)


### User Story
At model creation, after the model detail have been input, User able to select analysis wish to perform. At submital form will create an entry in the analysis_detail database forign key reff model name. Entry will have default values with "NONE", allowing details to be added later. 

When user looks at a specific model details via model ID. User will able to see that details of the model and the status of the analysis, if there is no analysis details then able to add. If there analysis has been performed then can make a request to the results database limiting the request to db's. 

>> this way will future proof the capablitiy of other people creating the request without adding or viewing the results


from the model detail page retrive judgement DB. 
inside analysis_detail db

1. analysis scheduled => stiffness, durability, static
2. judgement  => Improved, NG, None,
3. didPerform => False/True  ## if true then can fetch data from results page. better to seperate analysis 
4. foreignID => model_detail(id)




Keep the table modular and singles source of truths

project Table -> contain info about the project that user wishes to document.

- project_code
- project_part

model_details Table -> Engineer wishes to document the details about the model that has been validated

- base_model_name
- cm_model_name
- cm_model_description
- foreign key to project table (one to one)
- foreign key to model_files (one to one)
- foreign key to stiffness_results (one to many)

model_raw_result Table -> any file that is submitted to process results.

- cm_result_pnch_file

stiffness_result Table -> results are processed and are saved with in this table

- location_load_applied
- xyz_displacement
- node_number
- load_direction
- newton_mm_force
- foreign key to judgement!!
