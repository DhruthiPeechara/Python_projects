import pandas as pd
import seaborn as sns

from google.colab import files
Files= files.upload(Weather Dataset - Google Sheets_files)

weather = pd.read_csv('Trial Activity DataSet.csv')

weather.head()

weather.info 

sns.barplot(weather['wind_speed'], weather['temperature'])

sns.distplot(weather['temperature'])

sns.distplot(weather['humidity'], rug=True)

sns.jointplot(weather['humidity'], weather['temperature'])

sns.pairplot(weather[['humidity', 'temperature', 'air_pollution_index']])

sns.stripplot(weather['weather_type'], weather['temperature'], jitter = True)

