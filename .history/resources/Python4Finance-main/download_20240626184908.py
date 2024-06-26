# %%
# Provides ways to work with large multidimensional arrays
import numpy as np 
# Allows for further data manipulation and analysis
import pandas as pd
from pandas_datareader import data as web # Reads stock data 
import matplotlib.pyplot as plt # Plotting
import matplotlib.dates as mdates # Styling dates
%matplotlib inline

import datetime as dt # For defining dates
import mplfinance as mpf # Matplotlib finance

import time

# %% [markdown]
# ## Holds Stocks Not Downloaded

# %%


# %% [markdown]
# ## Function that Saves Stock Data to CSV

# %%
# Function that gets a dataframe by providing a ticker and starting date
def save_to_csv_from_yahoo(folder, ticker, syear, smonth, sday, eyear, emonth, eday):
    # Defines the time periods to use
    start = dt.datetime(syear, smonth, sday)
    end = dt.datetime(eyear, emonth, eday)
    
    try:
        print("Get Data for : ", ticker)
        # Reads data into a dataframe
        df = web.DataReader(ticker, 'yahoo', start, end)['Adj Close']
    
        # Wait 10 seconds
        time.sleep(10)
    
        # Save data to a CSV file
        df.to_csv(folder + ticker + '.csv')
    except Exception as ex:
        return()
        # stocks_not_downloaded.append(ticker)
        # print("Couldn't Get Data for :", ticker)


# %%
folder="data"
ticker="GOOGL"
start = dt.datetime(2018, 1, 1)
end = dt.datetime(2019, 1, 1)
df = web.DataReader(ticker, 'yahoo', start, end)['Adj Close']


# %%

save_to_csv_from_yahoo(folder, ticker, 2017, 1, 1, 2021, 8, 19)


# %% [markdown]
# ## Function that Returns a Stock Dataframe from a CSV

# %%
# # Reads a dataframe from the CSV file, changes index to date and returns it
# def get_stock_df_from_csv(folder, ticker):
    
#     # Try to get the file and if it doesn't exist issue a warning
#     try:
#         df = pd.read_csv(folder + ticker + '.csv')
#     except FileNotFoundError:
#         print("File Doesn't Exist")
#     else:
#         return df

# %% [markdown]
# ## Returns a Named Columns Data from a CSV

# %%
# def get_column_from_csv(file, col_name):
#     # Try to get the file and if it doesn't exist issue a warning
#     try:
#         df = pd.read_csv(file)
#     except FileNotFoundError:
#         print("File Doesn't Exist")
#     else:
#         return df[col_name]

# %% [markdown]
# ## Test Receiving Stock Tickers

# %%
tickers = get_column_from_csv("D:/Python for Finance/Wilshire-5000-Stocks.csv", "Ticker")
tickers

# for x in tickers:
#     print(x, end=", ")


# %% [markdown]
# ## Get 5 Years of Data for the 1st 20 Stocks

# %%
# # Folder used to store stock data
# folder = "D:/Python for Finance/Stocks/"

# for x in range(20):
#   save_to_csv_from_yahoo(folder, tickers[x], 2017, 1, 1, 2021, 8, 19)
# print("Finished")

# %%


# %% [markdown]
# ## Get Next 80 Stocks

# %%
# for x in range(20, 100):
#   save_to_csv_from_yahoo(folder, tickers[x], 2017, 1, 1, 2021, 8, 19)
# print("Finished")

# %%
for x in range(3000, 3480):
  save_to_csv_from_yahoo(folder, tickers[x], 2017, 1, 1, 2021, 8, 19)
print("Finished")
stocks_not_downloaded

# %%
for x in missing_stocks:
    save_to_csv_from_yahoo(folder, x, 2017, 1, 1, 2021, 8, 19)
print("Finished")
stocks_not_downloaded

# %%



