from transforms import roster_transform


def load(data, cursor):
    roster_data = roster_transform.transform(data)

    if len(roster_data) != 0:
        roster_data = list(
            (item.team, item.top, item.jng, item.mid, item.bot, item.sup) for index, item in roster_data.iterrows()
        )
        cursor.executemany('INSERT INTO roster ' +
                           '(team_id, top_player_id, jg_player_id, mid_player_id, bot_player_id, sup_player_id)' +
                           ' VALUES (?,?,?,?,?,?)', roster_data)

        print('Executed inserts for roster table.')

    else:
        print('No new rosters were inserted to the roster table.')
