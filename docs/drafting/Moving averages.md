---
tags:
  - technical_analysis
aliases:
  - MA
  - SMA
  - EMA
type: Technical Indicator
created: 2024-07-02 21:28
---
## Definition

A moving average (MA) is a widely used indicator in technical analysis that helps smooth out price data by creating a constantly updated average price.
## Types/Components

- **Simple Moving Average (SMA)**: An average of a security’s price over a set number of periods.
- **Exponential Moving Average (EMA)**: A type of moving average that gives more weight to recent prices.
## Usage

- Identifying trends in stock prices
- Determining support and resistance levels
- Generating buy and sell signals
## Example

Calculate a 50-day SMA for stock XYZ.

### Code Example

python

Copy code

``` python
	import pandas as pd
	import yfinance as yf
	import matplotlib.pyplot as plt
	
	# Download stock data
	data = yf.download('AAPL', start='2020-01-01', end='2021-01-01')
	
	# Calculate Simple Moving Average (SMA)
	data['SMA_50'] = data['Close'].rolling(window=50).mean()
	
	# Plot the data
	plt.figure(figsize=(14, 7))
	plt.plot(data['Close'], label='Close Price')
	plt.plot(data['SMA_50'], label='50-Day SMA', color='orange')
	plt.title('50-Day Simple Moving Average (SMA)')
	plt.legend()
	plt.show()
```

### References

- Investopedia on Moving Averages
- TradingView Indicators

### Notebook Ideas

- Calculate and plot SMA and EMA for different stocks.
- Compare SMA and EMA to see which provides better signals.
- Analyze the impact of different window sizes on the moving averages.