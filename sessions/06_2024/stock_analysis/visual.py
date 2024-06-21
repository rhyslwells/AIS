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

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

    ax1.plot(df.index, df['Adj Close'], label='Adjusted Close')
    ax1.plot(df.index, df['100ma'], label='100-Day Moving Average')
    ax1.set_title(f'Adjusted Close Price and 100-Day MA of {ticker}')
    ax1.set_ylabel('Price', fontsize=14)
    ax1.legend()
    ax1.grid(which='major')

    ax2.bar(df.index, df['Volume'])
    ax2.set_xlabel('Year', fontsize=14)
    ax2.set_ylabel('Volume', fontsize=14)
    ax2.grid(which='major')

    plt.tight_layout()
    plt.savefig(f'{ticker}_moving_average.png')
    plt.show()

def plot_comparison(goog_close, msft_close):
    style.use('dark_background')
    plt.figure(figsize=(10, 8))

    plt.subplot(2, 1, 1)
    sns.lineplot(x=goog_close.index, y=goog_close['Adj Close'], color='lemonchiffon')
    plt.title('Google Stock Prices: 2017 to Present')

    plt.subplot(2, 1, 2)
    sns.lineplot(x=msft_close.index, y=msft_close['Adj Close'])
    plt.title('Microsoft Stock Prices: 2017 to Present')

    plt.tight_layout()
    plt.savefig('comparison.png')
    plt.show()
