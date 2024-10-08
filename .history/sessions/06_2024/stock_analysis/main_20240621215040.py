import datetime
from data_retrieval import get_yahoo_data, get_web_data
from visual import plot_adjusted_close, plot_moving_average, plot_comparison
from technicals import add_bollinger_bands, plot_bollinger_bands, calculate_rsi, plot_rsi, calculate_macd, plot_macd
from fundamental import fetch_financial_data, print_fundamental_metrics, plot_net_income, plot_assets_liabilities, calculate_ratios, print_ratios
import yfinance as yf

ticker = "VEOEY"
tickers = [ticker]
start_date = "2023-01-01"
end_date = datetime.datetime.now()

# Get data
df_yahoo = get_yahoo_data(tickers, start_date, end_date)
# df_web_google = get_web_data("GOOGL", start_date, end_date)

df=df_yahoo

# Add indicators and plot
df = add_bollinger_bands(df)
plot_bollinger_bands(df, ticker)

df = calculate_rsi(df)
plot_rsi(df, ticker)

df = calculate_macd(df)
plot_macd(df, ticker)


income_stmt, balance_sheet, cash_flow = fetch_financial_data(ticker)

stock=yf.Ticker(ticker)
print_fundamental_metrics(stock, ticker)
plot_net_income(income_stmt)
plot_assets_liabilities(balance_sheet)

current_ratio, quick_ratio, debt_to_equity_ratio, return_on_equity = calculate_ratios(balance_sheet, income_stmt)
print_ratios(current_ratio, quick_ratio, debt_to_equity_ratio, return_on_equity)



# # Plot data
# plot_adjusted_close(df_yahoo, ticker)
# plot_moving_average(df_yahoo, ticker)

# # comparison
# df_web_microsoft = get_web_data("MSFT", start_date, end_date)
# plot_comparison(df_web_google, df_web_microsoft)

# # Technical indicators
# df_bbands = add_bollinger_bands(df_yahoo)
# plot_bollinger_bands(df_bbands, ticker)
