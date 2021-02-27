from Algorithms.DataAnalizer import __initialize_stock, __plot
from Helper import date_format as date

stock = "AAPL"
start_date = date.get_date_month(6)
df_input = __initialize_stock(stock, start_date=start_date)


def get_SMA(df, window_size=None, plot=False):
    if window_size is None:
        # 8- and 20-day for day traders while the 50 and 200-day EMA for long term investors.
        window_size = 20
    close = df['Close']
    SMA = df['Close'].rolling(window=window_size).mean()
    if not plot:
        dataframe = df.copy()
        dataframe = dataframe[window_size:]
        dataframe["SMA"] = SMA
        return dataframe
    else:
        data_to_plot = [close, SMA]
        __plot(data_to_plot, "SMA")


def get_EMA(df, window_size=None, plot=False):
    if window_size is None:
        # 8- and 20-day for day traders while the 50 and 200-day EMA for long term investors.
        window_size = 20
    df.drop(df.columns.difference(['Close']), 1, inplace=True)
    EMA = df.ewm(span=window_size, adjust=False).mean()
    df['EMA'] = EMA
    if plot:
        data_to_plot = [df['Close'], df['EMA']]
        __plot(data_to_plot, "EMA")
    else:
        return df


SMA_test = get_SMA(df_input)
print(SMA_test)
EMA_test = get_EMA(df_input)
print(EMA_test)
