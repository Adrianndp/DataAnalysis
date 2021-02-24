from Algorithms.DataAnalizer import __initialize_stock, get_EMA
import Helper.date_format as date


def df_to_csv(stock, start_date=None, end_date=None):
    dataframe = __initialize_stock(stock, start_date, end_date)
    return dataframe.to_html()


def get_graph_with_ema(stock, start_date=None):
    if start_date is None:
        start_date = date.get_date_month(1)
    end_date = date.get_current_date()
    df = __initialize_stock(stock, start_date, end_date, index_date=True)
    df_with_ema = get_EMA(df, plot=False)
    return df_with_ema.to_json()
