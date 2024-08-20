'''
One time script to convert datetime to date in the data/stock_data files
TODO: Update this in the buildDataset.py so this doesnt have to run
'''

import pandas as pd
import os
from datetime import date
import datetime


def cleanStockDate(ticker: str):
    '''
    Cleans one individual ticker
    '''

    # Read the csv
    data_path = f'data/stock_data/{ticker}.csv'
    df = pd.read_csv(data_path, index_col=None, parse_dates=['Date'])


cleanStockDate('')