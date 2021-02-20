from Algorithms.DataAnalizer import get_RSI, linear_regression, __initialize_stock
import math
from Helper import date_format as date

"""
https://www.tradingview.com/support/solutions/43000502338-relative-strength-index-rsi/
"""

stock = "AAPL"
start_date = date.get_date_month(6)
df = __initialize_stock(stock, start_date=start_date)


def get_angle_by_2_points(point_a, point_b):
    delta_x = point_b[0] - point_a[0]
    delta_y = point_b[1] - point_a[1]
    return math.degrees(math.atan2(delta_y, delta_x))


def get_linear_list_from_df(dataframe, property_given):
    linear_regression_data = linear_regression(dataframe[1:], property_to_check=property_given, plot=False)
    return linear_regression_data['Linear'].tolist()


RSI_data = get_RSI(df)

RSI_linear_list = get_linear_list_from_df(RSI_data, "RSI")
close_linear_list = get_linear_list_from_df(df, 'Close')


degree_of_close_line = get_angle_by_2_points((0, close_linear_list[0]), (len(close_linear_list), close_linear_list[-1]))
print(degree_of_close_line)


