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
    plt=plot_adjusted_close(df, ticker)
    plt.savefig(f'outputs/{ticker}/imgs/adjusted_close.png')
    # plt.show()

    plt=plot_moving_average(df, ticker)
    plt.savefig(f'outputs/{ticker}/imgs/moving_average.png')
    plt.show()

    plt=plot_volume(df, ticker)
    plt.savefig(f'outputs/{ticker}/imgs/volume.png')
    plt.show()



    # # Technical indicators
    df = add_bollinger_bands(df)
    plt=plot_bollinger_bands(df, ticker)
    plt.savefig(f'outputs/{ticker}/bollinger_bands.png')
    plt.show()

    df = calculate_rsi(df)
    plt=plot_rsi(df, ticker)
    plt.savefig(f'outputs/{ticker}/imgs/rsi.png')
    plt.show()

    df = calculate_macd(df)
    plt=plot_macd(df, ticker)
    plt.savefig(f'outputs/{ticker}/imgs/macd.png')
    plt.show()

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
