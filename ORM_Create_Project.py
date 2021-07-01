import sqlite3

try:
    sqlite_connection = sqlite3.connect('TimesheetWhy.db')
    cursor = sqlite_connection.cursor()

    ProjectName = "Timesheet Why?"
    ProjectDescription = "Домашнее задание для модуля 3"

    sql_query = """
        INSERT INTO Project (Project_Name, Project_Description) 
        VALUES (?, ?)
    """
    cursor.execute(sql_query, ProjectName, ProjectDescription)
    sqlite_connection.commit()

    cursor.close()
except sqlite3.Error as error:
    print(error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
