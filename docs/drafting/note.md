# Notes

- [ ] start tech 8

### ipynb 6

Need a list of stocks and sectors information and a way to search them.
Ticker,Company,Sector
Daily return for ticker using adjusted close.

For a portfolio merge into a single df with rows being dates and columns being the adjusted close.

project ROI for a series of tickers
order descending

### ipynb 7
portfolio percentage follwoing sharpe ratio and markowitz optimisation

### ipynb 8

Portfolio total return 
How is the portfolio weighted.
number of shares, share price at time,

What weighting should i have for my portfolio?

### ipynb 9

beta - relation of investment and market
capital assest pricing model
alpha


### ipynb 10

Forcasting: methods

AutoRegressive Integrated Moving Average (ARIMA) is the basis for many other models. It focuses on trying to fit the data as well as possible by examining differences between values instead of the values themselves.

ARIMA works very well when data values have a clear trend and seasonality. We can only make predictions based on the data we have. Any outside effects not in the data can't be used to make predictions. For example we could make predictions on stock prices, but since we don't know when a recession may occur that event can't be modeled.

There is a seasonal (SARIMA) and a non-seasonal ARIMA. There is also SARIMAX which focuses on exogenous, or external factors. It differs from ARIMA in that it has a set of parameters (P, D, and Q) that focus on seasonality.

AR (Autoregressions) refers to a model that regresses based on prior values.

### technical 2

expo moving average:
A EMA allows you to see the big picture when analyzing a stock. Unlike the Simple Moving Average it reduces the lag by putting more emphasis on recent price data.


The MACD helps us to see buy & sell signals. It shows the difference between 2 moving averages.

While these signals are derived from moving averages they occur much more quickly then with moving averages. It is important to know that since the signals occur earlier that they are also more risky.

When the signal line crosses the MACD line moving upwards this is bullish and vice versa. The slope of the angle tells you how strong the trend is.

More interesting macd <---- replace whats in techincals.py

### technicals 3

The RSI is used to determine if a security is overbought or oversold. With them you can take advantage of potential changes in trend. The 2 most commonly used oscillators are the RSI and Stochastic RSI.

The RSI focuses on the deviation of upward and downward averages with values between 0 and 100. The RSI normally uses 9, 14 or 25 sessions which means it is used mainly as a short term analysis tool. A 14 session period is the most commonly used. When used with 9 sessions 0 to 20 is oversold and 80 to 100 is overbought. With 14 values over 70 are considered overbought and those below 30 oversold. When using 25 over 65 are considered overbought and those below 35 oversold.

This indicator is most commonly used with other indicators.

### technical 4

Cumulative returns of a selection of stocks.

### technical 6

add columns to a df for a stock moving averate, returns...volumes

### tech 7

cumulative return ascending for a portfolio/sector



### To be cleaned

---

Ticker info application  
  
Stock analysis Readme  
Initial assement, other tools exist for more specific information. These reports are for initual assement of a stock.  
  
Future AIS ideas  
  
Can get csv with (for a given exchange):  
Ticker,Name,Description,Mrkt Cap,Sector  
  
For a ticker can pull csv for dates.  
  
---  
interactive visuals with plotly (for comparision of stock prices) :  
C:\Users\RhysL\Desktop\AIS\resources\Python4Finance-main\Numpy_Pandas.ipynb  
  
ipynb on blog of stock interactive. For visuals mostly  
---  
How to measure stock performance against peers? it should be a comparision of the rate of change in price. (daily return)  
C:\Users\RhysL\Desktop\AIS\resources\Python4Finance-main\Python for Finance 1.ipynb  
# It is hard to compare stocks by standard deviation when their stock prices  
# are so different. The coefficient of variation is the ratio between the  
# standard deviation and the mean and it provides a comparable standard deviation  
# We get it by dividing the standard deviation by the mean cov = std / mean  
# We see here that GOOG has the least amount of variability  
  
[ ] Image for report, need user to enter peers. Modify ipynb first.then productionise.  
  
Need markdown description, newpage  
  
  
---  
resources\Python4Finance-main\Python for Finance 2.ipynb  
## Get Stock Return over Time Period & Coefficient of Variation  
add_daily_return_to_df  
get_roi_defined_time  
get_cov  
  
What is ROI and coefficent of variation.  
How to visualise these. so we can add them to the report  
comparision with peers?  
  
---  
resources\Python4Finance-main\Python for Finance 3.ipynb  
get ROI and var coefficent between dates, do this for a list of tickers can then order the resulting dataframe Ticker,COV,ROI  
  
Corrolation matrix?  
# Correlation tells us how closely 2 stocks returns move together  
# Correlation is a standardized value lying between -1 and 1  
# When this value is greater that .5 we say that these stocks are strongly correlated  
# Of course each stocks price is perfectly correlated with itself  
  
# We focus on the correlation of returns because investors care about returns  
  
---  
Get top tickers By ROI for a sector.  
Alternatives for a ticker?  
resources\Python4Finance-main\Python for Finance 4.ipynb  
  
How risky is my portfolio? with reasoning  
  
---  
Stock report - to buy or not to buy  
Portfolio report -  
Stock finder report - sector best performers  
---  
Portfolio report :  
whats allocation to have for best Roi  
Allocation for reduction in risk?  
How diversified is the portfolio?