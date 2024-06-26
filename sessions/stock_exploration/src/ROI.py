# ROI

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
