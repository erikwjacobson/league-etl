# Housekeeping
import pandas


def team_transformed(data):
    # Select relevant columns
    columns = ['team', 'league']
    to_load = data[data['position'] == 'team'][columns].unique()

    # Return data
    return to_load
