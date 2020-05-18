# result_project_tracking

Small program that would take stiffness values produce from ARD program and add them to a local database. After the database has been updated. The script would generate the excel report that can be distributed among the team.

### Problems to solve

Born out of the desire to improve how my group process results

1. Design the database, best way to add maintain incoming results.
2. Add previous results to db, results are stored as excel.

   - wanted to make it easily accessible to the team. So keeping with a similar process would allow easy adoption. If concept shows improvement then can step forward in major changes in the process.

3. Manage new results, best way for everyone to contribute to the database.
4. Save the result that is common for traditional way of sharing results

## Build

The program will watch and serialize the data that has been saved to csv/excel file. Using excel or csv to interact with the database, would be a small hurdle for anyone that has been working at the company. Most of the data/result are shared. The concern of this method would be if the column name would be changes but and the data enter into the db would not be pure.

The data in the csv file is parse and sent to the db. Here many direction can be taken but the get the script produce value for the team, will make it generate a report to validate the results of the model.

In order to accomplish this the model that was last placed in the db will have a report generated for it. Using the model name fetch the data from the model detail table in the db. Once obtain the info there would be able to abstract the rest of the info to complete the report. The model id will be use to get all the stiffness results from the model_results table. The full set of data has been compiled and is tossed into a Python class to where the info can be tossed around and construct report.

To validate wether the results are have improved the base model result would need to be fetch from the database. Along with comparing the model to the base the overall objective will need to see how results are compared to the target that are supplied byt OEM. The Target is hard coded into the script, could be moved to the setup file but it is always something that model are compared with through out the to development of the part,'

---

watcher file will loop for updates on the template file
db_table_build folder
-> sql database and table for the project, also will add any results that have not been saved to db.

The use of csv/excel file to interact with the program, would

### Future idea

- Flask REST API
- json or .env to set parameters for "setup"

### TODO:

- result_template_process.py --- dynamic sql header name check

### conda commands

conda list --explicit > test.txt ---> list packages installed
conda env export > environment.yml ---> list packages installed

### pytest commands

pytest test_example.py -v ---> more detail in terminal
