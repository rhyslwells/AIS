import yfinance as yf
ticker = yf.Ticker('GOOGL').info
marketPrice = ticker['regularMarketPrice']
previousClosePrice = ticker['regularMarketPreviousClose']
print('Ticker Value: GOOGL')
print('Market Price Value:', marketPrice)
print('Previous Close Price Value:', previousClosePrice)