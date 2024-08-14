'''Takes the stock_tickers.txt file and extracts the ticker code and company name.
   Most likely to be redundant now it has run once, but may need to be used if the
   NASDAQ listings ever change.'''

import pandas as pd

def normaliseCompanyName(name: str) -> str:
    '''
    Removes excess info from the company name
    '''
    if isinstance(name, str):
        # Remove data after '-' from a company name if it exists
        new_name = name.split('-')[0].strip().replace(',', '')
    else:
        return ''
    return new_name

# Get the needed data from the stock_tickers.txt file
df = pd.read_csv('stock_tickers.txt', delimiter='|')
df2 = df[['Symbol', 'Security Name']].copy()
df2.columns = ['Ticker', 'Company']
df2.dropna()                        # Drop null rows
df2 = df2.convert_dtypes()          # Ensure datatypes are proper

# Normalize the company names and save the data
df2['Company'] = df2['Company'].map(normaliseCompanyName)
df2.to_csv('stock_tickers.csv', index=False)