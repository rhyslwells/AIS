# Purpose: Produce the images for the main report

import argparse
import datetime
import os
import yfinance as yf
from data_retrieval import get_yahoo_data, get_web_data
from visual import plot_adjusted_close, plot_moving_average, plot_volume
from technicals import add_bollinger_bands, plot_bollinger_bands, calculate_rsi, plot_rsi, calculate_macd, plot_macd
from fundamental import fetch_financial_data, print_fundamental_metrics, plot_net_income, plot_assets_liabilities, calculate_ratios, print_ratios

def main(ticker, start_date):
    end_date = datetime.datetime.now()
    os.makedirs(f'outputs/{ticker}', exist_ok=True)
    os.makedirs(f'outputs/{ticker}/imgs', exist_ok=True)

    # Get data
    tickers = [ticker]
    df_yahoo = get_yahoo_data(tickers, start_date, end_date)
    df = df_yahoo

    # Visuals
    plot_adjusted_close(df, ticker)
    plot_moving_average(df, ticker)
    plot_volume(df, ticker)

    # Technical indicators
    df = add_bollinger_bands(df)
    plot_bollinger_bands(df, ticker)

    df = calculate_rsi(df)
    plot_rsi(df, ticker)

    df = calculate_macd(df)
    plot_macd(df, ticker)

    # Fundamental
    # income_stmt, balance_sheet, cash_flow = fetch_financial_data(ticker)

    # Uncomment and fix the following lines if necessary
    # balance_sheet
    # first_column_terms = balance_sheet.index
    # liabilities_terms = [term for term in first_column_terms if "Liabilities" in term]

    # stock = yf.Ticker(ticker)
    # plot_net_income(income_stmt, ticker)
    # plot_assets_liabilities(balance_sheet, ticker)
    # print_fundamental_metrics(stock, ticker)
    # current_ratio, quick_ratio, debt_to_equity_ratio, return_on_equity = calculate_ratios(balance_sheet, income_stmt)
    # print_ratios(current_ratio, quick_ratio, debt_to_equity_ratio, return_on_equity)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Produce images for the main report.')
    parser.add_argument('ticker', type=str, help='Ticker symbol for the stock')
    parser.add_argument('start_date', type=str, help='Start date for data retrieval (YYYY-MM-DD)')
    args = parser.parse_args()

    main(args.ticker, args.start_date)