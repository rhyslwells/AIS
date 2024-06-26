import numpy as np  # Provides ways to work with large multidimensional arrays
import pandas as pd  # Allows for further data manipulation and analysis
from pandas_datareader import data as web  # Reads stock data
import datetime as dt  # For defining dates
import time  # For handling sleep/delays
import matplotlib.pyplot as plt  # Plotting
import matplotlib.dates as mdates  # Styling dates
import mplfinance as mpf  # Matplotlib finance
from statsmodels.tsa.ar_model import AutoReg, ar_select_order

def sectors():
    indus_df = sec_df.loc[sec_df['Sector'] == "Industrial"]
    health_df = sec_df.loc[sec_df['Sector'] == "Healthcare"]
    it_df = sec_df.loc[sec_df['Sector'] == "Information Technology"]
    comm_df = sec_df.loc[sec_df['Sector'] == "Communication"]
    staple_df = sec_df.loc[sec_df['Sector'] == "Staples"]
    discretion_df = sec_df.loc[sec_df['Sector'] == "Discretionary"]
    utility_df = sec_df.loc[sec_df['Sector'] == "Utilities"]
    financial_df = sec_df.loc[sec_df['Sector'] == "Financials"]
    material_df = sec_df.loc[sec_df['Sector'] == "Materials"]
    restate_df = sec_df.loc[sec_df['Sector'] == "Real Estate"]
    energy_df = sec_df.loc[sec_df['Sector'] == "Energy"]

    industrial = get_cum_ret_for_stocks(indus_df)
    health_care = get_cum_ret_for_stocks(health_df)
    it = get_cum_ret_for_stocks(it_df)
    commun = get_cum_ret_for_stocks(comm_df)
    staple = get_cum_ret_for_stocks(staple_df)
    discretion = get_cum_ret_for_stocks(discretion_df)
    utility = get_cum_ret_for_stocks(utility_df)
    finance = get_cum_ret_for_stocks(financial_df)
    material = get_cum_ret_for_stocks(material_df)
    restate = get_cum_ret_for_stocks(restate_df)
    energy = get_cum_ret_for_stocks(energy_df)

# Function to get stock price on a specific date
def get_stock_price_on_date(ticker, date):
    df = get_df_from_csv(ticker)
    df = df.set_index(['Date'])
    return df.loc[date, 'Adj Close']


# Function to calculate diversifiable risk
def calc_diversifiable_risk(df, tickers, weights):
    # Gets number of days
    days = len(df.index)
    # Calculate covariance of portfolio
    port_covar = np.dot(weights.T, np.dot(df.cov() * days, weights)) 
    
    i = 0
    while i < len(tickers):
        wt_sq = weights[i] ** 2
        stk_var = df[tickers[i]].var() * days
        wt_var = wt_sq * stk_var
        port_covar = port_covar - wt_var
        i += 1
    return port_covar

def find_beta(ticker):
    # Tickers analyzed being the S&P and the stock passed
    port_list =['GSPC']
    port_list.append(ticker)

    mult_df = merge_df_by_column_name('daily_return',  '2018-01-02', 
                                  '2021-09-10', *port_list)
    
    # Provides the covariance between the securities
    cov = mult_df.cov() * 252
    
    # Get the covariance of the stock and the market
    cov_vs_market = cov.iloc[0,1]
    
    # Get annualized variance of the S&P
    sp_var = mult_df['GSPC'].var() * 252
    
    # Beta is normally calculated over a 5 year period which is why you may see a difference
    beta = cov_vs_market / sp_var
    return beta


def get_valid_dates(df, sdate, edate):
    """
    Receives a start and end date and returns the first valid date in that range.
    
    Parameters:
    df (pd.DataFrame): The dataframe containing stock data.
    sdate (str): The start date in 'YYYY-MM-DD' format.
    edate (str): The end date in 'YYYY-MM-DD' format.
    
    Returns:
    tuple: The earliest and latest valid dates within the specified range.
    """
    try:
        mask = (df['Date'] > sdate) & (df['Date'] <= edate) 
        sm_df = df.loc[mask]
        sm_df = sm_df.set_index(['Date'])
    
        sm_date = sm_df.index.min()
        last_date = sm_df.index.max()
    
        date_leading = '-'.join(('0' if len(x)<2 else '')+x for x in sm_date.split('-'))
        date_ending = '-'.join(('0' if len(x)<2 else '')+x for x in last_date.split('-'))
        print(date_leading, " ", date_ending)
    except Exception:
        print("Date Corrupted")
    else:
        return date_leading, date_ending




