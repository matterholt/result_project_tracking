# result_project_tracking

## Build

watcher file will loop for updates on the template file
db_table_build folder 
     -> sql database and table for the project, also will add any results that have not been saved to db.



### Problems to solve

Born out of the desire to improve how my group process results

1. Design the database, best way to add maintain incoming results.
2. Add previous results to db, results are stored as excel.

     - wanted to make it easily accessible to the team. So keeping with a similar process would allow easy adoption. If concept shows improvement then can step forward in major changes in the process.

3. Manage new results, best way for everyone to contribute to the database.
4. Save the result that is common for traditional way of sharing results

### Future idea

- Flask REST API
- json or .env to set parameters for "setup"

### TODO:

- result_template_process.py --- dynamic sql header name check

### conda commands

conda list --explicit > test.txt ---> list packages installed
conda env export > environment.yml ---> list packages installed

### pytest commands

pytest test_example.py -v  ---> more detail in terminal
