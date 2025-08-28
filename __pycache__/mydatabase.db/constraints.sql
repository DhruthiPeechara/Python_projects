from google.colab import files 
file = files.upload ()

import sqlite3

conn = sqlite3.connect('database.sqlite')

print("Opened database succesdfully ")

conn.excucute(''' CREATE TABLE CLASS_10
(SNO INT PRIMARY KEY NOT NULL,
Roll_No INT NOT NULL,
Name TEXT NOT NULL, 
AGE INT DEFAULT (15),
GENDER TEXT NOT NULL, 
Email-ID TEXT NOT NULL, 
Contact_No Real NOT NULL);''')

conn.excecute("INSERT INTO CLASS_10
(SNO,Roll_No)Name, Age, Email, Contact ")

VALUES (1,1, 'Allen, 14, 'Male, 'allen.g@gmail.com, 09875442367')

conn.excecute("INSERT INTO CLASS_10 
(SNO,Roll_No)Name, Age, Email, Contact ")

VALUES(2,2,Aisha, Aisha.m@gmail.com, 45678986543)

conn.excecute(INSERT INTO CLASS 10_
)