import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def fetch_financial_data(ticker):
    stock = yf.Ticker(ticker)
    income_stmt = stock.financials
    balance_sheet = stock.balance_sheet
    cash_flow = stock.cashflow
    return income_stmt, balance_sheet, cash_flow

def print_fundamental_metrics(stock, ticker):
    pe_ratio = stock.info.get('forwardPE', 'N/A')
    eps = stock.info.get('forwardEps', 'N/A')
    print(f"{ticker} P/E Ratio: {pe_ratio}")
    print(f"{ticker} EPS: {eps}")


def calculate_ratios(balance_sheet, income_stmt):
    current_assets = balance_sheet.loc['Total Current Assets']
    current_liabilities = balance_sheet.loc['Total Current Liabilities']
    inventory = balance_sheet.loc['Inventory']
    total_liabilities = balance_sheet.loc['Total Liab']
    total_equity = balance_sheet.loc['Total Stockholder Equity']
    net_income = income_stmt.loc['Net Income']
    
    current_ratio = current_assets / current_liabilities
    quick_ratio = (current_assets - inventory) / current_liabilities
    debt_to_equity_ratio = total_liabilities / total_equity
    return_on_equity = net_income / total_equity
    
    return current_ratio.mean(), quick_ratio.mean(), debt_to_equity_ratio.mean(), return_on_equity.mean()

def print_ratios(current_ratio, quick_ratio, debt_to_equity_ratio, return_on_equity):
    print(f"Current Ratio: {current_ratio:.2f}")
    print(f"Quick Ratio: {quick_ratio:.2f}")
    print(f"Debt to Equity Ratio: {debt_to_equity_ratio:.2f}")
    print(f"Return on Equity (ROE): {return_on_equity:.2f}")

def plot_net_income(income_stmt,ticker):
    income_stmt.loc['Net Income'].reset_index().set_index('Date').rename(columns={'index': 'Date'}).plot(kind='bar', figsize=(10, 5), title='Net Income')
    plt.xlabel('Date')
    plt.ylabel('Net Income')
    plt.xticks(rotation=45)
    plt.xticks(rotation_mode="anchor")
    plt.savefig(f'outputs/{ticker}/imgs/net_income.png')
    plt.show()
    
#TODO fix fundamental metrics

def plot_assets_liabilities(balance_sheet,ticker):
    fig, ax = plt.subplots(figsize=(10, 5))
    balance_sheet.loc['Total Assets'].plot(kind='bar', ax=ax, label='Total Assets')
    balance_sheet.loc['Total Liab'].plot(kind='bar', ax=ax, label='Total Liabilities', color='red')
    plt.legend()
    plt.title('Total Assets vs Total Liabilities')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.savefig(f'outputs/{ticker}/imgs/assets_liabilities.png')
    plt.show()

    # ['Total Liabilities Net Minority Interest',
    # 'Total Non Current Liabilities Net Minority Interest',
    # 'Other Non Current Liabilities',
    # 'Derivative Product Liabilities',
    # 'Non Current Deferred Taxes Liabilities',
    # 'Current Liabilities',
    # 'Other Current Liabilities']

# 1. Fundamental Analysis Indicators:
# Earnings Per Share (EPS): Measure of a company's profitability.
# Price-to-Earnings (P/E) Ratio: Valuation metric to compare the company's current share price to its per-share earnings.
# Dividend Yield: Shows how much a company pays out in dividends each year relative to its stock price.
# Revenue and Profit Margins: Trends in revenue, gross profit, operating profit, and net profit margins.
# Debt-to-Equity Ratio: Indicator of the company's financial leverage.
# Return on Equity (ROE): Measure of financial performance calculated by dividing net income by shareholders' equity.

9. Financial Statements Analysis:
Balance Sheet: Assess the company's financial stability and liquidity.
Income Statement: Evaluate revenue, expenses, and profitability.
Cash Flow Statement: Analyze cash inflows and outflows to understand the company’s cash position and financial health.