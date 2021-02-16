from DataAnalizer import get_RSI, linear_regression, __initialize_stock
import math
import numpy as np

"""
https://www.tradingview.com/support/solutions/43000502338-relative-strength-index-rsi/
"""

stock = "AAPL"
df = __initialize_stock(stock, start_date="2019-01-01")


def get_angle_by_2_points(point_a, point_b):
    delta_x = point_b[0] - point_a[0]
    delta_y = point_b[1] - point_a[1]
    return math.degrees(math.atan2(delta_y, delta_x))


RSI_data = get_RSI(df)
linear_regression_RSI = linear_regression(RSI_data[1:], property_to_check="RSI", plot=False)
linear_regression_close = linear_regression(df, plot=False)
RSI_linear = linear_regression_RSI['Linear'].tolist()
close_linear = linear_regression_close['Linear'].tolist()
degree_of_close_line = get_angle_by_2_points((0, close_linear[0]), (len(close_linear), close_linear[-1]))
degree_of_RSI_line = get_angle_by_2_points((0, RSI_linear[0]), (len(RSI_linear), RSI_linear[-1]))

