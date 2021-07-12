import sqlite3

try:
    sqlite_connection = sqlite3.connect('TimesheetWhy.db')
    cursor = sqlite_connection.cursor()

    ProjectID = 1,
    WorkTypeID = 1,
    StartDateTime = "2021-07-12T08:30",
    EndDateTime = "2021-07-12T09:30",
    Duration = 1,
    Value = "Для того, чтобы разобраться как взаимодействуют слои в приложении",
    WorkDescription = "Отрисовка sequence diagram",
    Documents = "sequence.pdf",
    HourPrice = 1200,
    WorkPrice = 1200

    sql_query = """
        INSERT INTO Work (ProjectID, WorkTypeID, StartDateTime, EndDateTime, Duration, Value, WorkDescription, Documents, HourPrice, WorkPrice) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    cursor.execute(sql_query, (ProjectID, WorkTypeID, StartDateTime, EndDateTime, Duration, Value, WorkDescription, Documents, HourPrice, WorkPrice)
    sqlite_connection.commit()

    cursor.close()
except sqlite3.Error as error:
    print(error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
