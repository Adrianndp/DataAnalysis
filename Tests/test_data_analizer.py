from DataAnalizer import *

stock_input = "AAPL"


def test_visualize_close_year(stock):
    visualize_close(stock, 'year')


def test_visualize_close_month(stock):
    visualize_close(stock, 'month')


def test_visualize_close_day(stock):
    visualize_close(stock, 'day')


def test_linear_regression(stock):
    # default last six months
    linear_regression(stock)


def test_moving_average(stock, window_size=None, start_date=None):
    get_EMA(stock, window_size, start_date, plot=True)


def get_moving_average_df(stock, window_size=None, start_date=None):
    return get_EMA(stock, window_size, start_date, plot=False)


test_visualize_close_year("AAPL")
