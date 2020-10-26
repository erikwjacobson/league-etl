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

print(f'Finished extraction: {extraction_time.seconds}s load time.')

##
# Transformation
#
trans_start = datetime.now()
print('Starting data transformation...')

# TODO Do the transformation
trans_time = datetime.now() - trans_start
print(f'Finished transformation: {trans_time.seconds}s load time.')

##
# Loading
#
load_start = datetime.now()
print('Starting data loading...')

# TODO Load the data
loading_time = datetime.now() - load_start

print(f'Finished loading: {loading_time.seconds}s load time.')

# Final runtime
total_time = datetime.now() - start
print(f'Finished loading: {total_time.seconds}s load time.')
