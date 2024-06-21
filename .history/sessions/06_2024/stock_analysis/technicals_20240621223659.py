import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from ta.utils import dropna
from ta.volatility import BollingerBands
from ta.momentum import RSIIndicator
from ta.trend import MACD

def add_bollinger_bands(df):
    df = dropna(df)

    indicator_bb = BollingerBands(close=df["Close"], window=20, window_dev=2)

    df['bb_bbm'] = indicator_bb.bollinger_mavg()
    df['bb_bbh'] = indicator_bb.bollinger_hband()
    df['bb_bbl'] = indicator_bb.bollinger_lband()
    df['bb_bbhi'] = indicator_bb.bollinger_hband_indicator()
    df['bb_bbli'] = indicator_bb.bollinger_lband_indicator()
    df['bb_bbw'] = indicator_bb.bollinger_wband()
    df['bb_bbp'] = indicator_bb.bollinger_pband()

    return df

def plot_bollinger_bands(df, ticker):
    fig, ax1 = plt.subplots(figsize=(10, 5))

    ax1.plot(df.index, df['Adj Close'], label='Adjusted Close')
    ax1.plot(df.index, df['bb_bbm'], label='BB Middle Band')
    ax1.plot(df.index, df['bb_bbh'], label='BB High Band')
    ax1.plot(df.index, df['bb_bbl'], label='BB Low Band')

    ax1.set_title(f'Bollinger Bands for {ticker}')
    ax1.set_ylabel('Price', fontsize=14)
    ax1.set_xlabel('Year', fontsize=14)
    ax1.legend()
    ax1.grid(which='major')

    plt.tight_layout()
    plt.savefig(f'{ticker}/bollinger_bands.png')
    plt.show()

def calculate_rsi(df):
    rsi_indicator = RSIIndicator(close=df['Adj Close'], window=14)
    df['RSI'] = rsi_indicator.rsi()
    return df

def plot_rsi(df, ticker):
    plt.figure(figsize=(10, 5))
    plt.plot(df['RSI'], label='RSI')
    plt.axhline(70, linestyle='--', alpha=0.5, color='red')
    plt.axhline(30, linestyle='--', alpha=0.5, color='green')
    plt.title(f'{ticker} Relative Strength Index (RSI)')
    plt.xlabel('Date')
    plt.ylabel('RSI')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'{ticker}/rsi.png')
    plt.show()

def calculate_macd(df):
    macd_indicator = MACD(close=df['Adj Close'])
    df['MACD'] = macd_indicator.macd()
    df['MACD_Signal'] = macd_indicator.macd_signal()
    df['MACD_Diff'] = macd_indicator.macd_diff()
    return df

def plot_macd(df, ticker):
    plt.figure(figsize=(10, 5))
    plt.plot(df['MACD'], label='MACD')
    plt.plot(df['MACD_Signal'], label='MACD Signal')
    plt.bar(df.index, df['MACD_Diff'], label='MACD Diff', color='gray')
    plt.title(f'{ticker} MACD')
    plt.xlabel('Date')
    plt.ylabel('MACD')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'{ticker}/macd.png')
    plt.show()