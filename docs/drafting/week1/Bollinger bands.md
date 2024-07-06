---
tags:
  - technical_analysis
aliases:
  - BB
type: Technical Indicator
created: 2024-07-02 21:28
---
## Definition

Bollinger Bands are a type of statistical chart characterizing the prices and volatility over time of a financial instrument, using a formulaic method consisting of a [[Moving averages]] and two standard deviations.

## Components

- **Middle Band**: A simple moving average (usually 20 periods).
- **Upper Band**: The middle band plus two standard deviations.
- **Lower Band**: The middle band minus two standard deviations.

## Usage

- Identifying overbought and oversold conditions
- Detecting volatility
- Generating buy and sell signals

## Example

Calculate Bollinger Bands for stock XYZ.

### Code Example

python

Copy code
```python
	import pandas as pd
	import yfinance as yf
	import matplotlib.pyplot as plt
	
	# Download stock data
	data = yf.download('AAPL', start='2020-01-01', end='2021-01-01')
	
	# Calculate Bollinger Bands
	data['SMA_20'] = data['Close'].rolling(window=20).mean()
	data['STD_20'] = data['Close'].rolling(window=20).std()
	data['Upper Band'] = data['SMA_20'] + (data['STD_20'] * 2)
	data['Lower Band'] = data['SMA_20'] - (data['STD_20'] * 2)
	
	# Plot the data
	plt.figure(figsize=(14, 7))
	plt.plot(data['Close'], label='Close Price')
	plt.plot(data['SMA_20'], label='20-Day SMA', color='orange')
	plt.plot(data['Upper Band'], label='Upper Bollinger Band', color='green')
	plt.plot(data['Lower Band'], label='Lower Bollinger Band', color='red')
	plt.fill_between(data.index, data['Upper Band'], data['Lower Band'], color='gray', alpha=0.1)
	plt.title('Bollinger Bands')
	plt.legend()
	plt.show()

```


### References

- Investopedia on Bollinger Bands

### Notebook Ideas

- Calculate and plot Bollinger Bands for different stocks.
- Analyze how the width of the bands changes with volatility.
- Develop a trading strategy based on Bollinger Bands signals.