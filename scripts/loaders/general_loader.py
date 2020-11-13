# Housekeeping
import pyodbc
import pandas
from loaders import player_loader
from project import database_connection

##
# General loader that takes in a dataframe and loads the data into the database
# @param data - pandas dataframe that contains the loadable data
#


def load_data(data):
    # Establish connection
    connection = database_connection.connect(autocommit=False)
    cursor = connection.cursor()

    # Call each individual loader
    player_loader.load_player(data, cursor)

    # Execute
    connection.commit()
    connection.close()

    print('General loader finished loading.')
