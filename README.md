# League of Legends ETL (Extract, Transform, Load)

* With the World Championship Series underway, I often find myself with some very specific questions about the various players, teams, and specific games. Though the data is available in CSV form through a third party organization (Shoutout to Tim Sevenhuysen at https://oracleselixir.com/), it can be hard to answer some of my questions just by looking at the Excel spreadsheet. 
<br>

* I've decided to generate an ETL process using Python and SQL server as a means of warehousing data for easy querying (and as a fun exercise). The plan is as follows:

    1. Acquire the dataset and preparing it for loading using Python
    
    2. Design a relational database for the warehouse
    
    3. Enforce specific validation rules on the data using Python
    
    4. Clean and transform based on validation rules and database requirements
    
    5. Load into a SQL Server relational database that I designed using Python and pyodbc
    
    6. Extract insights using SQL
    
    7. Hook up PowerBI to the database to generate a dashboard for further insights

# Installation

- `pip install -r requirements.txt`
- `cp config.example config.json`
- Run the database script `database.SQL`
- To run the ETL process start-to-finish, run the `common.py` file