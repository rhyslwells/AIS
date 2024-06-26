
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
