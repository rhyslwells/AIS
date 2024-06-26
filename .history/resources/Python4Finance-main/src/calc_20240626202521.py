import numpy as np  # Provides ways to work with large multidimensional arrays
import pandas as pd  # Allows for further data manipulation and analysis
from pandas_datareader import data as web  # Reads stock data
import datetime as dt  # For defining dates
import time  # For handling sleep/delays
import matplotlib.pyplot as plt  # Plotting
import matplotlib.dates as mdates  # Styling dates
import mplfinance as mpf  # Matplotlib finance
from statsmodels.tsa.ar_model import AutoReg, ar_select_order



def get_stock_mean_sd(stock_df, ticker):
    """
    Calculates the mean and standard deviation for a specific stock.
    
    Parameters:
    stock_df (pd.DataFrame): The dataframe containing stock data.
    ticker (str): The stock ticker symbol.
    
    Returns:
    tuple: The mean and standard deviation of the stock.
    """
    return stock_df[ticker].mean(), stock_df[ticker].std()

def get_mult_stock_mean_sd(stock_df):
    """
    Calculates and prints the mean, standard deviation, and coefficient of variation
    for multiple stocks.
    
    Parameters:
    stock_df (pd.DataFrame): The dataframe containing stock data for multiple stocks.
    """
    for stock in stock_df:
        mean, sd = get_stock_mean_sd(stock_df, stock)
        cov = sd / mean
        print("Stock: {:4} Mean: {:7.2f} Standard deviation: {:2.2f}".format(stock, mean, sd))
        print("Coefficient of Variation: {}\n".format(cov))


def add_daily_return_to_df(df, ticker):
    """
    Adds a daily return column to the dataframe.
    
    Parameters:
    df (pd.DataFrame): The dataframe containing stock data.
    ticker (str): The stock ticker symbol.
    
    Returns:
    pd.DataFrame: The dataframe with an added daily return column.
    """
    df['daily_return'] = (df['Adj Close'] / df['Adj Close'].shift(1)) - 1
    df.to_csv("/Users/derekbanas/Documents/Tutorials/Python for Finance/" + ticker + '.csv')
    return df  

def add_cum_return_to_df(df, ticker):
    df['cum_return'] = (1 + df['daily_return']).cumprod()
    df.to_csv(PATH + ticker + '.csv')
    return df

def get_cum_ret_for_stocks(stock_df):
    tickers = []
    cum_rets = []

    for index, row in stock_df.iterrows():
        df = get_stock_df_from_csv(row['Ticker'])
        if df is None:
            pass
        else:
            tickers.append(row['Ticker'])
            cum = df['cum_return'].iloc[-1]
            cum_rets.append(cum)
    return pd.DataFrame({'Ticker':tickers, 'CUM_RET':cum_rets})

def sectors():
    indus_df = sec_df.loc[sec_df['Sector'] == "Industrial"]
    health_df = sec_df.loc[sec_df['Sector'] == "Healthcare"]
    it_df = sec_df.loc[sec_df['Sector'] == "Information Technology"]
    comm_df = sec_df.loc[sec_df['Sector'] == "Communication"]
    staple_df = sec_df.loc[sec_df['Sector'] == "Staples"]
    discretion_df = sec_df.loc[sec_df['Sector'] == "Discretionary"]
    utility_df = sec_df.loc[sec_df['Sector'] == "Utilities"]
    financial_df = sec_df.loc[sec_df['Sector'] == "Financials"]
    material_df = sec_df.loc[sec_df['Sector'] == "Materials"]
    restate_df = sec_df.loc[sec_df['Sector'] == "Real Estate"]
    energy_df = sec_df.loc[sec_df['Sector'] == "Energy"]

    industrial = get_cum_ret_for_stocks(indus_df)
    health_care = get_cum_ret_for_stocks(health_df)
    it = get_cum_ret_for_stocks(it_df)
    commun = get_cum_ret_for_stocks(comm_df)
    staple = get_cum_ret_for_stocks(staple_df)
    discretion = get_cum_ret_for_stocks(discretion_df)
    utility = get_cum_ret_for_stocks(utility_df)
    finance = get_cum_ret_for_stocks(financial_df)
    material = get_cum_ret_for_stocks(material_df)
    restate = get_cum_ret_for_stocks(restate_df)
    energy = get_cum_ret_for_stocks(energy_df)

# Function to get stock price on a specific date
def get_stock_price_on_date(ticker, date):
    df = get_df_from_csv(ticker)
    df = df.set_index(['Date'])
    return df.loc[date, 'Adj Close']

# Function to calculate portfolio weight
def get_port_weight(price, total):
    return price / total

# Function to calculate diversifiable risk
def calc_diversifiable_risk(df, tickers, weights):
    # Gets number of days
    days = len(df.index)
    # Calculate covariance of portfolio
    port_covar = np.dot(weights.T, np.dot(df.cov() * days, weights)) 
    
    i = 0
    while i < len(tickers):
        wt_sq = weights[i] ** 2
        stk_var = df[tickers[i]].var() * days
        wt_var = wt_sq * stk_var
        port_covar = port_covar - wt_var
        i += 1
    return port_covar

