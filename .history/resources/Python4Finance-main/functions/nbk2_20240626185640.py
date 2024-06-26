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

# Used to get data from a directory
import os
from os import listdir
from os.path import isfile, join

# %% [markdown]
# ## Default Values

# %%
# Define path to files
path = "D:/Python for Finance/Stocks/"

# Start date defaults
S_YEAR = 2017
S_MONTH = 1
S_DAY = 3
S_DATE_STR = f"{S_YEAR}-{S_MONTH}-{S_DAY}"
S_DATE_DATETIME = dt.datetime(S_YEAR, S_MONTH, S_DAY)

# End date defaults
E_YEAR = 2021
E_MONTH = 8
E_DAY = 19
E_DATE_STR = f"{E_YEAR}-{E_MONTH}-{E_DAY}"
E_DATE_DATETIME = dt.datetime(E_YEAR, E_MONTH, E_DAY)

# %% [markdown]
# ## Get Stock File Names in a List

# %%
# listdir returns all files in the directory and isfile will return true
# if it is a file and then we store its name in our list named files
files = [x for x in listdir(path) if isfile(join(path, x))]

# Remove extension from file names
# Splitext splits the file name into 2 parts being the name and extension
# We say get all file names and then store just the name in our list named files
tickers = [os.path.splitext(x)[0] for x in files]
tickers

# %% [markdown]
# ## Create a Dataframe from our List

# %%
stock_df = pd.DataFrame(tickers,columns=['Ticker'])
stock_df

# %% [markdown]
# ## Function that Returns a Dataframe from a CSV

# %%
# Reads a dataframe from the CSV file, changes index to date and returns it
def get_df_from_csv(ticker):
    
    # Try to get the file and if it doesn't exist issue a warning
    try:
        df = pd.read_csv(path + ticker + '.csv')
    except FileNotFoundError:
        print("File Doesn't Exist")
    else:
        return df

# %% [markdown]
# ## Function that Saves Dataframe to CSV

# %%
def save_dataframe_to_csv(df, ticker):
    df.to_csv(path + ticker + '.csv')

# %% [markdown]
# ## Delete Unnamed Columns in CSV Files

# %%
def delete_unnamed_cols(df):
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    return df

# %% [markdown]
# ## Add Daily Return to Dataframe

# %%
# We calculate a percentage rate of return for each day to compare investments.
# Simple Rate of Return = (End Price - Beginning Price) / Beginning Price OR (EP / BP) - 1

# Shift provides the value from the previous day
# NaN is displayed because there was no previous day price for the 1st calculation
def add_daily_return_to_df(df, ticker):
    df['daily_return'] = (df['Adj Close'] / df['Adj Close'].shift(1)) - 1
    # Save data to a CSV file
    df.to_csv(path + ticker + '.csv')
    return df  

# %% [markdown]
# ## Returns Return on Investment over Time

# %%
# Return on Investment is the return you received from your investment
# This amount does not include your initial investment
# If you invest 100 and have 200 after 5 years
# ROI = End Value (200) - Initial Value (100) / Inital Value = 1
# Your new total is Inital Investment + 1 * Inital Investment = 200

def get_roi_defined_time(df):
    # Set as a datetime
    df['Date'] = pd.to_datetime(df['Date'])
    start_val = df[df['Date'] == S_DATE_STR]['Adj Close'][0]
    print("Initial Price :", start_val)
    
    # ----- I CHANGED THIS AFTER THE VIDEO -----
    
    end_val = df[df['Date'] == E_DATE_STR]['Adj Close']
    print(end_val.item())
    print("Final Price :", end_val.item())
    
    # ----- END OF VIDEO CHANGES -----
    
    # Calculate return on investment
    roi = (end_val - start_val) / start_val

    # Return the total return between 2 dates
    return roi

# %% [markdown]
# ## Get Coefficient of Variation

# %%
# Receives the dataframe with the Adj Close data and returns the coefficient of variation
def get_cov(stock_df):
    mean = stock_df['Adj Close'].mean()
    sd = stock_df['Adj Close'].std()
    cov = sd / mean
    return cov

# %% [markdown]
# ## Test Functions

# %%
# Create a backup for all original stock data

# Get our 1st ticker
tickers[0]

# Get a dataframe for that ticker
stock_a = get_df_from_csv(tickers[0])
stock_a

# Add daily return to this dataframe
add_daily_return_to_df(stock_a, tickers[0])
stock_a

# Delete unnamed columns in dataframe
stock_a = delete_unnamed_cols(stock_a)
stock_a

# Save cleaned dataframe to csv
save_dataframe_to_csv(stock_a, tickers[0])

# %% [markdown]
# ## Add Daily Returns & Clean Up All Files

# %%
# Create a backup for all original stock data

# Cycle through all tickers
for ticker in tickers:
    print("Working on :", ticker)
    
    # Get a dataframe for that ticker
    stock_df = get_df_from_csv(ticker)
    
    # Add daily return to this dataframe
    add_daily_return_to_df(stock_df, ticker)
    
    # Delete unnamed columns in dataframe
    stock_df = delete_unnamed_cols(stock_df)
    
    # Save cleaned dataframe to csv
    save_dataframe_to_csv(stock_df, ticker)

# %% [markdown]
# ## Get Stock Return over Time Period & Coefficient of Variation

# %%
stock_a

# Get total return since 2017
# Final Price 167.67 = (44.77 * 2.745) + 44.77
get_roi_defined_time(stock_a)

# Get coefficient of variation 
# This is higher than normal because I'm using many years instead of one
# get_cov(stock_a)

# %%



