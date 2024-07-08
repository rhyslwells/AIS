from src.loading import get_stock_df_from_csv, get_column_from_csv, get_df_from_csv

from src.plotting import plot_with_boll_bands,price_plot
from src.technical import calculate_ema

# Define path to files

# Start date defaults
S_YEAR = 2017
S_MONTH = 1
S_DAY = 3
S_DATE_STR = f"{S_YEAR}-{S_MONTH}-{S_DAY}"
S_DATE_DATETIME = dt.datetime(S_YEAR, S_MONTH, S_DAY)

# End date Today<-- change to today.

E_YEAR = 2021
E_MONTH = 8
E_DAY = 19
E_DATE_STR = f"{E_YEAR}-{E_MONTH}-{E_DAY}"
E_DATE_DATETIME = dt.datetime(E_YEAR, E_MONTH, E_DAY)



data_location='data/'

ticker='COST'

save_to_csv_from_yahoo(data_location, 'AAPL', 2023, 1, 1, 2024, 6, 1)

path_loc=data_location+ticker+'.csv'

close_prices = get_column_from_csv(path_loc, 'Adj Close')

df = get_df_from_csv(path_loc, 'AAPL')



