# Provides ways to work with large multidimensional arrays
import numpy as np 
# Allows for further data manipulation and analysis
import pandas as pd 
import matplotlib.pyplot as plt # Plotting
import matplotlib.dates as mdates # Styling dates
get_ipython().run_line_magic('matplotlib', 'inline')

import datetime as dt # For defining dates
import time
import os

import yfinance as yf

import cufflinks as cf
import plotly.express as px
import plotly.graph_objects as go

from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)
cf.go_offline()

from plotly.subplots import make_subplots

import warnings
warnings.simplefilter("ignore")


def mplfinance_plot(ticker, chart_type, syear, smonth, sday, eyear, emonth, eday):
    """
    Plots stock data using Matplotlib finance.
    
    Parameters:
    ticker (str): The stock ticker symbol.
    chart_type (str): The type of chart (e.g., 'ohlc', 'candle').
    syear (int): Start year of the period.
    smonth (int): Start month of the period.
    sday (int): Start day of the period.
    eyear (int): End year of the period.
    emonth (int): End month of the period.
    eday (int): End day of the period.
    """
    start = f"{syear}-{smonth}-{sday}"
    end = f"{eyear}-{emonth}-{eday}"
    
    try:
        df = pd.read_csv('/Users/derekbanas/Documents/Tutorials/Python for Finance/' + ticker + '.csv', index_col=0, parse_dates=True)
    except FileNotFoundError:
        print("File Doesn't Exist")
    else:
        df.index = pd.DatetimeIndex(df['Date'])
        df_sub = df.loc[start:end]
        
        mpf.plot(df_sub, type='candle')
        mpf.plot(df_sub, type='line')
        mpf.plot(df_sub, type='ohlc', mav=4)
        
        s = mpf.make_mpf_style(base_mpf_style='charles', rc={'font.size': 8})
        fig = mpf.figure(figsize=(12, 8), style=s)
        ax = fig.add_subplot(2, 1, 1)
        av = fig.add_subplot(2, 1, 2, sharex=ax)
        
        mpf.plot(df_sub, type=chart_type, mav=(3, 5, 7), ax=ax, volume=av, show_nontrading=True)

def plot_return_mult_stocks(investment, stock_df):
    """
    Plots the return of an investment over time using multiple stocks.
    
    Parameters:
    investment (float): The initial investment amount.
    stock_df (pd.DataFrame): The dataframe containing stock data.
    """
    (stock_df / stock_df.iloc[0] * investment).plot(figsize=(15, 6))



def price_plot(ticker, syear, smonth, sday, eyear, emonth, eday):
    """
    Creates a simple price/date plot between specified dates.
    
    Parameters:
    ticker (str): The stock ticker symbol.
    syear (int): Start year of the period.
    smonth (int): Start month of the period.
    sday (int): Start day of the period.
    eyear (int): End year of the period.
    emonth (int): End month of the period.
    eday (int): End day of the period.
    """
    start = f"{syear}-{smonth}-{sday}"
    end = f"{eyear}-{emonth}-{eday}"
    
    try:
        df = pd.read_csv("/Users/derekbanas/Documents/Tutorials/Python for Finance/" + ticker + '.csv')
    except FileNotFoundError:
        print("File Doesn't Exist")
    else:
        df.index = pd.DatetimeIndex(df['Date'])
        df_sub = df.loc[start:end]
        
        df_np = df_sub.to_numpy()
        np_adj_close = df_np[:, 5]
        date_arr = df_np[:, 1]
        
        fig = plt.figure(figsize=(12, 8), dpi=100)
        axes = fig.add_axes([0, 0, 1, 1])
        axes.plot(date_arr, np_adj_close, color='navy')
        axes.xaxis.set_major_locator(plt.MaxNLocator(8))
        axes.grid(True, color='0.6', dashes=(5, 2, 1, 2))
        axes.set_facecolor('#FAEBD7')

def multplot(tickers):
    tickers = ["FB", "AMZN", "AAPL", "NFLX", "GOOG"]

    fig = go.Figure()

    for ticker in tickers:
        df = get_stock_df_from_csv(ticker)
        plot = go.Scatter(x=df.index, y=df['Close'], name=ticker)
        fig.add_trace(plot)

    fig.update_xaxes(title="Date", rangeslider_visible=True)
    fig.update_yaxes(title="Price")
    fig.update_layout(height=1200, width=1800, showlegend=True)

    fig.show()

import plotly.graph_objects as go

def plot_with_boll_bands(ticker):
    """
    Plots stock data with Bollinger Bands using Plotly.
    
    Args:
    - ticker (str): Ticker symbol of the stock (e.g., 'AAPL' for Apple).
    """
    df = get_stock_df_from_csv(f"D:/Python for Finance/Wilshire_Stocks/{ticker}.csv")
    
    if df is None:
        print(f"Failed to retrieve data for {ticker}.")
        return
    
    add_bollinger_bands(df)
    
    fig = go.Figure()
    candlestick = go.Candlestick(x=df.index,
                                 open=df['Open'],
                                 high=df['High'],
                                 low=df['Low'],
                                 close=df['Close'],
                                 name="Candlestick")
    
    upper_band = go.Scatter(x=df.index, y=df['upper_band'], mode='lines',
                            line=dict(color='red', width=1),
                            name='Upper Band')
    lower_band = go.Scatter(x=df.index, y=df['lower_band'], mode='lines',
                            line=dict(color='blue', width=1),
                            name='Lower Band')
    
    fig.add_trace(candlestick)
    fig.add_trace(upper_band)
    fig.add_trace(lower_band)
    
    fig.update_layout(title=f"{ticker} Candlestick Chart with Bollinger Bands",
                      xaxis_title='Date',
                      yaxis_title='Price',
                      showlegend=True)
    
    fig.show()
