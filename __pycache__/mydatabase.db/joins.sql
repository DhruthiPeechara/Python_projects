from google.colab import files 
uploaded = files.upload()

import numpy as np 
import pandas as pd 
import sqlite3 

database = 'database.sqlite'

conn  = sqlite3.connect(database)

tables = pd.read_sql(""" SELECT * 
                        FROM sqlite_master
                        WHERE type = 'table'""", conn)

tables 

joined_city = pd.read_sql(""")


