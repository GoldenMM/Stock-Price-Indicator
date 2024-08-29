'''
One time script to convert datetime to date in the data/stock_data files
TODO: Update this in the buildDataset.py so this doesnt have to run
'''

import pandas as pd
import os
from datetime import date
import datetime
from tqdm import tqdm

def cleanStockDate(ticker: str):
    '''
    Cleans one individual ticker
    '''

    # Read the csv
    data_path = f'data/stock_data/{ticker}.csv'
    df = pd.read_csv(data_path, parse_dates=['Date'])
    # Convert the Date col
    df['Date'] = pd.to_datetime(df['Date'], utc=True).dt.date
    # Save the csv
    df = df[['Date','Open','High','Low','Close','Volume']]
    df.to_csv(data_path, index='Date')

# Get all the tickers
tickers = pd.read_csv('data/stock_tickers.csv', index_col=None)

# Loop through all and clean the dates
# for ticker in tqdm(tickers['Ticker'], desc='Cleaning dates'):
#     print(f'Cleaning {ticker}:')
#     cleanStockDate(ticker)

cleanStockDate('AACG')