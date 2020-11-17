# Housekeeping
import pandas
from verification import league_verification


def transform(data):
    # Select relevant columns
    columns = ['league']

    # Main transformation
    to_verify = data[columns].drop_duplicates(subset=['league'])

    # Run verification
    to_load = league_verification.verify(to_verify)

    # Return data
    return to_load
