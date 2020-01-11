"""
SQLITE3 call to the data base

Params: Array and database file.
Purpose: retrieve and send data to database
Process: 
    1. Send array of results that have been extracted from the csv file
    2. Retrieve data from the database, 
        - details table looking for model_name
        - stiffness_results will look for the id of the model name.

At this stage sqlite3 will get the job, Then if program is successful the hope to migrate 
to more substantial database such as Postgresql
"""
import sqlite3
from sqlite3 import Error

def create_db_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn