import sqlite3

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        connection = sqlite3.connect(db_file)
        print("Opened database successfully", type(connection))
        
    except Exception as e:
        raise e
    return connection

def close_connection(connection):
    # closes a connection to a database
    connection.close()
    print("Closed database successfully")

def select_all(conn):
    """select all rows from our table using the conn we already created """
    #cur = conn.cursor()
    query = "SELECT * FROM longley;" # To-Do write the query to retrive all data from the longley table 
    cur = conn.execute(query)
    #cur.execute(query)
    print('Query Executed successfully.')
    rows = [row for row in cur]  # To-Do fetch all rows using the cursor cur

    return rows 

def print_rows(rows):
    """ Loop through the retrived rows of a table and print them"""
    # All of the function body is a todo task
    for row in rows:
        print(row)