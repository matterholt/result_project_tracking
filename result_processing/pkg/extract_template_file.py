"""
Params: need the folder path to the template file
Purpose: extract the information from the template.csv file 
Process: 
    1. Read the csv file 
    2. Run checks on file to confirm data is sanitize for database
        - might need some regex,
    3. create object from extracted results
"""
import csv
