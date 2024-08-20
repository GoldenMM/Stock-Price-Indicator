import yfinance as yf
import pandas as pd
import os


def list_files_in_directory(directory):
    # Get list of all entries in the directory
    entries = os.listdir(directory)
    # Filter out only files
    files = [entry for entry in entries if os.path.isfile(os.path.join(directory, entry))]
    return files


directory_path = 'data/stock_data/'
files = list_files_in_directory(directory_path)
files = [file[:-4] for file in files] # Cut off the .csv


stock_tickers = pd.read_csv('data/stock_tickers.csv', index_col=None)
stock_tickers = stock_tickers.convert_dtypes()

print(stock_tickers.shape)
stock_tickers = stock_tickers[stock_tickers['Ticker'].isin(files)]
stock_tickers.to_csv('data/stock_tickers.csv', index=False)

