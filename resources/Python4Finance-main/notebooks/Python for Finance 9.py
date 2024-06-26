#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Provides ways to work with large multidimensional arrays
import numpy as np 
# Allows for further data manipulation and analysis
import pandas as pd
from pandas_datareader import data as web # Reads stock data 
import matplotlib.pyplot as plt # Plotting
import matplotlib.dates as mdates # Styling dates
get_ipython().run_line_magic('matplotlib', 'inline')

import datetime as dt # For defining dates
import mplfinance as mpf # Matplotlib finance

import time

# Used to get data from a directory
import os
from os import listdir
from os.path import isfile, join

#Statsmodels is a great library we can use to run regressions.
import statsmodels.api as sm
# Seaborn extends the capabilities of Matplotlib
import seaborn as sns
# Used for calculating regressions
from statsmodels.tsa.ar_model import AutoReg, ar_select_order


# ## Dates & Other Constants

# In[2]:


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

risk_free_rate = 0.0125 # Approximate 10 year bond rate


# ## Function that Saves Dataframe to CSV

# In[3]:


def save_dataframe_to_csv(df, ticker):
    df.to_csv(PATH + ticker + '.csv')


# ## Function that Returns a Dataframe from a CSV

# In[4]:


def get_df_from_csv(ticker):
    try:
        df = pd.read_csv(PATH + ticker + '.csv', index_col='Date', 
                         parse_dates=True)
    except FileNotFoundError:
        pass
        # print("File Doesn't Exist")
    else:
        return df


# ## Add Daily Return to Dataframe

# In[5]:


# Shift provides the value from the previous day
# NaN is displayed because there was no previous day price for the 1st calculation
def add_daily_return_to_df(df, ticker):
    df['daily_return'] = (df['Adj Close'] / df['Adj Close'].shift(1)) - 1
    # Save data to a CSV file
    save_dataframe_to_csv(df, ticker)
    return df  


# ## Merge Multiple Stocks in One Dataframe by Column Name

# In[43]:


def merge_df_by_column_name(col_name, sdate, edate, *tickers):
    # Will hold data for all dataframes with the same column name
    mult_df = pd.DataFrame()
    
    for x in tickers:
        df = get_df_from_csv(x)
        
        # NEW Check if your dataframe has duplicate indexes
        if not df.index.is_unique:
            # Delete duplicates 
            df = df.loc[~df.index.duplicated(), :]
        
        mask = (df.index >= sdate) & (df.index <= edate)
        mult_df[x] = df.loc[mask][col_name]
        
    return mult_df


# In[44]:


port_list = ["AMD", "CPRT"]
mult_df = merge_df_by_column_name('daily_return',  '2018-01-02', 
                                  '2021-09-10', *port_list)
mult_df


# ## Calculating Beta

# Beta provides the relationship between an investment and the overall market. Risky investments tend to fall further during bad times, but will increase quicker during good times. 
# 
# Beta is found by dividing the covariance of the stock and the market by the variance of the overall market. It is a measure of systematic risk that can't be diversified away.  
# 
# $ \beta = \frac{Cov(r_x, r_m)}{\sigma_m^2} $
# 
# $ \beta = 0 $ : No relation to market
# 
# $ \beta < 1 $ : Less risky than market
# 
# $ \beta > 1 $ : More risky than the market

# ## Examples

# Albertsons is a grocery store chain with a low beta of 0.5 because no matter what people need food and pharmecueticals. 
# 
# AMD manufacturers microchips and is a high beta stock at 1.4 because during hard times there is less demand for their products.

# ## Get S&P 500 and AMD Data

# In[45]:


# # Will hold S&P 500 adjusted close data
# sp_df = pd.DataFrame()

# # Download data from Yahoo
# sp_df = web.DataReader('^GSPC', 'yahoo', '2017-1-3', '2021-9-10')['Adj Close']

amd_df = get_df_from_csv('AMD')

amd_df


# In[46]:


sp_df = get_df_from_csv('^GSPC')

sp_df


# ## Add Daily Return & Save to CSV

# In[124]:


# # Save S&P to csv
# save_dataframe_to_csv(sp_df, '^GSPC')

