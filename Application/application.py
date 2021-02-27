from Algorithms.DataAnalizer import __initialize_stock
from Algorithms.MACD import get_SMA
import Helper.date_format as date
from APIS.NewsAPI import get_news
from flask import abort


def df_to_csv(stock, start_date=None, end_date=None):
    dataframe = __initialize_stock(stock, start_date, end_date)
    return dataframe.to_html()


def get_graph_with_sma(stock, start_date=None):
    if stock is None:
        return abort(404, "Not stock was given")
    if start_date is None:
        start_date = date.get_date_month(7)
    end_date = date.get_current_date()
    df = __initialize_stock(stock, start_date, end_date, index_date=True)
    df_with_ema = get_SMA(df, plot=False)
    return df_with_ema.to_json()


def get_news_api(keyword, start_date):
    if keyword is None:
        return abort(404, "Not keyword was given")
    if start_date is None:
        start_date = date.get_date_day(5)
    return get_news(keyword, start_date)

