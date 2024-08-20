'''
    Updates all the stock data in /data/stock_data to the current date.
'''
import yfinance
import pandas
import os


def updateStockTicker(ticker: str):
    