# # Get dataframe from csv
# sp_df2 = get_df_from_csv('^GSPC')

# # Add daily return to dataframe
# add_daily_return_to_df(sp_df2, '^GSPC')
# sp_df2


# ## Find Beta for Stock versus S&P

# In[47]:


def find_beta(ticker):
    # Tickers analyzed being the S&P and the stock passed
    port_list =['^GSPC']
    port_list.append(ticker)

    mult_df = merge_df_by_column_name('daily_return',  '2018-01-02', 
                                  '2021-09-10', *port_list)
    
    # Provides the covariance between the securities
    cov = mult_df.cov() * 252
    
    # Get the covariance of the stock and the market
    cov_vs_market = cov.iloc[0,1]
    
    # Get annualized variance of the S&P
    sp_var = mult_df['^GSPC'].var() * 252
    
    # Beta is normally calculated over a 5 year period which is why you may see a difference
    beta = cov_vs_market / sp_var
    return beta


# ## Get Stock Beta

# In[48]:


print("AMD Beta :", find_beta('AMD'))


# ## Capital Asset Pricing Model

# Sharpe continued to create the CAPM based on the research of Markowitz. It focuses on investments in stocks and bonds. With it we can more exactly create portfolios that match the risk an investor is willing to assume. CAPM assumes a risk free asset which of course provides a small return. So if the investor wants less risk they simply buy more of the risk free assets.
# 
# There is risk that you can limit through diversifaction (Idiosyncratic) and risk that you can't (Systematic). This portfolio contains no Idiosyncratic risk and like before it lies on the efficient frontier.
# 
# To find this portfolio we will draw a line ( The Capital Market Line ) from the Y intercept to the efficient frontier. 
# 
# Here is the formula. The securities expected return equals the risk free asset plus Beta times the market return minus the risk free asset. it is common for $ r_m - r_f $ to be considered 5% which is called the Equity Risk Premium.
# 
# $ r_i = r_f + \beta_i (r_m - r_f) $

# ## Calculate AMDs Expected Return

# In[49]:


risk_free_rate = 0.013
ri = risk_free_rate + find_beta('AMD') * 0.05
ri


# ## Sharpe Ratio

# William Sharpe created the Sharpe Ratio to find the portfolio that provides the best return for the lowest amount of risk. 
# 
# *Sharpe Ratio* = $\frac{r_i - r_f}{\sigma_i}$
# 
# $r_f = $ Risk Free Rate
# 
# $r_i = $ Rate of Return of the stock
# 
# $\sigma_i = $ Standard Deviation of the Stock
# 
# As return increases so does the Sharpe Ratio, but as Standard Deviation increase the Sharpe Ratio decreases.

# In[50]:


# We can find the Sharpe ratio for AMD
amd_sharpe = (ri - risk_free_rate) / (mult_df['AMD'].std() * 252 ** 0.5)
amd_sharpe


# ## Get Stock Prices on Date

# In[94]:


def get_prices_on_date(stocks_df, date):
    return stocks_df.loc[pd.DatetimeIndex([date])]['Adj Close'].item()


# ## Returns the Value of Portfolio by Date

# In[60]:


def get_port_val_by_date(date, shares, tickers):
    port_prices = merge_df_by_column_name('Adj Close',  date, 
                                  date, *port_list)
    # Convert from dataframe to Python list
    port_prices = port_prices.values.tolist()
    # Trick that converts a list of lists into a single list
    port_prices = sum(port_prices, [])
    
    # Create a list of values by multiplying shares by price
    value_list = []
    for price, share in zip(port_prices, shares):
        value_list.append(price * share)
    
    return sum(value_list)


# ## Get Value of Portfolio at Beginning and End of Year

# In[70]:


port_list = ["GNRC", "CPRT", "ODFL", "AMD", "PAYC", "CHTR", "MKC", 
             "PG", "PGR", "NEM", "CCI", "COG"]

port_shares = [25, 20, 22, 26, 1, 1, 4, 1, 5, 28, 3, 7]

# Portfolio value at start of 2020
port_val_start = get_port_val_by_date('2020-01-02', port_shares, port_list)
print("Portfolio Value at Start of 2020 : $%2.2f" % (port_val_start))

