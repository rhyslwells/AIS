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
        
# Mixed functions

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
