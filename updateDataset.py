'''
    Updates all the stock data in /data/stock_data to the current date. This script would run
    daily, but it verbose enough to update from last date entry.
'''
import yfinance as yf
import pandas as pd
import os
from datetime import date
import datetime


def updateStockTicker(ticker: str):
    '''
    This will update an individual stockdata.csv file from the ticker
    '''
    # today = date.today()
    today = datetime.datetime.fromisoformat('2024-08-13 00:00:00-04:00')
    
    # Get the current dataframe for the ticker
    data_path = f'data/stock_data/{ticker}.csv'
    df = pd.read_csv(data_path, index_col=None, parse_dates=['Date'])

    print(df.dtypes)
    print(df.iloc[-1].iat[0])
    print(df['Date'].dtype)
    print(today)

    if (today == df.iloc[-1].iat[0].date):
        print(f'{ticker}.csv is up to date.')
    else:
        print(f'{ticker}.csv is not up to date.')



