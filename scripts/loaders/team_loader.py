# Housekeeping
from transforms import team_transform


def load(data, cursor):
    team_data = team_transform.transform(data)

    if len(team_data) != 0:
        team_data = list((item.team, item.league_id) for index, item in team_data.iterrows())
        cursor.executemany(f'INSERT INTO team (team_name, league_id) VALUES (?,?)', team_data)

        print('Executed inserts for team table.')

    else:
        print('No new teams were inserted to the team table.')