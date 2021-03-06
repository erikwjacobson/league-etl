# Housekeeping
import numpy
from project import database_connection


def verify(data):
    # Primary verification for players is to ensure no duplicates.
    connection = database_connection.connect()
    cursor = connection.cursor()

    cursor.execute('SELECT player_name from player;')
    players = list(item.player_name for item in cursor.fetchall())
    verified = data[~data['player'].isin(players)]['player'].tolist()

    connection.close()

    return verified
