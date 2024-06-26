from functions.download_data import save_to_csv_from_yahoo
from functions.load_data import get_stock_df_from_csv, get_column_from_csv, get_df_from_csv



# Define path to files
path = "D:/Python for Finance/Stocks/"

# Start date defaults
S_YEAR = 2017
S_MONTH = 1
S_DAY = 3
S_DATE_STR = f"{S_YEAR}-{S_MONTH}-{S_DAY}"
S_DATE_DATETIME = dt.datetime(S_YEAR, S_MONTH, S_DAY)

# End date defaults
E_YEAR = 2021
E_MONTH = 8
E_DAY = 19
E_DATE_STR = f"{E_YEAR}-{E_MONTH}-{E_DAY}"
E_DATE_DATETIME = dt.datetime(E_YEAR, E_MONTH, E_DAY)

# Get stock file names in a list
files = [x for x in listdir(path) if isfile(join(path, x))]
tickers = [os.path.splitext(x)[0] for x in files]

# Create a dataframe from our list
stock_df = pd.DataFrame(tickers, columns=['Ticker'])


save_to_csv_from_yahoo('/path/to/folder/', 'AAPL', 2023, 1, 1, 2024, 6, 1)

df = get_stock_df_from_csv('/path/to/folder/', 'AAPL')

close_prices = get_column_from_csv('/path/to/file.csv', 'Adj Close')

df = get_df_from_csv('/path/to/folder/', 'AAPL')

download_multiple_stocks(2023, 1, 1, 2024, 6, 1, 'AAPL', 'MSFT', 'GOOGL')



