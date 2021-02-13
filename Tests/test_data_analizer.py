from DataAnalizer import *

stock_input = "MSFT"


def test_visualize_close_year(stock):
    visualize_close(stock, 'year')


def test_visualize_close_month(stock):
    visualize_close(stock, 'month')


def test_visualize_close_day(stock):
    visualize_close(stock, 'day')


def test_linear_regression(stock):
    # default last six months
    linear_regression(stock)


test_linear_regression(stock_input)