def calc_projected_roi(ticker):
    a_df = get_df_from_csv(PATH, ticker) 

    a_df = a_df.asfreq('d') # Change frequency to day
    a_df.index # Check frequency
    a_df = a_df.fillna(method='ffill') # Fill missing values

    # Delete unnamed column
    a_df.drop(a_df.columns[a_df.columns.str.contains('unnamed',case = False)],
          axis = 1, inplace = True)

    # Delete daily return column
    a_df = a_df.drop(['daily_return'], axis=1)
    
    # Figure out optimum lags which will be 1 or 2 for this data set
    lags = ar_select_order(a_df, maxlag=30)

    # Create our model using whole data set
    model = AutoReg(a_df['Adj Close'], lags.ar_lags)
    model_fit = model.fit()

    # Define training and testing area
    print("Length :",len(a_df)) # 1712 observations
    train_df = a_df.iloc[50:1369] # 80% minus 1st 50
    test_df = a_df.iloc[1369:] # Last 20%

    # Define training model for 500 days (Play with Number & Test)
    # and White's covariance estimator
    train_model = AutoReg(a_df['Adj Close'], 500).fit(cov_type="HC0")

    # Define start and end for prediction 
    start = len(train_df)
    end = len(train_df) + len(test_df) - 1

    prediction = train_model.predict(start=start, end=end, dynamic=True)

    # Predict 160 days into the future
    forecast = train_model.predict(start=end, end=end+60, dynamic=True)

    # Get starting price of prediction
    s_price = forecast.head(1).iloc[0]

    # Get the last price of prediction
    e_price = forecast.iloc[-1]

    # Get return over prediction
    return (e_price - s_price) / s_price


def get_proj_rois():
    # Will hold all tickers & stock rois
    ticker = []
    roi = []
    
    for x in tickers:
        print("Working on :", x)
        try:
            the_roi = calc_projected_roi(x)
        except Exception as ex:
            print("Stock Data Corrupted")
        else:
            ticker.append(x)
            print("ROI :", the_roi)
            roi.append(the_roi)
        
    return pd.DataFrame({'Ticker':ticker, 'ROI':roi})


def find_beta(ticker):
    # Tickers analyzed being the S&P and the stock passed
    port_list =['GSPC']
    port_list.append(ticker)

    mult_df = merge_df_by_column_name('daily_return',  '2018-01-02', 
                                  '2021-09-10', *port_list)
    
    # Provides the covariance between the securities
    cov = mult_df.cov() * 252
    
    # Get the covariance of the stock and the market
    cov_vs_market = cov.iloc[0,1]
    
    # Get annualized variance of the S&P
    sp_var = mult_df['GSPC'].var() * 252
    
    # Beta is normally calculated over a 5 year period which is why you may see a difference
    beta = cov_vs_market / sp_var
    return beta

def get_port_daily_return(sdate, edate, shares, tickers):
    # Merge all daily prices for all stocks into 1 dataframe
    mult_df = merge_df_by_column_name('Adj Close',  sdate, 
                                  edate, *port_list)
    
    # Get the number of stocks in portfolio
    num_cols = len(mult_df.columns)
    
    # Multiply each stock column by the number of shares
    i = 0
    while i < num_cols:
        mult_df[tickers[i]] = mult_df[tickers[i]].apply(lambda x: x * shares[i])
        i += 1
        
    # Create a new column with the sums of all stocks named Total
    mult_df['Total'] = mult_df.iloc[:, 0:num_cols].sum(axis=1)
    
    # Add column for portfolio daily return
    mult_df['daily_return'] = (mult_df['Total'] / mult_df['Total'].shift(1)) - 1
    
    return mult_df



def get_roi_defined_time(df):
    """
    Calculates the return on investment over a specified time period.
    
    Parameters:
    df (pd.DataFrame): The dataframe containing stock data.
    
    Returns:
    float: The return on investment over the specified period.
    """
    df['Date'] = pd.to_datetime(df['Date'])
    start_val = df[df['Date'] == S_DATE_STR]['Adj Close'][0]
    end_val = df[df['Date'] == E_DATE_STR]['Adj Close'].item()
    
    roi = (end_val - start_val) / start_val
    return roi

def get_cov(stock_df):
    """
    Calculates the coefficient of variation for the stock data.
    
    Parameters:
    stock_df (pd.DataFrame): The dataframe containing stock data.
    
    Returns:
    float: The coefficient of variation.
    """
    mean = stock_df['Adj Close'].mean()
    sd = stock_df['Adj Close'].std()
    cov = sd / mean
    return cov

