import sqlite3

database = 'database.sqlite'

conn = sqlite3.connect(database)
print('opened data succesfully')

print("Database connected")

import pandas as pd 

new_teams = pd.read_sql("""SELECT*
                        FROM Team 
                        WHERE Team_name LIKE DEccan chargers'

min_max_margin = pd.read_sql("""SELECT MIN (WIN_Margin), MAX(Win_Margin))
                        FROM Match;""", conn)
min_max_margin 

