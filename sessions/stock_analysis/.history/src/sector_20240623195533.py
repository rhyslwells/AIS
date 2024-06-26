# 4. Sector and Industry Analysis:
# Industry Performance: Compare the stock's performance with its industry peers.
# Market Position: Evaluate the company’s market share and competitive advantages.
# Regulatory Environment: Consider potential regulatory changes that could impact the industry

# How to compare with fundementals?



import yfinance as yf

def get_industry(symbol):
    stock = yf.Ticker(symbol)
    return stock.info['industry']

symbol = 'AAPL'
industry = get_industry(symbol)
print(f'The industry of {symbol} is {industry}.')
