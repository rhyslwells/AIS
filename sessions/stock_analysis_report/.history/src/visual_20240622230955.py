import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import style

def plot_adjusted_close(df, ticker):
    """
    Plots the adjusted close price of a stock over time.
    
    Args:
        df (pandas.DataFrame): The DataFrame containing the stock data.
        ticker (str): The ticker symbol of the stock.
    """
    plt.figure(figsize=(10, 5))
    df['Adj Close'].plot()
    plt.title(f'Adjusted Close Price of {ticker}')
    plt.ylabel('Price', fontsize=14)
    plt.xlabel('Date', fontsize=14)
    plt.grid(which='major')
    # plt.savefig(f'{ticker}/imgs/adjusted_close.png')
    # plt.show()
    return plt

def plot_moving_average(df, ticker):
    """
    Plots the adjusted close price and its 100-day moving average of a stock over time.
    
    Args:
        df (pandas.DataFrame): The DataFrame containing the stock data.
        ticker (str): The ticker symbol of the stock.
    """
    df["100ma"] = df["Adj Close"].rolling(window=100, min_periods=0).mean()
    df.dropna(inplace=True)

    plt.figure(figsize=(10, 5))
    plt.plot(df.index, df['Adj Close'], label='Adjusted Close')
    plt.plot(df.index, df['100ma'], label='100-Day Moving Average')
    plt.title(f'Adjusted Close Price and 100-Day MA of {ticker}')
    plt.ylabel('Price', fontsize=14)
    plt.legend()
    plt.grid(which='major')
    plt.tight_layout()
    return plt

def plot_volume(df, ticker):
    """
    Plots the volume of a stock over time.
    
    Args:
        df (pandas.DataFrame): The DataFrame containing the stock data.
        ticker (str): The ticker symbol of the stock.
    """
    plt.figure(figsize=(10, 5))
    plt.bar(df.index, df['Volume'], label='Volume')
    plt.title(f'{ticker} Volume')
    plt.xlabel('Date')
    plt.ylabel('Volume')
    plt.legend()
    plt.grid(True)
    # plt.savefig(f'{ticker}/imgs/volume.png')
    # plt.show()
    return plt
