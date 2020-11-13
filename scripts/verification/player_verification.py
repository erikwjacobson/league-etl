# Housekeeping
import numpy
from project import database_connection


def verify(data):
    # Primary verification for players is to ensure no duplicates.
    connection = database_connection.connect()
    cursor = connection.cursor()

    cursor.execute('SELECT player_name from player;')
    players = cursor.fetchall()
    verified = data[~data['player'].isin(players)]['player'].tolist()

    return verified
