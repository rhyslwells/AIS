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

def plot_net_income(income_stmt):
    income_stmt.loc['Net Income'].plot(kind='bar', figsize=(10, 5), title='Net Income')
    plt.xlabel('Date')
    plt.ylabel('Net Income')
    plt.savefig(f'{ticker}/net_income.png')
    plt.show()


def plot_assets_liabilities(balance_sheet):
    fig, ax = plt.subplots(figsize=(10, 5))
    balance_sheet.loc['Total Assets'].plot(kind='bar', ax=ax, label='Total Assets')
    balance_sheet.loc['Total Liab'].plot(kind='bar', ax=ax, label='Total Liabilities', color='red')
    plt.legend()
    plt.title('Total Assets vs Total Liabilities')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.savefig(f'{ticker}/assets_liabilities.png')
    plt.show()


