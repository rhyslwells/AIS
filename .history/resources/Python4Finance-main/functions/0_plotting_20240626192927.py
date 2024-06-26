

def mplfinance_plot(ticker, chart_type, syear, smonth, sday, eyear, emonth, eday):
    """
    Plots stock data using Matplotlib finance.
    
    Parameters:
    ticker (str): The stock ticker symbol.
    chart_type (str): The type of chart (e.g., 'ohlc', 'candle').
    syear (int): Start year of the period.
    smonth (int): Start month of the period.
    sday (int): Start day of the period.
    eyear (int): End year of the period.
    emonth (int): End month of the period.
    eday (int): End day of the period.
    """
    start = f"{syear}-{smonth}-{sday}"
    end = f"{eyear}-{emonth}-{eday}"
    
    try:
        df = pd.read_csv('/Users/derekbanas/Documents/Tutorials/Python for Finance/' + ticker + '.csv', index_col=0, parse_dates=True)
    except FileNotFoundError:
        print("File Doesn't Exist")
    else:
        df.index = pd.DatetimeIndex(df['Date'])
        df_sub = df.loc[start:end]
        
        mpf.plot(df_sub, type='candle')
        mpf.plot(df_sub, type='line')
        mpf.plot(df_sub, type='ohlc', mav=4)
        
        s = mpf.make_mpf_style(base_mpf_style='charles', rc={'font.size': 8})
        fig = mpf.figure(figsize=(12, 8), style=s)
        ax = fig.add_subplot(2, 1, 1)
        av = fig.add_subplot(2, 1, 2, sharex=ax)
        
        mpf.plot(df_sub, type=chart_type, mav=(3, 5, 7), ax=ax, volume=av, show_nontrading=True)

def plot_return_mult_stocks(investment, stock_df):
    """
    Plots the return of an investment over time using multiple stocks.
    
    Parameters:
    investment (float): The initial investment amount.
    stock_df (pd.DataFrame): The dataframe containing stock data.
    """
    (stock_df / stock_df.iloc[0] * investment).plot(figsize=(15, 6))



def price_plot(ticker, syear, smonth, sday, eyear, emonth, eday):
    """
    Creates a simple price/date plot between specified dates.
    
    Parameters:
    ticker (str): The stock ticker symbol.
    syear (int): Start year of the period.
    smonth (int): Start month of the period.
    sday (int): Start day of the period.
    eyear (int): End year of the period.
    emonth (int): End month of the period.
    eday (int): End day of the period.
    """
    start = f"{syear}-{smonth}-{sday}"
    end = f"{eyear}-{emonth}-{eday}"
    
    try:
        df = pd.read_csv("/Users/derekbanas/Documents/Tutorials/Python for Finance/" + ticker + '.csv')
    except FileNotFoundError:
        print("File Doesn't Exist")
    else:
        df.index = pd.DatetimeIndex(df['Date'])
        df_sub = df.loc[start:end]
        
        df_np = df_sub.to_numpy()
        np_adj_close = df_np[:, 5]
        date_arr = df_np[:, 1]
        
        fig = plt.figure(figsize=(12, 8), dpi=100)
        axes = fig.add_axes([0, 0, 1, 1])
        axes.plot(date_arr, np_adj_close, color='navy')
        axes.xaxis.set_major_locator(plt.MaxNLocator(8))
        axes.grid(True, color='0.6', dashes=(5, 2, 1, 2))
        axes.set_facecolor('#FAEBD7')

