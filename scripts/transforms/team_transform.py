# Housekeeping
import pandas
from project import database_connection
from verification import team_verification


def transform(data):
    # Select relevant columns
    columns = ['team', 'league']
    data = data[data['position'] == 'team'][columns]  # Select only team data

    # Selecting the league based on where they played the most games
    # - This is based around assumptions, and likely won't be perfect
    #   but is the best method of selecting the proper league as of now.
    grouped = data.groupby(columns, as_index=False).size()
    grouped = grouped.sort_values('size', ascending=False).drop_duplicates(subset=['team'])
    grouped = grouped.drop(columns=['size'])

    # Getting league_ids from the database
    connection = database_connection.connect()
    league_ids = pandas.read_sql('SELECT league_id, league_name FROM league', connection)
    to_verify = grouped.merge(league_ids, left_on='league', right_on='league_name')
    connection.close()

    # Verify data
    to_load = team_verification.verify(to_verify)

    # Return data
    return to_load
