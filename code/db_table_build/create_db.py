import sqlite3
from sqlite3 import Error
def create_db_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn
def create_table(conn,table):
    try:
        c = conn.cursor()
        c.execute(table)
    except Error as e:
        print(e)

def struct_table(db):

    sql_create_model_details_table = """ CREATE TABLE IF NOT EXISTS model_details (
                                    id integer PRIMARY KEY,
                                    model_name TEXT NOT NULL,
                                    base_on TEXT,
                                    weight_kg REAL,
                                    description TEXT,
                                    add_date TEXT DEFAULT CURRENT_TIMESTAMP
                                ); """
 
    sql_create_model_results_table = """CREATE TABLE IF NOT EXISTS model_results (
                                    id integer PRIMARY KEY,
                                    location_load_applied TEXT NOT NULL ,
                                    node_number REAL,
                                    load_direction TEXT NOT NULL,
                                    newton_mm_force REAL NOT NULL,
                                    model_id integer NOT NULL,
                                    FOREIGN KEY (model_id) REFERENCES model_details (id)
                                );"""

    conn = create_db_connection(db)
    if conn is not None:
        create_table(conn,sql_create_model_details_table)
        create_table(conn,sql_create_model_results_table)
    else:
        print('Could not connect to DB')


def main():
    database_file = r"../XYZ_project.db"
    struct_table(database_file)
    print(f"database has been create {database_file}")

if __name__ == "__main__":
    main()