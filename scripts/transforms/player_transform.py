# Housekeeping
import pandas
from verification import player_verification


def player_transformed(data):
    # Select relevant columns
    columns = ['player']
    only_players = data[data['position'] != 'team'][columns]
    to_verify = only_players.drop_duplicates(subset=['player'])
    to_load = player_verification.verify(to_verify)

    # Return data
    return to_load
