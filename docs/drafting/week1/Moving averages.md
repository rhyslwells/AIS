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
## Investigation
### References

- [Investopedia on Moving Averages](https://www.investopedia.com/terms/m/movingaverage.asp)

### Notebook Ideas

- Calculate and plot SMA and EMA for different stocks.
- Compare SMA and EMA to see which provides better signals.
- Analyze the impact of different window sizes on the moving averages.
- Provide an example of a death cross and golden cross
- Highlight cases where in a bullish trend or bearish trend.
- EMA versus SMA comparison

## Definition

A moving average (MA) is a widely used indicator in technical analysis that helps smooth out price data by creating a constantly updated average price. This is particularly useful for:

- Visualizing the long-term trend of a stock price.
- Smoothing out short-term fluctuations to identify underlying trends.

By averaging out price data over a specified period, moving averages provide a clearer picture of the general direction in which the price is moving.

## Types/Components

- **Simple Moving Average (SMA)**: This is calculated by averaging the closing prices of a security over a specified number of periods. Each price in the series is given equal weight.
- **Exponential Moving Average (EMA)**: This moving average gives more weight to recent prices, making it more responsive to new information. The EMA is calculated by applying a multiplier to the most recent price data, giving it more significance.

## Usage

Moving averages are used for various purposes in technical analysis:

- **Identifying Trends**: They help determine whether a stock is in an uptrend, downtrend, or sideways trend.
- **Determining Support and Resistance Levels**: Moving averages can act as dynamic support and resistance levels where prices tend to bounce.
- **Generating Buy and Sell Signals**: Crossovers and slopes of moving averages can signal potential buy or sell opportunities.

## What to Look For in Use:

### Moving Averages

1. **50-day Moving Average (50 MA)**: 
   - Short-term trend indicator.
   - More responsive to recent price changes.
   - Can signal shorter-term trends.

2. **100-day Moving Average (100 MA)**:
   - Medium-term trend indicator.
   - Balances sensitivity and stability.
   - Provides a clearer picture of the trend compared to the 50 MA.

3. **200-day Moving Average (200 MA)**:
   - Long-term trend indicator.
   - Less responsive to short-term price movements.
   - Highlights the overarching trend.

### Price Crossing Moving Averages

- **Price Above Moving Average**:
  - Indicates a bullish trend.
  - Suggests the stock is trading above its average price over the specified period.

- **Price Below Moving Average**:
  - Indicates a bearish trend.
  - Suggests the stock is trading below its average price over the specified period.

### Moving Average Crossovers

- **Golden Cross**:
  - Occurs when a shorter-term moving average (e.g., 50 MA) crosses above a longer-term moving average (e.g., 200 MA).
  - Suggests a bullish signal, indicating potential upward momentum.

- **Death Cross**:
  - Occurs when a shorter-term moving average crosses below a longer-term moving average.
  - Suggests a bearish signal, indicating potential downward momentum.


## Example

Calculate a 50-day SMA for stock XYZ.

### Code Example

```python
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

