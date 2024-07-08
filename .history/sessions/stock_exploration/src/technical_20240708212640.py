

import numpy as np  # Provides ways to work with large multidimensional arrays
import pandas as pd  # Allows for further data manipulation and analysis
from pandas_datareader import data as web  # Reads stock data
import datetime as dt  # For defining dates
import time  # For handling sleep/delays
import matplotlib.pyplot as plt  # Plotting
import matplotlib.dates as mdates  # Styling dates
import mplfinance as mpf  # Matplotlib finance
from statsmodels.tsa.ar_model import AutoReg, ar_select_order
import plotly.graph_objects as go
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from ta.trend import MACD
from ta.momentum import StochasticOscillator


def calculate_ema(df, column, spans):
    """
    Calculates the Exponential Moving Average (EMA) for given spans and adds them to the DataFrame.

    Parameters:
    df (pd.DataFrame): DataFrame containing the stock data.
    column (str): The column to calculate the EMA on.
    spans (list): List of spans for which to calculate the EMA.

    Returns:
    pd.DataFrame: DataFrame with added EMA columns.
    """
    for span in spans:
        df[f'EMA{span}'] = df[column].ewm(span=span, adjust=False).mean()
    return df

def plot_candlestick_with_ema(df, title="Stock Data with EMAs"):
    """
    Plots candlestick chart with EMAs.

    Parameters:
    df (pd.DataFrame): DataFrame con
    
    taining the stock data.
    title (str): Title of the plot.

    Returns:
    None
    """
    fig = go.Figure()

    candle = go.Candlestick(x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'], name='Candlestick')
    fig.add_trace(candle)

    for col in df.columns:
        if col.startswith('EMA'):
            fig.add_trace(go.Scatter(x=df.index, y=df[col], line=dict(width=1), name=col))

    fig.update_layout(title=title)
    fig.update_xaxes(rangebreaks=[dict(bounds=["sat", "mon"])])
    fig.show()

def plot_macd_stoch(ticker, time_period, time_int):
    """
    Plots the MACD and Stochastic Oscillator along with the candlestick chart for the given ticker.

    Parameters:
    ticker (str): The stock ticker symbol.
    time_period (str): The period over which to retrieve data.
    time_int (str): The interval between data points.

    Returns:
    None
    """
    stock_df = download_stock_data(ticker, time_period, time_int)
    
    stock_df['MA12'] = stock_df['Adj Close'].ewm(span=12, adjust=False).mean()
    stock_df['MA26'] = stock_df['Adj Close'].ewm(span=26, adjust=False).mean()
    
    macd = MACD(close=stock_df['Close'], window_slow=26, window_fast=12, window_sign=9)
    sto_os = StochasticOscillator(high=stock_df['High'], close=stock_df['Close'], low=stock_df['Low'], window=14, smooth_window=3)
    
    fig = make_subplots(rows=4, cols=1, shared_xaxes=True, vertical_spacing=0.01)
    candle = go.Candlestick(x=stock_df.index, open=stock_df['Open'], high=stock_df['High'], low=stock_df['Low'], close=stock_df['Close'])
    fig.add_trace(candle, row=1, col=1)

    fig.add_trace(go.Scatter(x=stock_df.index, y=macd.macd(), line=dict(color='blue', width=2)), row=2, col=1)
    fig.add_trace(go.Scatter(x=stock_df.index, y=macd.macd_signal(), line=dict(color='orange', width=2)), row=2, col=1)
    fig.add_trace(go.Bar(x=stock_df.index, y=macd.macd_diff()), row=2, col=1)

    fig.add_trace(go.Scatter(x=stock_df.index, y=sto_os.stoch(), line=dict(color='blue', width=2)), row=3, col=1)
    fig.add_trace(go.Scatter(x=stock_df.index, y=sto_os.stoch_signal(), line=dict(color='orange', width=2)), row=3, col=1)
    fig.add_hline(y=20, line_width=1, line_dash="dash", line_color="red", row=3, col=1)
    fig.add_hline(y=80, line_width=1, line_dash="dash", line_color="green", row=3, col=1)

    fig.add_trace(go.Bar(x=stock_df.index, y=stock_df['Volume']), row=4, col=1)

    fig.update_layout(title=ticker)
    fig.update_yaxes(title_text="Price", row=1)


def example():
    # Download stock data
    amd_df = download_stock_data("AMD", "1y", "1d")

    # Calculate EMAs
    amd_df = calculate_ema(amd_df, 'Adj Close', [20, 50])

    # Plot candlestick with EMAs
    plot_candlestick_with_ema(amd_df, title="AMD Stock Data with EMAs")

    # Plot MACD and Stochastic Oscillator
    plot_macd_stoch("PG", "5d", "5m")

import numpy as np

def calculate_rsi(df, close_column='Close', timeperiod=14):
    """
    Calculates the Relative Strength Index (RSI) and adds it to the DataFrame.

    Parameters:
    df (pd.DataFrame): DataFrame containing the stock data.
    close_column (str): The column name of the close prices.
    timeperiod (int): The time period for RSI calculation.

    Returns:
    pd.DataFrame: DataFrame with added 'RSI' column.
    """
    df['RSI'] = ta.RSI(np.array(df[close_column]), timeperiod=timeperiod)
    return df

import plotly.graph_objects as go
from plotly.subplots import make_subplots

def plot_rsi(df, title="Stock Data with RSI"):
    """
    Plots candlestick chart with RSI.

    Parameters:
    df (pd.DataFrame): DataFrame containing the stock data.
    title (str): Title of the plot.

    Returns:
    None
    """
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.01,
                        row_heights=[0.7, 0.3])

    candle = go.Candlestick(x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'], name='Candlestick')
    rsi = go.Scatter(x=df.index, y=df['RSI'], line=dict(color='blue', width=2))

    fig.add_trace(candle, row=1, col=1)
    fig.add_trace(rsi, row=2, col=1)

    # Draw RSI threshold lines
    fig.add_hline(y=30, line_width=1, line_dash="dash", line_color="red", row=2, col=1)
    fig.add_hline(y=70, line_width=1, line_dash="dash", line_color="green", row=2, col=1)

    fig.update_layout(title=title)
    fig.update_layout(height=900, width=1200, showlegend=False, xaxis_rangeslider_visible=False,
                      xaxis_rangebreaks=[dict(bounds=["sat", "mon"]), dict(bounds=[16, 9.5], pattern="hour"),
                                        dict(values=["2021-12-25", "2022-01-01"])])
    fig.show()

def calculate_bollinger_bands(df, window=20):
    """
    Calculates Bollinger Bands (BB) and adds them to the DataFrame.

    Parameters:
    df (pd.DataFrame): DataFrame containing the stock data.
    window (int): The window size for rolling mean and standard deviation.

    Returns:
    pd.DataFrame: DataFrame with added 'BB_Hi' and 'BB_Low' columns.
    """
    df['Mean'] = df['Adj Close'].rolling(window=window).mean()
    df['SD'] = df['Adj Close'].rolling(window=window).std()
    df['BB_Hi'] = df['Mean'] + (2 * df['SD'])
    df['BB_Low'] = df['Mean'] - (2 * df['SD'])
    return df

def plot_bollinger_bands(df, title="Stock Data with Bollinger Bands"):
    """
    Plots candlestick chart with Bollinger Bands.

    Parameters:
    df (pd.DataFrame): DataFrame containing the stock data.
    title (str): Title of the plot.

    Returns:
    None
    """
    fig = go.Figure()

    candle = go.Candlestick(x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Adj Close'], name='Candlestick')
    bb_hi = go.Scatter(x=df.index, y=df['BB_Hi'], line=dict(color='green', width=1), name="BB Hi")
    bb_low = go.Scatter(x=df.index, y=df['BB_Low'], line=dict(color='orange', width=1), name="BB Low")

    fig.add_trace(candle)
    fig.add_trace(bb_hi)
    fig.add_trace(bb_low)

    fig.update_layout(title=title)
    fig.update_xaxes(rangebreaks=[dict(bounds=["sat", "mon"])])
    fig.show()

def example_2():
    # Example usage of the extracted functions

    # Download stock data
    amd_df = download_stock_data("AMD", "3d", "15m")

    # Calculate RSI
    amd_df = calculate_rsi(amd_df)

    # Plot RSI
    plot_rsi(amd_df)

    # Download stock data for Bollinger Bands example
    msft_df = download_stock_data("MSFT", "6mo", "1d")

    # Calculate Bollinger Bands
    msft_df = calculate_bollinger_bands(msft_df)

    # Plot Bollinger Bands
    plot_bollinger_bands(msft_df)
