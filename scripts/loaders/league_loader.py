import pyodbc
import pandas
from transforms import league_transform


def load(data, cursor):
    # Get transformed data
    league_data = league_transform.transform(data)

    if len(league_data) != 0:
        league_data = list((item,) for item in league_data)
        cursor.executemany(f'INSERT INTO league VALUES (?)', league_data)

        print('Executed inserts for league table.')

    else:
        print('No new leagues were inserted to the league table.')
