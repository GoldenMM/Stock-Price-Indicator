'''
    Updates all the stock data in /data/stock_data to the current date. This script would run
    daily, but it verbose enough to update from last date entry.
'''
import yfinance as yf
import pandas as pd
import os
from datetime import date, timedelta
import datetime
from tqdm import tqdm


def updateStockTicker(ticker: str):
    '''
    This will update an individual stockdata.csv file from the ticker
    '''
    today = date.today()

    # Get the current dataframe for the ticker
    data_path = f'data/stock_data/{ticker}.csv'
    df = pd.read_csv(data_path, index_col=0, parse_dates=['Date'])

    df['Date'] = pd.to_datetime(df['Date'], utc=True).dt.date

    last_entry = df.iloc[-1].iat[0]
    yesterday = today - timedelta(days=1)
    
    # Check if it needs updating. If not do nothing
    if (yesterday == last_entry):
        print(f'{ticker}.csv is up to date.')
        return 
    
    print(f'{ticker}.csv is not up to date.')
    # Get the tickets to date from last entry
    recent = yf.Ticker(ticker).history(start=last_entry + timedelta(days=1), end = today)
    recent_clean = recent[['Open', 'High', 'Low', 'Close', 'Volume']].copy()
    recent_clean = recent_clean.reset_index()
    recent_clean['Date'] =  pd.to_datetime(recent_clean['Date']).dt.date
    
    # Concat the two dataframes
    updated_df = pd.concat([df, recent_clean])
    updated_df = updated_df.reset_index(drop=True)
    
    # Save the .csv
    updated_df.to_csv(data_path)
 
# Run it for all stocks

# Get all the tickers
tickers = pd.read_csv('data/stock_tickers.csv', index_col=None)

# Loop through all and clean the dates
for ticker in tqdm(tickers['Ticker'], desc='Updating stock data...'):
    print(f'Updating {ticker}:')
    updateStockTicker(ticker)



