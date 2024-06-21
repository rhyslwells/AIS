stock = yf.Ticker(ticker)
# Get P/E ratio
pe_ratio = stock.info['forwardPE']
# Get EPS
eps = stock.info['forwardEps']
# Print fundamental metrics
print(f"{ticker} P/E Ratio: {pe_ratio}")
print(f"{ticker} EPS: {eps}")

import matplotlib.pyplot as plt

# Plot Net Income
income_stmt.loc['Net Income'].plot(kind='bar', figsize=(10, 5), title='Net Income')
plt.xlabel('Date')
plt.ylabel('Net Income')
plt.show()

# Plot Total Assets and Total Liabilities
balance_sheet.loc['Total Assets'].plot(kind='bar', figsize=(10, 5), title='Total Assets vs Total Liabilities')
balance_sheet.loc['Total Liab'].plot(kind='bar')
plt.legend(['Total Assets', 'Total Liabilities'])
plt.xlabel('Date')
plt.ylabel('Value')
plt.show()


# consider the stock 

# Current Ratio: Measures the company's ability to pay short-term obligations with its current assets.
# Quick Ratio: Similar to the current ratio but excludes inventory, providing a more stringent measure of liquidity.
# Debt to Equity Ratio: Indicates the proportion of equity and debt used to finance the company's assets.
# Return on Equity (ROE): Measures the profitability relative to shareholders' equity.


# Plotting key metrics over time helps in visualizing the financial trends of the company.

import matplotlib.pyplot as plt

# Plot Net Income
income_stmt.loc['Net Income'].plot(kind='bar', figsize=(10, 5), title='Net Income')
plt.xlabel('Date')
plt.ylabel('Net Income')
plt.show()

# Plot Total Assets and Total Liabilities
balance_sheet.loc['Total Assets'].plot(kind='bar', figsize=(10, 5), title='Total Assets vs Total Liabilities')
balance_sheet.loc['Total Liab'].plot(kind='bar')
plt.legend(['Total Assets', 'Total Liabilities'])
plt.xlabel('Date')
plt.ylabel('Value')
plt.show()
