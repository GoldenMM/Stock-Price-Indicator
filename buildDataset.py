'''
Purpose of this script is to build the initial dataset of stock data.
This is not to be confused with the updateDataset.py script which is used to update the dataset
based on mising days
'''

import yfinance as yf
import pandas as pd
from tqdm import tqdm

def getHistoricFromTicker(ticker: str) -> pd.DataFrame:
    '''
    Returns cleaned data from yfinance request. We will be using a period of 5 years to
    keep the dataset manageable.
    '''
    df = yf.Ticker(ticker).history(period='5y') # Get the data
    df2 = df[['Open', 'High', 'Low', 'Close', 'Volume']].copy() #only get the rows we want
    if (df2.shape[0] == 0):
        raise ValueError(f"No data found for ticker {ticker} in the specified range")
    return df2


# Pull in the stock tickers
tickers = pd.read_csv('data/stock_tickers.csv')
print(tickers.head())

# Iterate over each ticker and save the historical data to CSV files
for ticker in tqdm(tickers['Ticker'], desc='Processing tickers'):
    try:
        df = getHistoricFromTicker(ticker)
        df.to_csv(f'data/stock_data/{ticker}.csv', index=True)
        print(f"Saved data for {ticker}")
    except Exception as e:
        print(f"Failed to save data for {ticker}: {e}")
        continue