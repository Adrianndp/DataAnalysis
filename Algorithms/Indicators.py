from Algorithms.DataAnalizer import __initialize_stock, __plot
from Helper import date_format as date
import stockstats

stock = "MDB"
start_date = date.get_date_month(6)
df_input = __initialize_stock(stock, start_date=start_date, index_date=True)


def get_EMA(df, window_size=None, plot=False):
    if window_size is None:
        # 8- and 20-day for day traders while the 50 and 200-day EMA for long term investors.
        window_size = 10
    close = df['Close']
    df["EMA"] = df['Close'].ewm(span=window_size, adjust=False).mean()
    if not plot:
        return df
    else:
        data_to_plot = [close, df['EMA']]
        __plot(data_to_plot, "EMA")


def get_MACD(df, plot=False):
    """ Moving Average Convergence Divergence

    This function will initialize all following columns.

    MACD Line (macd): (12-day EMA - 26-day EMA)
    Signal Line (macds): 9-day EMA of MACD Line
    MACD Histogram (macdh): MACD Line - Signal Line

    :param bool plot: if True plot the macd
    :param df: data
    :return: df with macd
    """
    df = stockstats.StockDataFrame(df)
    stock_df = stockstats.StockDataFrame.retype(df)
    df['macd'] = stock_df['macd']
    if plot:
        __plot([df['macd']], "MACD")
    else:
        return df


def get_RSI(df, window_size=None, plot=False):
    # https://www.tradingview.com/support/solutions/43000502338-relative-strength-index-rsi/
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


def get_RSI_with_library(df, plot=False):
    stock_df = stockstats.StockDataFrame.retype(df)
    df['rsi'] = stock_df['rsi_14']
    if plot:
        __plot([df['rsi']], "RSI")
    else:
        return df


def get_bollinger_bands(df, period=None, multiplier=None):
    if multiplier is None:
        multiplier = 2
    if period is None:
        period = 20
    # 20-period Simple Moving Average plus 2 times the 20-period rolling standard deviation
    df['UpperBand'] = df['Close'].rolling(period).mean() + df['Close'].rolling(period).std() * multiplier
    # 20-period Simple Moving Average minus 2 times the 20-period rolling standard deviation
    df['LowerBand'] = df['Close'].rolling(period).mean() - df['Close'].rolling(period).std() * multiplier
    __plot([df['Close'], df['UpperBand'], df['LowerBand']], "Bollinger Bands")
    # plt.plot(df['UpperBand'], label="Upper Bollinger Band")
    # plt.plot(df['LowerBand'], label="Lower Bollinger Band")
