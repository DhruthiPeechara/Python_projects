import pandas as pd 
import matplotlib.pyplot as plt 

countries_df = pd.read_csv('countries.csv')

countries = countries_df 

countries.head(3)

c_S2 = countries.loc[countries['year']== 1952 ]
c_s2.head()

c_07 = countries.loc{{countries}'year'}== 2007
c_07.head()

c_merge.head()

c_merge.drop(('year_x','year_y'), axis=1)
