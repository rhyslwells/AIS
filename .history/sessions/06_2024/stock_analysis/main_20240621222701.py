import datetime
from data_retrieval import get_yahoo_data, get_web_data
from visual import plot_adjusted_close, plot_moving_average, plot_volume
from technicals import add_bollinger_bands, plot_bollinger_bands, calculate_rsi, plot_rsi, calculate_macd, plot_macd
from fundamental import fetch_financial_data, print_fundamental_metrics, plot_net_income, plot_assets_liabilities, calculate_ratios, print_ratios
import yfinance as yf
import os


ticker = "VEOEY"
tickers = [ticker]
start_date = "2023-01-01"
end_date = datetime.datetime.now()

# create a folder called by the ticker
os.makedirs(ticker, exist_ok=True)

# # Get data
# df_yahoo = get_yahoo_data(tickers, start_date, end_date)
# # df_web_google = get_web_data("GOOGL", start_date, end_date)
# df=df_yahoo

# # visuals
# plot_adjusted_close(df, ticker)
# plot_moving_average(df, ticker)
# plot_volume(df, ticker)

# #technical indicators
# df = add_bollinger_bands(df)
# plot_bollinger_bands(df, ticker)

# df = calculate_rsi(df)
# plot_rsi(df, ticker)

# df = calculate_macd(df)
# plot_macd(df, ticker)

#fundamental
income_stmt, balance_sheet, cash_flow = fetch_financial_data(ticker)

# needs to be fixed wrt above.

# balance_sheet
# first_column_terms = balance_sheet.index
# first_column_terms
# get all terms of first_column_terms that contains Liabilities
# liabilities_terms = [term for term in first_column_terms if "Liabilities" in term]
# liabilities_terms


# stock=yf.Ticker(ticker)
# plot_net_income(income_stmt, ticker)
# # plot_assets_liabilities(balance_sheet, ticker)

# print_fundamental_metrics(stock, ticker)
# current_ratio, quick_ratio, debt_to_equity_ratio, return_on_equity = calculate_ratios(balance_sheet, income_stmt)
# print_ratios(current_ratio, quick_ratio, debt_to_equity_ratio, return_on_equity)
