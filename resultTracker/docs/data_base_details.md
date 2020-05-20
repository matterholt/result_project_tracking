# Data base structure for project

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
