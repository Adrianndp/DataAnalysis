from Algorithms.DataAnalizer import __initialize_stock, __plot
from Helper import date_format as date
import stockstats

stock = "AAPL"
start_date = date.get_date_month(6)
df_input = __initialize_stock(stock, start_date=start_date)


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
    :param plot:
    :param df: data
    :return: None
    """
    df = stockstats.StockDataFrame(df)
    stock_df = stockstats.StockDataFrame.retype(df)
    df['macd'] = stock_df['macd']
    if plot:
        __plot([df['macd']], "MACD")
    else:
        return df['macd']