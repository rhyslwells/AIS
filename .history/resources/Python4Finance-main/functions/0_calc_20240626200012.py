
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