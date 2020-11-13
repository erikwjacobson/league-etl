# Housekeeping
import pyodbc
import json


def connect(autocommit=True):
    config = json.loads(open('../config.json', 'r').read())
    conn = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={config["SERVER"]};DATABASE={config["DATABASE"]};UID={config["USERNAME"]};PWD={config["PASSWORD"]}', autocommit=autocommit)
    return conn
