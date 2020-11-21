# Housekeeping
import pandas
from verification import roster_verification
from project import database_connection


def transform(data):
    # Perform pivot transformation
    data = data[data['position'] != 'team']

    # Selects rosters based on gameid and team, and pivots columns to provide data
    # where one row = one roster
    pivoted = data.pivot_table(index=['gameid', 'team'], values='player', columns='position', aggfunc='first')
    pivoted = pivoted.reset_index()

    # Only select unique rosters based on team and players in specific positions
    pivoted = pivoted.drop_duplicates(subset=['team', 'bot', 'jng', 'mid', 'sup', 'top'])

    # Get keys from database
    connection = database_connection.connect()
    player_ids = pandas.read_sql_query('SELECT player_id, player_name FROM player', connection)
    team_ids = pandas.read_sql_query('SELECT team_id, team_name FROM team', connection)
    connection.close()

    # Replace names with ids in the table
    team_id_dict = team_ids.set_index('team_name').to_dict()['team_id']
    player_id_dict = player_ids.set_index('player_name').to_dict()['player_id']
    positions = ['top', 'jng', 'mid', 'bot', 'sup']
    pivoted[positions] = pivoted[positions].replace(player_id_dict)  # replace all player names with ids
    pivoted = pivoted.replace({'team': team_id_dict})  # replace all team names with ids

    # Verify the data
    to_verify = pivoted
    to_load = roster_verification.verify(to_verify)

    return to_load
