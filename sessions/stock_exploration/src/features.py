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
