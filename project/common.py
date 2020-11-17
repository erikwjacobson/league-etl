# Housekeeping
from scripts import extractor
from datetime import datetime
from verification import general_verification
from loaders import general_loader
import pandas

start = datetime.now()

##
# Extraction
#
print('Starting data extraction...')

# TODO Determine how to reduce load time by providing options for loading most recent
# TODO Change back to true extraction once production ready
# all_data = extractor.extract('https://oracleselixir.com/tools/downloads')

all_data = {'2020': pandas.read_csv('../2020_LoL_esports_match_data.csv')} # for dev purposes only

extraction_time = datetime.now() - start
print(f'Finished extraction: {extraction_time.seconds}s.')

# Iterate through each dataset
# TODO Update this for options other than loading all of the data sets
for key in all_data:
    dataset = all_data[key]

    ##
    # Loading
    #
    load_start = datetime.now()
    print(f'Starting data loading for {key}...')
    print()

    general_loader.load(dataset)  # Load all data

    print()

loading_time = datetime.now() - load_start
print(f'Finished loading: {loading_time.seconds}s.')

# Final runtime
total_time = datetime.now() - start
print(f'Total ETL time: {total_time.seconds}s.')
