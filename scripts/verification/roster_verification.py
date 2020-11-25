from project import database_connection
import pandas


def verify(data):
    # Primary verification for rosters is to ensure no duplicates.
    connection = database_connection.connect()

    query = 'SELECT team_id, top_player_id, jg_player_id, mid_player_id, bot_player_id, sup_player_id from roster'
    rosters = pandas.read_sql_query(query, connection)

    # Performing an outer merge to determine return only rosters not in the database
    merged = pandas.merge(data, rosters, how='outer',
                          left_on=['team', 'top', 'jng', 'mid', 'bot', 'sup'],
                          right_on=['team_id','top_player_id','jg_player_id','mid_player_id','bot_player_id','sup_player_id'],
                          indicator=True)  # indicator allows us to select only the left side of the venn diagram
    final_columns = ['team', 'top', 'jng', 'mid', 'bot', 'sup']
    verified = merged[merged._merge == 'left_only'][final_columns]  # get only left side

    return verified
