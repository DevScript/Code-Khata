
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from statsmodels.tsa.arima_model import ARIMA

#read the data
df = pd.read_csv('Data Science\Time Series Analysis\AirPassengers.csv', index_col='Month', parse_dates=True)
df.index.freq = 'MS'

#plot the data
df.plot()

#split the data
train_data = df.iloc[:len(df)-12]
test_data = df.iloc[len(df)-12:]

#fit the model
model = ARIMA(train_data['#Passengers'], order=(1,1,1))
results = model.fit()

#plot the results
results.plot_diagnostics(figsize=(12,8))
plt.show()

#predict the values
start = len(train_data)
end = len(train_data) + len(test_data) - 1

predictions = results.predict(start, end, typ='levels').rename('ARIMA Predictions')

#plot the predictions
test_data['#Passengers'].plot(legend=True)
predictions.plot(legend=True)

#evaluate the model
from statsmodels.tools.eval_measures import rmse
error = rmse(test_data['#Passengers'], predictions)
print(f'ARIMA(1,1,1) RMSE Error: {error}')

#forecast the future
model = ARIMA(df['#Passengers'], order=(1,1,1))
results = model.fit()
fcast = results.predict(len(df), len(df)+11, typ='levels').rename('ARIMA Forecast')

#plot the forecast
df['#Passengers'].plot(figsize=(12,5), legend=True)
fcast.plot(legend=True)




