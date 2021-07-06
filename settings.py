import sqlite3

try:
    sqlite_connection = sqlite3.connect('TimesheetWhy.db')

    RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
    ITEM_METHODS = ['GET', 'PUT', 'DELETE']

    DOMAIN = {
        'Projects': {
            'schema': {
                'ProjectId': {
                    'type': 'integer',
                    'required': True,
                    'unique': True,
                },
                'ProjectName': {
                    'type': 'string',
                    'maxlength': 100,
                    'required': True,
                    'unique': True,
                },
                'ProjectDescription': {
                    'type': 'string',
                    'maxlength': 1000,
                    'required': True,
                    'unique': True,
                }
            }
        }
    }

except sqlite3.Error as error:
    print(error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()