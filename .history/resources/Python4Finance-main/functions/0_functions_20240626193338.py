import numpy as np  # Provides ways to work with large multidimensional arrays
import pandas as pd  # Allows for further data manipulation and analysis
from pandas_datareader import data as web  # Reads stock data
import datetime as dt  # For defining dates
import time  # For handling sleep/delays

import numpy as np  # Provides ways to work with large multidimensional arrays
import pandas as pd  # Allows for further data manipulation and analysis
from pandas_datareader import data as web  # Reads stock data
import datetime as dt  # For defining dates
import time  # For handling sleep/delays
import matplotlib.pyplot as plt  # Plotting
import matplotlib.dates as mdates  # Styling dates
import mplfinance as mpf  # Matplotlib finance




def get_return_defined_time(df, syear, smonth, sday, eyear, emonth, eday):
    """
    Calculates the total return over a specified time period.
    
    Parameters:
    df (pd.DataFrame): The dataframe containing stock data.
    syear (int): Start year of the period.
    smonth (int): Start month of the period.
    sday (int): Start day of the period.
    eyear (int): End year of the period.
    emonth (int): End month of the period.
    eday (int): End day of the period.
    
    Returns:
    float: The total return over the specified period.
    """
    start = f"{syear}-{smonth}-{sday}"
    end = f"{eyear}-{emonth}-{eday}"
    df['Date'] = pd.to_datetime(df['Date'])
    
    mask = (df['Date'] >= start) & (df['Date'] <= end)
    daily_ret = df.loc[mask]['daily_return'].mean()
    days = df.loc[mask].shape[0]

    return (days * daily_ret)




def merge_df_by_column_name(col_name, syear, smonth, sday, eyear, emonth, eday, *tickers):
    """
    Merges data from multiple stocks into one dataframe by a specific column name.
    
    Parameters:
    col_name (str): The column name to merge by.
    syear (int): Start year of the period.
    smonth (int): Start month of the period.
    sday (int): Start day of the period.
    eyear (int): End year of the period.
    emonth (int): End month of the period.
    eday (int): End day of the period.
    tickers (str): Stock ticker symbols.
    
    Returns:
    pd.DataFrame: The merged dataframe.
    """
    mult_df = pd.DataFrame()
    start = f"{syear}-{smonth}-{sday}"
   

    end = f"{eyear}-{emonth}-{eday}"
        
    for x in tickers:
        mult_df[x] = web.DataReader(x, 'yahoo', start, end)[col_name]
        
    return mult_df



def get_roi_defined_time(df):
    """
    Calculates the return on investment over a specified time period.
    
    Parameters:
    df (pd.DataFrame): The dataframe containing stock data.
    
    Returns:
    float: The return on investment over the specified period.
    """
    df['Date'] = pd.to_datetime(df['Date'])
    start_val = df[df['Date'] == S_DATE_STR]['Adj Close'][0]
    end_val = df[df['Date'] == E_DATE_STR]['Adj Close'].item()
    
    roi = (end_val - start_val) / start_val
    return roi

def get_cov(stock_df):
    """
    Calculates the coefficient of variation for the stock data.
    
    Parameters:
    stock_df (pd.DataFrame): The dataframe containing stock data.
    
    Returns:
    float: The coefficient of variation.
    """
    mean = stock_df['Adj Close'].mean()
    sd = stock_df['Adj Close'].std()
    cov = sd / mean
    return cov

Here are the new functions extracted from the provided script:

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

def roi_between_dates(df, sdate, edate):
    """
    Calculates the return on investment (ROI) between two dates.
    
    Parameters:
    df (pd.DataFrame): The dataframe containing stock data.
    sdate (str): The start date in 'YYYY-MM-DD' format.
    edate (str): The end date in 'YYYY-MM-DD' format.
    
    Returns:
    float: The ROI between the specified dates.
    """
    try:
        start_val = df.loc[sdate,'Adj Close'] 
        end_val = df.loc[edate,'Adj Close']
        roi = ((end_val - start_val) / start_val)
    except Exception:
        print("Data Corrupted")
    else:
        return roi

def get_mean_between_dates(df, sdate, edate):
    """
    Calculates the mean adjusted close price between two dates.
    
    Parameters:
    df (pd.DataFrame): The dataframe containing stock data.
    sdate (str): The start date in 'YYYY-MM-DD' format.
    edate (str): The end date in 'YYYY-MM-DD' format.
    
    Returns:
    float: The mean adjusted close price.
    """
    mask = (df['Date'] > sdate) & (df['Date'] <= edate)
    return df.loc[mask]["Adj Close"].mean()

def get_sd_between_dates(df, sdate, edate):
    """
    Calculates the standard deviation of the adjusted close price between two dates.
    
    Parameters:
    df (pd.DataFrame): The dataframe containing stock data.
    sdate (str): The start date in 'YYYY-MM-DD' format.
    edate (str): The end date in 'YYYY-MM-DD' format.
    
    Returns:
    float: The standard deviation of the adjusted close price.
    """
    mask = (df['Date'] > sdate) & (df['Date'] <= edate)
    return df.loc[mask]["Adj Close"].std()

def get_cov_between_dates(df, sdate, edate):
    """
    Calculates the coefficient of variation of the adjusted close price between two dates.
    
    Parameters:
    df (pd.DataFrame): The dataframe containing stock data.
    sdate (str): The start date in 'YYYY-MM-DD' format.
    edate (str): The end date in 'YYYY-MM-DD' format.
    
    Returns:
    float: The coefficient of variation of the adjusted close price.
    """
    mean = get_mean_between_dates(df, sdate, edate)
    sd = get_sd_between_dates(df, sdate, edate)
    return sd / mean

def get_cov_ror(tickers, sdate, edate):
    """
    Calculates the coefficient of variation (COV) and return on investment (ROI) for all stocks over a defined period.
    
    Parameters:
    tickers (list): The list of stock ticker symbols.
    sdate (str): The start date in 'YYYY-MM-DD' format.
    edate (str): The end date in 'YYYY-MM-DD' format.
    
    Returns:
    pd.DataFrame: A dataframe containing the ticker, COV, and ROI for each stock.
    """
    col_names = ["Ticker", "COV", "ROI"]
    df = pd.DataFrame(columns = col_names)
    
    for ticker in tickers:
        print("Working on :", ticker)
        s_df = get_df_from_csv(ticker)
    
        sdate2, edate2 = get_valid_dates(s_df, sdate, edate)
    
        cov = get_cov_between_dates(s_df, sdate2, edate2)
    
        s_df = s_df.set_index(['Date'])
        roi = roi_between_dates(s_df, sdate2, edate2)

        df.loc[len(df.index)] = [ticker, cov, roi]
    
    return df

def merge_df_by_column_name(col_name, sdate, edate, *tickers):
    """
    Merges multiple dataframes by a common column name.
    
    Parameters:
    col_name (str): The name of the column to merge on.
    sdate (str): The start date in 'YYYY-MM-DD' format.
    edate (str): The end date in 'YYYY-MM-DD' format.
    *tickers (str): The stock ticker symbols.
    
    Returns:
    pd.DataFrame: A dataframe containing the merged data.
    """
    mult_df = pd.DataFrame()
    
    for x in tickers:
        df = get_df_from_csv(x)
        df['Date'] = pd.to_datetime(df['Date'])
        mask = (df['Date'] >= sdate) & (df['Date'] <= edate)
        mult_df[x] = df.loc[mask][col_name]
        
    return mult_df


