from Algorithms.DataAnalizer import *

stock_input = "AAPL"


def test_visualize_close_year(stock):
    visualize_close(stock, 'year')


def test_visualize_close_month(stock):
    visualize_close(stock, 'month')


def test_visualize_close_day(stock):
    visualize_close(stock, 'day')


def test_plot_linear_regression(stock):
    # default last six months
    linear_regression(stock)


def test_plot_moving_average(stock, window_size=None, start_date=None):
    get_EMA(stock, window_size, start_date, plot=True)


def test_get_moving_average(stock, window_size=None, start_date=None):
    return get_EMA(stock, window_size, start_date, plot=False)


def test_plot_RSI(stock, window_size=None, start_date=None):
    get_RSI(stock, window_size=window_size, start_date=start_date, plot=True)


def test_get_RSI(stock, window_size=None, start_date=None):
    return get_RSI(stock, window_size=window_size, start_date=start_date, plot=False)


test_plot_moving_average(stock_input)
