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
# ## Dates

# %%
# Define path to files
# For MacOS
# PATH = "/Users/derekbanas/Documents/Tutorials/Python for Finance/Stocks/"
# For Windows
PATH = "D:/Python for Finance/Stocks/"

# Start date defaults
S_YEAR = 2017
S_MONTH = 1
S_DAY = 3
S_DATE_STR = "2017-01-03"
S_DATE_DATETIME = dt.datetime(S_YEAR, S_MONTH, S_DAY)

# End date defaults
E_YEAR = 2021
E_MONTH = 8
E_DAY = 19
E_DATE_STR = "2021-08-19"
E_DATE_DATETIME = dt.datetime(E_YEAR, E_MONTH, E_DAY)

# %% [markdown]
# ## Get Stock File Names in a List

# %%
files = [x for x in listdir(PATH) if isfile(join(PATH, x))]
tickers = [os.path.splitext(x)[0] for x in files]
tickers

# On MacOS Only
# tickers.remove('.DS_Store')
tickers.sort()
tickers

# %% [markdown]
# ## Function that Returns a Dataframe from a CSV

# %%
# Reads a dataframe from the CSV file, changes index to date and returns it
def get_df_from_csv(ticker):
    # Try to get the file and if it doesn't exist issue a warning
    try:
        df = pd.read_csv(PATH + ticker + '.csv')
    except FileNotFoundError:
        print("File Doesn't Exist")
    else:
        return df

# %% [markdown]
# ## Function that Saves Dataframe to CSV

# %%
def save_dataframe_to_csv(df, ticker):
    df.to_csv(PATH + ticker + '.csv')

# %% [markdown]
# ## Return 1st Valid Date in Dataframe

# %%
# Receives a start and end date and returns the 1st date in that range
def get_valid_dates(df, sdate, edate):
    
    try:
        mask = (df['Date'] > sdate) & (df['Date'] <= edate) 
        sm_df = df.loc[mask]
        sm_df = sm_df.set_index(['Date'])
    
        # Get smallest date that matches
        sm_date = sm_df.index.min()
        last_date = sm_df.index.max()
    
        # Add leading zeros to date
        # Split string on - and if a number is less than 2 add a zero in front
        date_leading = '-'.join(('0' if len(x)<2 else '')+x for x in sm_date.split('-'))
        date_ending = '-'.join(('0' if len(x)<2 else '')+x for x in last_date.split('-'))
        print(date_leading, " ", date_ending)
    except Exception:
        print("Date Corrupted")
    else:
        return date_leading, date_ending

# %% [markdown]
# ## Returns Return on Investment over Time

# %%
# Get ROI between 2 dates
def roi_between_dates(df, sdate, edate):
    
    try:
        # Gets the Adj Close price for 1st & last date 
        start_val = df.loc[sdate,'Adj Close'] 
        end_val = df.loc[edate,'Adj Close']
        roi = ((end_val - start_val) / start_val)
    except Exception:
        print("Data Corrupted")
    else:
        return roi

# %% [markdown]
# ## Get Mean Between Dates

# %%
def get_mean_between_dates(df, sdate, edate):
    mask = (df['Date'] > sdate) & (df['Date'] <= edate)
    return df.loc[mask]["Adj Close"].mean()

# %% [markdown]
# ## Get Standard Deviation Between Dates

# %%
def get_sd_between_dates(df, sdate, edate):
    mask = (df['Date'] > sdate) & (df['Date'] <= edate)
    return df.loc[mask]["Adj Close"].std()

# %% [markdown]
# ## Get Coefficient of Variation Between Dates

# %%
def get_cov_between_dates(df, sdate, edate):
    mean = get_mean_between_dates(df, sdate, edate)
    sd = get_sd_between_dates(df, sdate, edate)
    return sd / mean

# %% [markdown]
# ## Test Functions

# %%
# Get our 1st ticker
tickers[0]
print("Dataframe for Ticker", tickers[0])

# Get a dataframe for that ticker
stock_a = get_df_from_csv(tickers[0])
stock_a

# Get the first and last valid date in the date range
print(get_valid_dates(stock_a, '2020-01-01', '2020-12-31'))
sdate, edate = get_valid_dates(stock_a, '2020-01-01', '2020-12-31')
sdate
edate

print("Adj Close Mean :", get_mean_between_dates(stock_a, sdate, edate))
print("Adj Close Standard Deviation :", get_sd_between_dates(stock_a, sdate, edate))
print("Adj Close Coefficient of Variation :", get_cov_between_dates(stock_a, sdate, edate))

stock_a = stock_a.set_index(['Date'])
stock_a

print("Return on Investment since 2020:", roi_between_dates(stock_a, sdate, edate))

# %% [markdown]
# ## COV & ROI for All Stocks Over Defined Period

