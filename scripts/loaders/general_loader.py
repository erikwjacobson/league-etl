# Housekeeping
import pyodbc
import pandas
from loaders import player_loader
from loaders import league_loader
from verification import general_verification
from project import database_connection

##
# General loader that takes in a dataframe and loads the data into the database
# @param data - pandas dataframe that contains the loadable data
#


def load(data):
    # Establish connection
    connection = database_connection.connect(autocommit=False)
    cursor = connection.cursor()
    cursor.fast_executemany = True

    # Run general verifications on the data
    verified_data = general_verification.verify(data)

    # Call each individual loader
    player_loader.load(verified_data, cursor)
    league_loader.load(verified_data, cursor)

    # Execute
    connection.commit()
    connection.close()

    print('General loader finished loading.')
