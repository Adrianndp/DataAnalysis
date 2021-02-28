from Algorithms.DataAnalizer import linear_regression, __initialize_stock, __plot
import math
from Helper import date_format as date
import pandas_ta as ta

"""
https://www.tradingview.com/support/solutions/43000502338-relative-strength-index-rsi/
"""

stock = "AAPL"
start_date = date.get_date_month(6)
df_input = __initialize_stock(stock, start_date=start_date)


def get_RSI(df, window_size=None, plot=False):
    if window_size is None:
        window_size = 14
    df = df.sort_index()
    adj_close = df['Adj Close']
    delta = adj_close.diff()
    delta = delta[1:]
    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0
    # ta.ema(up, length=20)
    avg_gain = up.ewm(span=window_size).mean()
    avg_loss = down.abs().ewm(span=window_size).mean()
    RS = avg_gain / avg_loss
    RSI = 100.0 - (100.0 / (1.0 + RS))
    df['RSI'] = RSI
    df = df[window_size:]
    if plot:
        __plot([df['RSI']], "RSI")
    else:
        df.drop(df.columns.difference(['Close', 'Adj Close', 'RSI']), 1, inplace=True)
        return df
