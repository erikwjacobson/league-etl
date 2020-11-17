# Housekeeping
import pandas


def roster_tranformed(data):
    # Select relevant columns
    columns = ['position','player','team','date']
    to_trans = data[data['position' != 'team']][columns]

    to_trans = to_trans.pivot(columns='position', values=['player', 'team'])

    return to_load
