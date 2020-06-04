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
to more substantial database such as Postgresql, and  SQLAlchemy

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


def add_sql_model_details(db, details):
    conn = create_db_connection(db)
    sql_insert = """INSERT INTO model_details
    (model_name, base_on, weight_kg, description)
    VALUES(?,?,?,?)"""

    with conn:
        cur = conn.cursor()
        cur.execute(sql_insert, details)
        version_name = details[0]
        print(f"Model {version_name} details have been made")
        return cur.lastrowid


def add_sql_model_stiffness(db, results, model_id):
    conn = create_db_connection(db)
    sql_insert = """INSERT INTO model_results
        (model_id, location_load_applied, node_number,
         load_direction, newton_mm_force)
        VALUES(?,?,?,?,?)"""
    with conn:
        for row_result in results[1:]:
            sql_result_entry = [model_id] + row_result

            cur = conn.cursor()
            cur.execute(sql_insert, sql_result_entry)
        print(f"Results have been added to db, model id = {model_id}")


def get_sql_modelID_detail(db, model_id):
    conn = create_db_connection(db)
    with conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM model_details WHERE id = ?', (model_id,))
        row = cur.fetchone()

        return row


def get_sql_modelName_detail(db, model_name):
    conn = create_db_connection(db)
    with conn:
        cur = conn.cursor()
        cur.execute(
            'SELECT * FROM model_details WHERE model_name = ? ORDER BY id', (model_name,))
        row = cur.fetchone()

        return row


def get_sql_modelID_stiffness(db, id):
    conn = create_db_connection(db)
    with conn:
        cur = conn.cursor()
        cur.execute(
            'SELECT * FROM model_results WHERE model_id = ?', (id,)
        )
        row = cur.fetchall()
        return row
