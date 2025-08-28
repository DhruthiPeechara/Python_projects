from google.colab import files 
file = files.upload()

"""### **2. Connect with SQLite Database **"""

import sqlite3 

database = 'database.sqlite'

conn = sqlite3.connect(database)
print('opened date successfully')

import pandas as pd 
tables = pd.read_sql (""" SELECT *
                    FROM sqlite_master
                    WHERE type ='table';""",conn)

tables


)