import yfinance as yf
import ta
import pandas as pd
import numpy as np

df = yf.download('AAPL', start='2015-01-01', end='2021-12-31')  

df.Close = df['Adj Close']

def applyindicators(df):
    df['SMA_200'] = df.Close.rolling(200).mean()
    df['SMA_20'] = df.Close.rolling(20).mean()
    df['stddev'] = df.Close.rolling(20).std()
    df['Upper'] = df.SMA_20 + 2.5 * df.stddev
    df['Lower'] = df.SMA_20 - 2.5 * df.stddev
    df['rsi'] = ta.momentum.rsi(df.Close, 2)

applyindicators(df)

#df.tail(250)[['Close', 'SMA_20', 'Upper', 'Lower']].plot()

def conditions(df):
    df['Buy'] = np.where((df.Close > df.SMA_200) & (df.Close < df.Lower) & (0.97 * df.Close >= df.Low.shift(-1)), 1, 0)  

    df['Sell'] = np.where((df.rsi > 50), 1, 0)

    df['BuyPrice'] = 0.97 * df.Close
    df['SellPrice'] = df.Open.shift(-1) 

conditions(df)

def matchtrades(df):
    Buy_Sells = df[(df.Buy == 1) | (df.Sell == 1)]
    matched_Buy_Sells  = Buy_Sells[(Buy_Sells.Buy.diff() == 1) | (Buy_Sells.Sell.diff() == 1)]
    return matched_Buy_Sells

trades = matchtrades(df)

profit = (trades.SellPrice.shift(-1) - trades.BuyPrice) / trades.BuyPrice
profit = profit[::2]
print(profit)
