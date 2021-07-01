import sqlite3

try:
    sqlite_connection = sqlite3.connect('TimesheetWhy.db')
    cursor = sqlite_connection.cursor()

    sql_query = """
        CREATE TABLE Project (
        Project_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Project_Name NVARCHAR(100) NOT NULL,
        Project_Description NVARCHAR(1000) NULL
        );
    """
    cursor.execute(sql_query)
    sqlite_connection.commit()

    sql_query = """
        CREATE TABLE WorkType (
        WorkType_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        WorkType_Name NVARCHAR(100) NOT NULL,
        WorkType_Description NVARCHAR(1000) NULL
        );
    """
    cursor.execute(sql_query)
    sqlite_connection.commit()

    sql_query = """
        CREATE TABLE Work (
        Project_ID INTEGER REFERENCES Project(Project_ID),
        WorkType_ID INTEGER REFERENCES WorkType(WorkType_ID),
        StartDateTime DATETIME NOT NULL,
        EndDateTime DATETIME NOT NULL,
        Value NVARCHAR(1000) NOT NULL,
        WorkDescription NVARCHAR(1000) NOT NULL,
        Documents NVARCHAR(2500) NOT NULL,
        Duration TIME NOT NULL,
        HourPrice MONEY NULL,
        WorkPrice MONEY NULL,
        PRIMARY KEY (Project_ID, WorkType_ID, StartDateTime, EndDateTime)
        );
    """
    cursor.execute(sql_query)
    sqlite_connection.commit()

    cursor.close()
except sqlite3.Error as error:
    print(error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
