from Algorithms.DataAnalizer import __initialize_stock, __plot
import stockstats


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


def get_RSI(df, plot=False):
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
