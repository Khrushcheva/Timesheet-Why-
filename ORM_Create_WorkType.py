import sqlite3

try:
    sqlite_connection = sqlite3.connect('TimesheetWhy.db')
    cursor = sqlite_connection.cursor()

    WorkTypeName = "Отрисовка схем"
    WorkTypeDescription = "Рисование схем в различных нотациях"

    sql_query = """
        INSERT INTO WorkType (WorkType_Name, WorkType_Description) 
        VALUES (?, ?)
    """
    cursor.execute(sql_query, WorkTypeName, WorkTypeDescription)
    sqlite_connection.commit()

    cursor.close()
except sqlite3.Error as error:
    print(error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
