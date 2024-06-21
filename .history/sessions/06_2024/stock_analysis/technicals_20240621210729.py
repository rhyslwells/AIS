import ta
from ta.utils import dropna
from ta.volatility import BollingerBands

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
    fig, ax1 = plt.subplots(figsize=(14, 8))

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
    plt.savefig(f'{ticker}_bollinger_bands.png')
    plt.show()
