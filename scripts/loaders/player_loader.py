# Housekeeping
import pyodbc
import pandas
from transforms import player_transform


def load_player(data, cursor):
    # Get transformed data
    player_data = player_transform.player_transformed(data)

    # Load using pyodbc
    cursor.fast_executemany = True
    player_data = list((item,) for item in player_data)
    cursor.executemany(f'INSERT INTO player VALUES (?)', player_data)

    # Next table load occurs
    print('Executed inserts for player table.')
