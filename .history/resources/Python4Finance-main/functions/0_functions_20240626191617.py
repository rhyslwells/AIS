import numpy as np  # Provides ways to work with large multidimensional arrays
import pandas as pd  # Allows for further data manipulation and analysis
from pandas_datareader import data as web  # Reads stock data
import datetime as dt  # For defining dates
import time  # For handling sleep/delays

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
