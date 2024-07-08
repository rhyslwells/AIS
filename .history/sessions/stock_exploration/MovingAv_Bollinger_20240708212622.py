import datetime as dt
import pandas as pd
from src.loading import get_column_from_csv, get_df_from_csv, save_to_csv_from_yahoo
from src.plotting import  price_plot
from src.technical import calculate_ema, plot_candlestick_with_ema
import plotly.graph_objects as go


# Define path to files
data_location = 'data/'

# Ticker for Costco
ticker = 'AMC'

# Start and end dates
S_YEAR = 2021
S_MONTH = 1
S_DAY = 1
S_DATE_STR = f"{S_YEAR}-{S_MONTH}-{S_DAY}"
S_DATE_DATETIME = dt.datetime(S_YEAR, S_MONTH, S_DAY)

# End date set to 1st of July 2024
E_YEAR = 2024
E_MONTH = 7
E_DAY = 1
E_DATE_STR = f"{E_YEAR}-{E_MONTH}-{E_DAY}"
E_DATE_DATETIME = dt.datetime(E_YEAR, E_MONTH, E_DAY)


# Save adjusted close prices to CSV from Yahoo Finance
save_to_csv_from_yahoo(data_location, ticker, S_YEAR, S_MONTH, S_DAY, E_YEAR, E_MONTH, E_DAY)



# Path to the saved CSV file

# Load adjusted close prices from CSV
df = get_df_from_csv(data_location,ticker)
df.head()


######################################################################################


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

calculate_bollinger_bands(df, 20)

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

# Plot with Bollinger Bands
plot_bollinger_bands(df)

df.head()

######################################################################################
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

# Plotting price with candlesticks and EMA
plot_candlestick_with_ema(df, 'Adj Close')

# Additional Moving Average Exploration
df['50_MA'] = df['Adj Close'].rolling(window=50).mean()
df['200_MA'] = df['Adj Close'].rolling(window=200).mean()

# Plotting Moving Averages
price_plot(df, ['Adj Close', '50_MA', '200_MA'])
