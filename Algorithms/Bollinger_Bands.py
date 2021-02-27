from Algorithms.DataAnalizer import __initialize_stock
import matplotlib.pyplot as plt

stock = "SPY"
df = __initialize_stock(stock, start_date="2020-07-15")
period = 20
multiplier = 2
# 20-period Simple Moving Average plus 2 times the 20-period rolling standard deviation
df['UpperBand'] = df['Close'].rolling(period).mean() + df['Close'].rolling(period).std() * multiplier
# 20-period Simple Moving Average minus 2 times the 20-period rolling standard deviation
df['LowerBand'] = df['Close'].rolling(period).mean() - df['Close'].rolling(period).std() * multiplier
plt.rcParams['figure.figsize'] = [12, 7]
plt.rc('font', size=14)
plt.plot(df['Close'], label="S&P 500")
plt.plot(df['UpperBand'], label="Upper Bollinger Band")
plt.plot(df['LowerBand'], label="Lower Bollinger Band")
plt.legend()
plt.show()
