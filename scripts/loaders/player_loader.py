# Housekeeping
import pyodbc
import pandas
from transforms import player_transform


def load(data, cursor):
    # Get transformed data
    player_data = player_transform.transform(data)

    # Load using pyodbc
    if len(player_data) != 0:
        player_data = list((item,) for item in player_data)
        cursor.executemany(f'INSERT INTO player VALUES (?)', player_data)

        print('Executed inserts for player table.')

    else:
        print('No new players were inserted to the player table.')
