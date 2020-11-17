# Housekeeping
import pandas
from project import database_connection

##
# Verify that the data meets specific requirements
#


def verify(data):
    # Ensure data completeness
    data = data[data['datacompleteness'] == 'complete']

    # Ensure match id is not in the verification table
    connection = database_connection.connect()
    cursor = connection.cursor()

    cursor.execute('SELECT match_id from verification;')
    matches = list(item.match_id for item in cursor.fetchall())
    verified = data[~data['gameid'].isin(matches)].tolist()

    connection.close()

    return verified
