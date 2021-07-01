import sqlite3

try:
    sqlite_connection = sqlite3.connect('TimesheetWhy.db')
    cursor = sqlite_connection.cursor()

    sql_query = """
        SELECT Project_ID, Project_Name, Project_Description
        FROM Project
    """
    cursor.execute(sql_query)

    Projects = cursor.fetchall()

    cursor.close()
except sqlite3.Error as error:
    print(error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
