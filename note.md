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


### ipynb 9

beta - relation of investment and market
capital assest pricing model
alpha

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