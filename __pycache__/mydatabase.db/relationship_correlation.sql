from google.colab import files 
uploaded = files.upload()

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 

data = pd.read_csv('gapminder(2007).csv')

data.head()

data.info()

data.isnull().any()

sns.scatterplot(data=data, x = 'gdp_cap', y='life_exp')

plt.show()

sns.scatterplot.(data=data, x ='gdp_cap', y='life_exp', hue= 'continent')

plt.show()

sns.scatterplot(x='total_map'y='coordinates')


