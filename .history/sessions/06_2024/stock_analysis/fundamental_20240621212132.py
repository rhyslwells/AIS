stock = yf.Ticker(ticker)
# Get P/E ratio
pe_ratio = stock.info['forwardPE']
# Get EPS
eps = stock.info['forwardEps']
# Print fundamental metrics
print(f"{ticker} P/E Ratio: {pe_ratio}")
print(f"{ticker} EPS: {eps}")
