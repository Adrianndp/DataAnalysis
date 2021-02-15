from StockAPI import *

stock_input = "AAPL"
dummy_start_date = "2019-10-10"


def test_get_data(stock, start_date, end_date=None):
    return get_data(stock, start_date, end_date)


def test_get_current_stock_price(stock):
    return get_current_stock_price(stock)


def test_get_most_active_stocks():
    return get_most_active_stocks()


def test_get_bigger_gainers():
    return get_bigger_gainers()


def test_get_worst_performers():
    return get_worst_performers()


def test_get_market_cap(stock):
    return get_market_cap(stock)