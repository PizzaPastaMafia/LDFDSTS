import yfinance as yf
import pandas as pd
import yahoo_fin.stock_info as si

tickers = si.tickers_sp500()
si.tickers_sp500(True)
tickers =  ["aapl", "goog", "amzn", "BAC", "BA"]
tickers_data= {}
for ticker in tickers:
    ticker_object = yf.Ticker(ticker)

    #convert info() output from dictionary to dataframe
    temp = pd.DataFrame.from_dict(ticker_object.info, orient="index")
    temp.reset_index(inplace=True)
    temp.columns = ["Attribute", "Recent"]
    
    # add (ticker, dataframe) to main dictionary
    tickers_data[ticker] = temp

print(tickers_data)