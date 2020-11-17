from project import database_connection


def verify(data):
    # Primary verification for leagues is to ensure no duplicates.
    connection = database_connection.connect()
    cursor = connection.cursor()

    cursor.execute('SELECT league_name from league;')
    leagues = list(item.league_name for item in cursor.fetchall())
    verified = data[~data['league'].isin(leagues)]['league'].tolist()

    connection.close()

    return verified
