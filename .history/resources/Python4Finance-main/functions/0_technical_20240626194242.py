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

import plotly.graph_objects as go

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


import plotly.graph_objects as go
from plotly.subplots import make_subplots
from ta.trend import MACD
from ta.momentum import StochasticOscillator

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
    fig.update_yaxes(title_text="Price", row=1


def example():
    # Download stock data
    amd_df = download_stock_data("AMD", "1y", "1d")

    # Calculate EMAs
    amd_df = calculate_ema(amd_df, 'Adj Close', [20, 50])

    # Plot candlestick with EMAs
    plot_candlestick_with_ema(amd_df, title="AMD Stock Data with EMAs")

    # Plot MACD and Stochastic Oscillator
    plot_macd_stoch("PG", "5d", "5m")
