# Housekeeping
import pandas
from project import database_connection

##
# Verify that the data meets specific requirements
#


def verify(data):
    # Ensure data completeness
    data = data[data['datacompleteness'] == 'complete']

    # Need to replace special characters that exist in some of the names from various EU countries.
    decoded = data.copy()
    decoded.loc[:, 'team'] = decoded['team'].str.normalize('NFD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    decoded.loc[:, 'player'] = decoded['player'].str.normalize('NFD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    data = decoded

    # Ensure match id is not in the verification table
    connection = database_connection.connect()
    cursor = connection.cursor()

    cursor.execute('SELECT match_id from verification;')
    matches = list(item.match_id for item in cursor.fetchall())
    verified = data[~data['gameid'].isin(matches)]

    connection.close()

    return verified
