from Algorithms.DataAnalizer import __initialize_stock
from Algorithms.Indicators import get_EMA, get_RSI_with_library
import Helper.date_format as date
from APIS.NewsAPI import get_news
from flask import abort
from APIS.StockAPI import get_bigger_gainers


def df_to_csv(stock, start_date=None, end_date=None):
    dataframe = __initialize_stock(stock, start_date, end_date)
    return dataframe.to_html()


def get_graph_with_indicators(stock, start_date=None):
    if stock is None:
        return abort(404, "Not stock was given")
    if start_date is None:
        start_date = date.get_date_month(4)
    end_date = date.get_current_date()
    df = __initialize_stock(stock, start_date, end_date, index_date=True)
    df = get_EMA(df, plot=False)
    df = get_RSI_with_library(df)
    df.reset_index(level=0, inplace=True)
    upper = ["rsi", "ema"]
    for col in df.columns:
        if col in upper:
            df = df.rename(columns={col: col.upper()})
        else:
            df = df.rename(columns={col: col.capitalize()})
    return df.to_json()


def get_news_api(keyword, start_date):
    if keyword is None:
        return abort(404, "Not keyword was given")
    if start_date is None:
        start_date = date.get_date_day(5)
    return get_news(keyword, start_date)


def get_top_gainers():
    return get_bigger_gainers().to_json


