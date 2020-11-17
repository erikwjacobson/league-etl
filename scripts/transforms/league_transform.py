# Housekeeping
import pandas


def league_transformed(data):
    # Select relevant columns
    columns = ['league']
    to_load = data[columns].league.unique()

    # Return data
    return to_load
