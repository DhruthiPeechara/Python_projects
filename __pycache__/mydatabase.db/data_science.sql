import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as ans 

df=pd.read_csv("country_vaccinations.csv")

df.head(10)

df.isnull().sum()

df.dropna()

df.fillna(0)

