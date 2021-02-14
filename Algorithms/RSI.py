from DataAnalizer import get_RSI

"""
https://www.tradingview.com/support/solutions/43000502338-relative-strength-index-rsi/
"""

stock = "AAPL"

RSI = get_RSI(stock, plot=True)
