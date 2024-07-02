import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from ta.utils import dropna
from ta.volatility import BollingerBands
from ta.momentum import RSIIndicator
from ta.trend import MACD

def add_bollinger_bands(df):
    """
    Calculates Bollinger Bands indicators and adds them to the DataFrame.
    
    Args:
        df (pandas.DataFrame): The DataFrame containing the stock data.
        
    Returns:
        pandas.DataFrame: Updated DataFrame with Bollinger Bands indicators.
    """
    df = dropna(df)  # Drop rows with NaN values

    # Calculate Bollinger Bands
    indicator_bb = BollingerBands(close=df["Close"], window=20, window_dev=2)
    df['bb_bbm'] = indicator_bb.bollinger_mavg()          # Bollinger Middle Band
    df['bb_bbh'] = indicator_bb.bollinger_hband()         # Bollinger High Band
    df['bb_bbl'] = indicator_bb.bollinger_lband()         # Bollinger Low Band
    df['bb_bbhi'] = indicator_bb.bollinger_hband_indicator()  # Bollinger High Band Indicator
    df['bb_bbli'] = indicator_bb.bollinger_lband_indicator()  # Bollinger Low Band Indicator
    df['bb_bbw'] = indicator_bb.bollinger_wband()         # Bollinger Band Width
    df['bb_bbp'] = indicator_bb.bollinger_pband()         # Bollinger Band %B
    
    return df

def plot_bollinger_bands(df, ticker):
    """
    Plots Bollinger Bands for a stock over time.
    
    Args:
        df (pandas.DataFrame): The DataFrame containing the stock data with Bollinger Bands.
        ticker (str): The ticker symbol of the stock.
    """
    fig, ax1 = plt.subplots(figsize=(10, 5))

    ax1.plot(df.index, df['Adj Close'], label='Adjusted Close')
    ax1.plot(df.index, df['bb_bbm'], label='BB Middle Band')
    ax1.plot(df.index, df['bb_bbh'], label='BB High Band')
    ax1.plot(df.index, df['bb_bbl'], label='BB Low Band')

    ax1.set_title(f'Bollinger Bands for {ticker}')
    ax1.set_ylabel('Price', fontsize=14)
    ax1.set_xlabel('Date', fontsize=14)
    ax1.legend()
    ax1.grid(which='major')

    plt.tight_layout()
    return plt
    # plt.savefig(f'{ticker}/bollinger_bands.png')
    # plt.show()

def calculate_rsi(df):
    """
    Calculates the Relative Strength Index (RSI) indicator and adds it to the DataFrame.
    
    Args:
        df (pandas.DataFrame): The DataFrame containing the stock data.
        
    Returns:
        pandas.DataFrame: Updated DataFrame with RSI values.
    """
    rsi_indicator = RSIIndicator(close=df['Adj Close'], window=14)
    df['RSI'] = rsi_indicator.rsi()
    return df

def plot_rsi(df, ticker):
    """
    Plots the Relative Strength Index (RSI) of a stock over time.
    
    Args:
        df (pandas.DataFrame): The DataFrame containing the stock data with RSI values.
        ticker (str): The ticker symbol of the stock.
    """
    plt.figure(figsize=(10, 5))
    plt.plot(df['RSI'], label='RSI')
    plt.axhline(70, linestyle='--', alpha=0.5, color='red')
    plt.axhline(30, linestyle='--', alpha=0.5, color='green')
    plt.title(f'{ticker} Relative Strength Index (RSI)')
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('RSI', fontsize=14)
    plt.legend()
    plt.grid(True)
    # plt.savefig(f'{ticker}/rsi.png')
    # plt.show()
    return plt

def calculate_macd(df):
    """
    Calculates the Moving Average Convergence Divergence (MACD) indicators and adds them to the DataFrame.
    
    Args:
        df (pandas.DataFrame): The DataFrame containing the stock data.
        
    Returns:
        pandas.DataFrame: Updated DataFrame with MACD values.
    """
    macd_indicator = MACD(close=df['Adj Close'])
    df['MACD'] = macd_indicator.macd()          # MACD Line
    df['MACD_Signal'] = macd_indicator.macd_signal()  # Signal Line
    df['MACD_Diff'] = macd_indicator.macd_diff()      # MACD Histogram
    return df

def plot_macd(df, ticker):
    """
    Plots the Moving Average Convergence Divergence (MACD) of a stock over time.
    
    Args:
        df (pandas.DataFrame): The DataFrame containing the stock data with MACD values.
        ticker (str): The ticker symbol of the stock.
    """
    plt.figure(figsize=(10, 5))
    plt.plot(df['MACD'], label='MACD')
    plt.plot(df['MACD_Signal'], label='MACD Signal')
    plt.bar(df.index, df['MACD_Diff'], label='MACD Diff', color='gray')
    plt.title(f'{ticker} MACD')
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('MACD', fontsize=14)
    plt.legend()
    plt.grid(True)
    return plt
    # plt.savefig(f'{ticker}/macd.png')
    # plt.show()
