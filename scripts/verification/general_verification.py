# Housekeeping
import pandas

##
# Verify that the data meets specific requirements
#


def verify(data):
    # Ensure data completeness
    data = data[data['datacompleteness'] == 'complete']

    return data
