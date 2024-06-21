import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import style

def plot_adjusted_close(df, ticker):
    plt.figure(figsize=(8,4))
    df['Adj Close'].plot()
    plt.title(f'Adjusted Close Price of {ticker}')
    plt.ylabel('Price', fontsize=14)
    plt.xlabel('Year', fontsize=14)
    plt.grid(which='major')
    plt.savefig(f'{ticker}_adjusted_close.png')
    plt.show()

def plot_moving_average(df, ticker):
    df["100ma"] = df["Adj Close"].rolling(window=100, min_periods=0).mean()
    df.dropna(inplace=True)

    fig, ax1 = plt.subplots(figsize=(10, 8))

    ax1.plot(df.index, df['Adj Close'], label='Adjusted Close')
    ax1.plot(df.index, df['100ma'], label='100-Day Moving Average')
    ax1.set_title(f'Adjusted Close Price and 100-Day MA of {ticker}')
    ax1.set_ylabel('Price', fontsize=14)
    ax1.legend()
    ax1.grid(which='major')

    plt.tight_layout()
    plt.savefig(f'{ticker}_moving_average.png')
    plt.show()



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
    plt.savefig(f'{ticker}_volume.png')
    plt.show()

