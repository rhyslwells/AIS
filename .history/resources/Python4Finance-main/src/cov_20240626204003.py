
# Standard deviation

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


