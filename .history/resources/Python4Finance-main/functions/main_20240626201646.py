



save_to_csv_from_yahoo('/path/to/folder/', 'AAPL', 2023, 1, 1, 2024, 6, 1)

df = get_stock_df_from_csv('/path/to/folder/', 'AAPL')

close_prices = get_column_from_csv('/path/to/file.csv', 'Adj Close')

df = get_df_from_csv('/path/to/folder/', 'AAPL')

download_multiple_stocks(2023, 1, 1, 2024, 6, 1, 'AAPL', 'MSFT', 'GOOGL')
