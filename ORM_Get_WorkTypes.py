import sqlite3

try:
    sqlite_connection = sqlite3.connect('TimesheetWhy.db')
    cursor = sqlite_connection.cursor()

    sql_query = """
        SELECT WorkType_ID, WorkType_Name, WorkType_Description
        FROM WorkType
    """
    cursor.execute(sql_query)
    WorkTypes = cursor.fetchall()

    for WorkType in WorkTypes:
        print("Hello!")
        print(WorkType)

    cursor.close()
except sqlite3.Error as error:
    print(error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
