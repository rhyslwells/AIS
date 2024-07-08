import datetime as dt
import pandas as pd
from src.loading import get_column_from_csv, get_df_from_csv, save_to_csv_from_yahoo
from src.plotting import plot_with_boll_bands, price_plot
from src.technical import calculate_ema, plot_candlestick_with_ema

# Define path to files
data_location = 'data/'

# Ticker for Costco
ticker = 'AAL'

# Start and end dates
S_YEAR = 2021
S_MONTH = 1
S_DAY = 1
S_DATE_STR = f"{S_YEAR}-{S_MONTH}-{S_DAY}"
S_DATE_DATETIME = dt.datetime(S_YEAR, S_MONTH, S_DAY)

E_DATE_DATETIME = dt.datetime.today()
E_YEAR = E_DATE_DATETIME.year
E_MONTH = E_DATE_DATETIME.month
E_DAY = E_DATE_DATETIME.day

# Save adjusted close prices to CSV from Yahoo Finance
save_to_csv_from_yahoo(data_location, ticker, S_YEAR, S_MONTH, S_DAY, E_YEAR, E_MONTH, E_DAY)



# Path to the saved CSV file
path_loc = f"{data_location}{ticker}.csv"

# Load adjusted close prices from CSV
df = get_df_from_csv(path_loc)

# Ensure the 'Adj Close' column exists in the DataFrame
if 'Adj Close' not in df.columns:
    raise ValueError(f"'Adj Close' column not found in {path_loc}")

# Plot with Bollinger Bands
plot_with_boll_bands(df, 'Adj Close')

# Plotting price with candlesticks and EMA
plot_candlestick_with_ema(df, 'Adj Close')

# Additional Moving Average Exploration
df['50_MA'] = df['Adj Close'].rolling(window=50).mean()
df['200_MA'] = df['Adj Close'].rolling(window=200).mean()

# Plotting Moving Averages
price_plot(df, ['Adj Close', '50_MA', '200_MA'])
