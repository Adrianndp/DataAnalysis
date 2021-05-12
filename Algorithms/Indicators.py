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


def get_RSI(df, plot=False):
    stock_df = stockstats.StockDataFrame.retype(df)
    df['rsi'] = stock_df['rsi_14']
    if plot:
        __plot([df['rsi']], "RSI")
    else:
        return df
