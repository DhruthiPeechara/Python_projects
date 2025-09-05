from google.colab import files 
uploaded = files.upload()

import pandas as pd 
import numpy as np 
from datatime import datatime 
import sqlite3  

database = 'database.sqlite'
conn = sqlite3.connect(databse )

tables = pd.read_sql(""" SELECT 
FROM  sqlite_master 
WHERE type = 'table;""", conn)

tables 

match_details= pd.read_sql('''SELECT Season_Id, Match_id 
v.venue_name, c.city_name )