def get_valid_dates(df, sdate, edate):
    """
    Receives a start and end date and returns the first valid date in that range.
    
    Parameters:
    df (pd.DataFrame): The dataframe containing stock data.
    sdate (str): The start date in 'YYYY-MM-DD' format.
    edate (str): The end date in 'YYYY-MM-DD' format.
    
    Returns:
    tuple: The earliest and latest valid dates within the specified range.
    """
    try:
        mask = (df['Date'] > sdate) & (df['Date'] <= edate) 
        sm_df = df.loc[mask]
        sm_df = sm_df.set_index(['Date'])
    
        sm_date = sm_df.index.min()
        last_date = sm_df.index.max()
    
        date_leading = '-'.join(('0' if len(x)<2 else '')+x for x in sm_date.split('-'))
        date_ending = '-'.join(('0' if len(x)<2 else '')+x for x in last_date.split('-'))
        print(date_leading, " ", date_ending)
    except Exception:
        print("Date Corrupted")
    else:
        return date_leading, date_ending

def roi_between_dates(df, sdate, edate):
    """
    Calculates the return on investment (ROI) between two dates.
    
    Parameters:
    df (pd.DataFrame): The dataframe containing stock data.
    sdate (str): The start date in 'YYYY-MM-DD' format.
    edate (str): The end date in 'YYYY-MM-DD' format.
    
    Returns:
    float: The ROI between the specified dates.
    """
    try:
        start_val = df.loc[sdate,'Adj Close'] 
        end_val = df.loc[edate,'Adj Close']
        roi = ((end_val - start_val) / start_val)
    except Exception:
        print("Data Corrupted")
    else:
        return roi

def get_mean_between_dates(df, sdate, edate):
    """
    Calculates the mean adjusted close price between two dates.
    
    Parameters:
    df (pd.DataFrame): The dataframe containing stock data.
    sdate (str): The start date in 'YYYY-MM-DD' format.
    edate (str): The end date in 'YYYY-MM-DD' format.
    
    Returns:
    float: The mean adjusted close price.
    """
    mask = (df['Date'] > sdate) & (df['Date'] <= edate)
    return df.loc[mask]["Adj Close"].mean()

def get_sd_between_dates(df, sdate, edate):
    """
    Calculates the standard deviation of the adjusted close price between two dates.
    
    Parameters:
    df (pd.DataFrame): The dataframe containing stock data.
    sdate (str): The start date in 'YYYY-MM-DD' format.
    edate (str): The end date in 'YYYY-MM-DD' format.
    
    Returns:
    float: The standard deviation of the adjusted close price.
    """
    mask = (df['Date'] > sdate) & (df['Date'] <= edate)
    return df.loc[mask]["Adj Close"].std()

def get_cov_between_dates(df, sdate, edate):
    """
    Calculates the coefficient of variation of the adjusted close price between two dates.
    
    Parameters:
    df (pd.DataFrame): The dataframe containing stock data.
    sdate (str): The start date in 'YYYY-MM-DD' format.
    edate (str): The end date in 'YYYY-MM-DD' format.
    
    Returns:
    float: The coefficient of variation of the adjusted close price.
    """
    mean = get_mean_between_dates(df, sdate, edate)
    sd = get_sd_between_dates(df, sdate, edate)
    return sd / mean

def get_cov_ror(tickers, sdate, edate):
    """
    Calculates the coefficient of variation (COV) and return on investment (ROI) for all stocks over a defined period.
    
    Parameters:
    tickers (list): The list of stock ticker symbols.
    sdate (str): The start date in 'YYYY-MM-DD' format.
    edate (str): The end date in 'YYYY-MM-DD' format.
    
    Returns:
    pd.DataFrame: A dataframe containing the ticker, COV, and ROI for each stock.
    """
    col_names = ["Ticker", "COV", "ROI"]
    df = pd.DataFrame(columns = col_names)
    
    for ticker in tickers:
        print("Working on :", ticker)
        s_df = get_df_from_csv(ticker)
    
        sdate2, edate2 = get_valid_dates(s_df, sdate, edate)
    
        cov = get_cov_between_dates(s_df, sdate2, edate2)
    
        s_df = s_df.set_index(['Date'])
        roi = roi_between_dates(s_df, sdate2, edate2)

        df.loc[len(df.index)] = [ticker, cov, roi]
    
    return df


def get_return_defined_time(df, syear, smonth, sday, eyear, emonth, eday):
    """
    Calculates the total return over a specified time period.
    
    Parameters:
    df (pd.DataFrame): The dataframe containing stock data.
    syear (int): Start year of the period.
    smonth (int): Start month of the period.
    sday (int): Start day of the period.
    eyear (int): End year of the period.
    emonth (int): End month of the period.
    eday (int): End day of the period.
    
    Returns:
    float: The total return over the specified period.
    """
    start = f"{syear}-{smonth}-{sday}"
    end = f"{eyear}-{emonth}-{eday}"
    df['Date'] = pd.to_datetime(df['Date'])
    
    mask = (df['Date'] >= start) & (df['Date'] <= end)
    daily_ret = df.loc[mask]['daily_return'].mean()
    days = df.loc[mask].shape[0]

    return (days * daily_ret)

