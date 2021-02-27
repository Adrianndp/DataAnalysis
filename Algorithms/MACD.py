from Algorithms.DataAnalizer import __initialize_stock, __plot
from Helper import date_format as date

stock = "AAPL"
start_date = date.get_date_month(6)
df_input = __initialize_stock(stock, start_date=start_date)


def get_EMA(df, window_size=None, plot=False):
    if window_size is None:
        # 8- and 20-day for day traders while the 50 and 200-day EMA for long term investors.
        window_size = 20
    close = df['Close']
    moving_average_list = df['Close'].rolling(window=window_size).mean()
    if not plot:
        dataframe = df.copy()
        dataframe = dataframe[window_size:]
        dataframe["EMA"] = moving_average_list
        return dataframe
    else:
        data_to_plot = [close, moving_average_list]
        __plot(data_to_plot, "EMA")


EMA = get_EMA(df_input, plot=False)

print(EMA)
