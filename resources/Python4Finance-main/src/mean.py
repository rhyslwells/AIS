# Mean


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

