from DataAnalizer import get_RSI, linear_regression, __initialize_stock
import numpy as np
"""
https://www.tradingview.com/support/solutions/43000502338-relative-strength-index-rsi/
"""

stock = "AAPL"
df = __initialize_stock(stock, head=100)
RSI = get_RSI(df)


linear_RSI = linear_regression(RSI[1:], property_to_check="RSI", plot=False)
linear_close = linear_regression(df, plot=False)
