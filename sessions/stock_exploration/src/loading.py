import pandas as pd
import numpy as np
import yfinance as yf
import datetime
import datetime as dt
import time
import pandas_datareader.data as web

def save_to_csv_from_yahoo(folder, ticker, syear, smonth, sday, eyear, emonth, eday):
    """
    Fetches adjusted close prices for a given ticker from Yahoo Finance 
    within a specified date range and saves the data to a CSV file.
    
    Parameters:
    folder (str): The directory where the CSV file will be saved.
    ticker (str): The stock ticker symbol.
    syear (int): The start year of the data fetching period.
    smonth (int): The start month of the data fetching period.
    sday (int): The start day of the data fetching period.
    eyear (int): The end year of the data fetching period.
    emonth (int): The end month of the data fetching period.
    eday (int): The end day of the data fetching period.
    """
    start = dt.datetime(syear, smonth, sday)
    end = dt.datetime(eyear, emonth, eday)
    
    try:
        print("Get Data for : ", ticker)
        df = web.DataReader(ticker, 'yahoo', start, end)['Adj Close']
        time.sleep(10)
        df.to_csv(folder + ticker + '.csv')
    except Exception as ex:
        return()
    
def get_stock_df_from_csv(folder, ticker):
    """
    Reads a CSV file containing stock data, changes the index to date,
    and returns the dataframe.
    
    Parameters:
    folder (str): The directory where the CSV file is located.
    ticker (str): The stock ticker symbol.
    
    Returns:
    pd.DataFrame: The dataframe containing stock data.
    """
    try:
        df = pd.read_csv(folder + ticker + '.csv')
    except FileNotFoundError:
        print("File Doesn't Exist")
    else:
        return df

def get_column_from_csv(file, col_name):
    """
    Reads a specific column from a CSV file and returns its data.
    
    Parameters:
    file (str): The path to the CSV file.
    col_name (str): The name of the column to be read.
    
    Returns:
    pd.Series: The series containing the column data.
    """
    try:
        df = pd.read_csv(file)
    except FileNotFoundError:
        print("File Doesn't Exist")
    else:
        return df[col_name]

def get_df_from_csv(path,ticker):
    """
    Reads a CSV file containing stock data and returns a dataframe.
    
    Parameters:
    ticker (str): The stock ticker symbol.
    
    Returns:
    pd.DataFrame: The dataframe containing the stock data.
    """
    try:
        df = pd.read_csv(path + ticker + '.csv')
    except FileNotFoundError:
        print("File Doesn't Exist")
    else:
        return df

def download_multiple_stocks(syear, smonth, sday, eyear, emonth, eday, *args):
    """
    Downloads stock data for multiple tickers and saves them to CSV files.
    
    Parameters:
    syear (int): Start year of the period.
    smonth (int): Start month of the period.
    sday (int): Start day of the period.
    eyear (int): End year of the period.
    emonth (int): End month of the period.
    eday (int): End day of the period.
    args (str): Stock ticker symbols.
    """
    for x in args:
        save_to_csv_from_yahoo(x, syear, smonth, sday, eyear, emonth, eday)

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


# Example usage:
# save_to_csv_from_yahoo(PATH, "AAPL")
