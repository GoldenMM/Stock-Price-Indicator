import yfinance as yf
import pandas as pd

apple_stock = yf.Ticker("AAPL").history(period="1mo")

print(apple_stock.head())
print(apple_stock.shape)