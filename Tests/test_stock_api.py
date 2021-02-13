from StockAPI import *

stock = "AAPL"


def test_get_data(stock, start_date, end_date):
    return get_data(stock, start_date, end_date)