# Portfolio value at end of 2020
port_val_end = get_port_val_by_date('2020-12-31', port_shares, port_list)
print("Portfolio Value at End of 2020 : $%2.2f" % (port_val_end))


# ## Calculate Return on Investment

# ROI = $\frac{Final Value - Initial Value}{Initial Value}$

# In[102]:


# Rate of return for portfolio
roi_port = (port_val_end - port_val_start) / port_val_end
print("Portfolio ROI at End of 2020 : %2.2f %%" % (roi_port * 100))

# S&P ROI
sp_df = get_df_from_csv('^GSPC')
sp_val_start = get_prices_on_date(sp_df, '2020-01-02')
sp_val_end = get_prices_on_date(sp_df, '2020-12-31')
sp_roi = (sp_val_end - sp_val_start) / sp_val_end
print("S&P ROI at End of 2020 : %2.2f %%" % (sp_roi * 100))


# ## Find Daily Return for Whole Portfolio

# To find the daily return for the whole portfolio, I must multiply the daily price by the number of shares for each security. Then sum those values for all stocks per day. This creates a portfolio list of daily prices. Then I can calculate the daily return.

# In[82]:


def get_port_daily_return(sdate, edate, shares, tickers):
    # Merge all daily prices for all stocks into 1 dataframe
    mult_df = merge_df_by_column_name('Adj Close',  sdate, 
                                  edate, *port_list)
    
    # Get the number of stocks in portfolio
    num_cols = len(mult_df.columns)
    
    # Multiply each stock column by the number of shares
    i = 0
    while i < num_cols:
        mult_df[tickers[i]] = mult_df[tickers[i]].apply(lambda x: x * shares[i])
        i += 1
        
    # Create a new column with the sums of all stocks named Total
    mult_df['Total'] = mult_df.iloc[:, 0:num_cols].sum(axis=1)
    
    # Add column for portfolio daily return
    mult_df['daily_return'] = (mult_df['Total'] / mult_df['Total'].shift(1)) - 1
    
    return mult_df


# In[116]:


tot_port_df = get_port_daily_return('2020-01-02', '2020-12-31', 
                                    port_shares, port_list)
tot_port_df


# ## Find Portfolio Beta

# In[109]:


def find_port_beta(port_df, sdate, edate):
    # Will hold data for S&P and my portfolio
    mult_df = pd.DataFrame()
    
    # Mask defining the dates worth of data that we want
    port_mask = (port_df.index >= sdate) & (port_df.index <= edate)
    
    # Get S&P Dataframe
    sp_df = get_df_from_csv('^GSPC')
    
    sp_mask = (sp_df.index >= sdate) & (sp_df.index <= edate)
    
    # Add S&P daily return to dataframe
    mult_df['^GSPC'] = sp_df.loc[sp_mask]['daily_return']
    
    # Add the portfolio daily return data
    mult_df['Portfolio'] = port_df.loc[port_mask]['daily_return']
    
    # Provides the covariance between the securities
    cov = mult_df.cov() * 252
    
    # Get the covariance of the stocks and the market
    cov_vs_market = cov.iloc[0,1]
    
    # Get annualized variance of the S&P
    sp_var = mult_df['^GSPC'].var() * 252
    
    # Beta is normally calculated over a 5 year period which is why you may see a difference
    beta = cov_vs_market / sp_var
    return beta


# ## Calculating Alpha

# Alpha provides a measure of how well a portfolio has performed. The CAPM assumes an Alpha of 0. Good portfolios have a positive Alpha, while poor have negative. 
# 
# Alpha = R – Rf – beta (Rm-Rf)
# 
# * R represents the portfolio return
# * Rf represents the risk-free rate of return
# * Beta represents the systematic risk of a portfolio
# * Rm represents the market return, per a benchmark

# In[111]:


port_beta = find_port_beta(tot_port_df, '2020-01-02', '2020-12-31')
port_beta


# In[115]:


port_alpha = roi_port - risk_free_rate - (port_beta * (sp_roi - risk_free_rate))
print("Portfolio Alpha : %2.2f %%" % (port_alpha * 100))


# This means our portfolio outperformed the market in 2020 by 26.74%
