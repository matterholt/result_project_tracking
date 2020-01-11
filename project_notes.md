# result_project_tracking

## Build

### Problems to solve

Born out of the desire to improve how my group process results

1. Design the database, best way to add maintain incoming results.
2. Add previous results to db, results are stored as excel.

     - wanted to make it easily accessible to the team. So keeping with a similar process would allow easy adoption. If concept shows improvement then can step forward in major changes in the process.

3. Manage new results, best way for everyone to contribute to the database.
4. Save the result that is common for traditional way of sharing results

### Future idea

- Flask REST API


### conda commands

conda list --explicit > test.txt ---> list packages installed
conda env export > environment.yml ---> list packages installed

### pytest commands

pytest test_example.py -v  ---> more detail in terminal

## keyword expressions 

### Run all tests with some string ‘validate’ in the name

pytest -k “validate”

### Exclude tests with ‘db’ in name but include 'validate'

pytest -k “validate and not db” 

### Run all test files inside a folder demo_tests

pytest demo_tests/

### Run a single method test_method of a test class TestClassDemo 

pytest demo_tests/test_example.py::TestClassDemo::test_method

### Run a single test class named TestClassDemo 

pytest demo_tests/test_example.py::TestClassDemo

### Run a single test function named test_sum

pytest demo_tests/test_example.py::test_sum

### Run tests in verbose mode: 

pytest -v demo_tests/

### Run tests including print statements: 

pytest -s demo_tests/

### Only run tests that failed during the last run 
pytest — lf

-https://medium.com/testcult/intro-to-test-framework-pytest-5b1ce4d011ae