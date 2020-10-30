# Housekeeping
from scripts import extractor
from datetime import datetime
start = datetime.now()

##
# Extraction
#
print('Starting data extraction...')

data = extractor.extract('https://oracleselixir.com/tools/downloads')
extraction_time = datetime.now() - start

print(f'Finished extraction: {extraction_time.seconds}s.')

##
# Loading
#
load_start = datetime.now()
print('Starting data loading...')

# TODO Load the data


loading_time = datetime.now() - load_start
print(f'Finished loading: {loading_time.seconds}s.')

# Final runtime
total_time = datetime.now() - start
print(f'Total ETL time: {total_time.seconds}s.')
