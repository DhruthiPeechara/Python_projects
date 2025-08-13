import sqlite3

database = 'database.sqlite'

conn = sqlite3.connect(database)
print('opened data succesfully')

import pandas as pd
tables = pd.read_sql("""SELECT*
FROM sqlite_master
WHERE type= 'table';""", conn)

-- Get a list of tables and views in the current database
SELECT table_catalog [database], table_schema [schema], table_name name, table_type type
FROM INFORMATION_SCHEMA.TABLES
GO

matches.info()
