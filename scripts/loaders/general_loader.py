# Housekeeping
from loaders import player_loader
from loaders import league_loader
from loaders import team_loader
from loaders import roster_loader
from verification import general_verification
from project import database_connection


def load(data):
    # Establish connection
    connection = database_connection.connect(autocommit=False)
    cursor = connection.cursor()

    # Run general verifications on the data
    verified_data = general_verification.verify(data)

    # Call each individual loader
    player_loader.load(verified_data, cursor)
    connection.commit()

    league_loader.load(verified_data, cursor)
    connection.commit()

    team_loader.load(verified_data, cursor)
    connection.commit()

    roster_loader.load(verified_data, cursor)
    connection.commit()

    # Close the connection
    connection.close()

    print('General loader finished loading.')
