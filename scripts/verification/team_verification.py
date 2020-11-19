from project import database_connection


def verify(data):
    # Primary verification for teams is to ensure no duplicates.
    connection = database_connection.connect()
    cursor = connection.cursor()

    cursor.execute('SELECT team_name from team;')
    teams = list(item.team_name for item in cursor.fetchall())
    verified = data[~data['team'].isin(teams)]

    connection.close()

    return verified
