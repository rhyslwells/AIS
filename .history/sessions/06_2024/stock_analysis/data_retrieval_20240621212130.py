import yfinance as yf
import pandas_datareader.data as web
import datetime

def get_yahoo_data(tickers, start_date, end_date):
    data = yf.download(tickers, start=start_date, end=end_date)
    data.reset_index(inplace=True)
    data.set_index("Date", inplace=True)
    df.fillna(method='ffill', inplace=True)
    return data

def get_web_data(ticker, start_date, end_date):
    df = web.DataReader(ticker, 'yahoo', start_date, end_date)
    return df