# %%
def get_cov_ror(tickers, sdate, edate):
    # Define column names for dataframe
    col_names = ["Ticker", "COV", "ROI"]
    
    # Create dataframe with column names
    df = pd.DataFrame(columns = col_names)
    
    for ticker in tickers:
        print("Working on :", ticker)
        s_df = get_df_from_csv(ticker)
    
        sdate2, edate2 = get_valid_dates(s_df, sdate, edate)
    
        cov = get_cov_between_dates(s_df, sdate2, edate2)
    
        # Set date as index
        s_df = s_df.set_index(['Date'])
        roi = roi_between_dates(s_df, sdate2, edate2)

        # Add stock data to new dataframe row
        # len provides the length of the dataframe which is the next open index
        df.loc[len(df.index)] = [ticker, cov, roi]
    
    return df

# %%
# Remove CRC GRUB AAN ARNC
market_df = get_cov_ror(tickers, '2017-01-03', '2017-12-31')

# %%
# Get top 20 stocks ROI
market_df.sort_values(by=['ROI'], ascending=False).head(20)

# %% [markdown]
# ## Merge Multiple Stocks in One Dataframe by Column Name

# %%
def merge_df_by_column_name(col_name, sdate, edate, *tickers):
    # Will hold data for all dataframes with the same column name
    mult_df = pd.DataFrame()
    
    for x in tickers:
        df = get_df_from_csv(x)
        df['Date'] = pd.to_datetime(df['Date'])
        # Use a mask to grab data between defined dates
        mask = (df['Date'] >= sdate) & (df['Date'] <= edate)
        mult_df[x] = df.loc[mask][col_name]
        
    return mult_df

# %% [markdown]
# ## Create a Correlation Matrix using FAANGS

# %%
# Correlation tells us how closely 2 stocks returns move together
# Correlation is a standardized value lying between -1 and 1
# When this value is greater that .5 we say that these stocks are strongly correlated
# Of course each stocks price is perfectly correlated with itself

# We focus on the correlation of returns because investors care about returns 

# Merge all stock price data into 1 dataframe
faang_list = ["FB", "AMZN", "AAPL", "NFLX", "GOOG"]
mult_df = merge_df_by_column_name('daily_return',  '2020-1-1', '2020-12-31', *faang_list)
mult_df

# Generate a Correlation Matrix
mult_df.corr()

# We can look at the correlation between Netflix and the others
mult_df.corr()['NFLX']

# We can plot this in a bar chart
mult_df.corr()['NFLX'].plot(kind='bar')

# %% [markdown]
# ## Get the Variance of a Stock

# %%
# Remember variance is a measure of how spread out a data set is
# Get Netflix variance
mult_df['NFLX'].var()

# Annualize by getting the number of samples and multiply
days = len(mult_df.index) # 253

nflx_a_var = mult_df['NFLX'].var() * 253
nflx_a_var

# %% [markdown]
# ## Get Covariance of Stocks

# %% [markdown]
# Covariance is the measure of the relationship between 2 blocks of data. The covariance of a
# stock to itself is the variance of that variable. 

# %%
mult_df.cov() * 253

# %% [markdown]
# ## Why do We Care About Risk      

# %% [markdown]
# Most investors don't handle massive flucuations in stock prices well. What we want to
# do at the very least is to make them aware of how dramatically their portfolios 
# returns may be. We can then do our best to minimize risk by adding other stocks
# that have returns that aren't as closely correlated.

# %% [markdown]
# ## Calculating a Portfolios Variance

# %% [markdown]
# When calculating the variance of a portfolio we must define its weight, or how much of
# the portfolio it makes up. If you add up the weight of all stocks you get a value of 1.
# 
# $ w_1, w_2 $ = Stock Weights
# 
# $ \sigma_1, \sigma_2 $ = Stock Standard Deviations
# 
# Portfolio Variance = $ (w_1\sigma_1 + w_2\sigma_2)^2 $
# 
# Since $ (a+b)^2 = a^2 + 2ab + b^2 $
# 
# Then the Portfolio Variance = $ w_1^2\sigma_1^2 + 2w_1\sigma_1w_2\sigma_2\rho_12 + w_2^2\sigma_2^2 $

# %%
# Let's create a portfolio made up of Facebook & Newmont Corporation
port_list = ["FB", "NEM"]
port_df = merge_df_by_column_name('daily_return',  '2020-1-1', '2020-12-31', *port_list)
port_df

# Generate a Correlation Matrix to see that they are not correlated
port_df.corr()

# Get prices at the beginning of Jan 2020 to calculate weight of both stocks
price_df = merge_df_by_column_name('Adj Close',  '2020-1-1', '2020-12-31', *["FB","NEM"])
price_df.head()

# I'll buy 1 share of FB at 209.78 & 5 of NEM for 41.74 for a total of 208.70
# Total Value = $418.48
fb_wt = 209.78 / 418.48
nem_wt = 208.70 / 418.48
fb_wt = .5012 # .5012
nem_wt = .4988 # .4987 and we'll change it to .4988 so they equal 1
wts = np.array([fb_wt, nem_wt])

# The portfolio variance is found from matrix multiplication
# We transpose the weights, multiply by the covarience and then the weight to get 
# the covariance of the portfolio
wts.T
port_var = np.dot(wts.T, np.dot(port_df.cov() * 253, wts))
print("Portfolio Var :", port_var)
print("FB Var :", port_df["FB"].var() * 253)
print("NEM Var :", port_df["NEM"].var() * 253)

# %%



