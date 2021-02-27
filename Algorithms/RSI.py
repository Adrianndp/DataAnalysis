from Algorithms.DataAnalizer import linear_regression, __initialize_stock, __plot
import math
from Helper import date_format as date

"""
https://www.tradingview.com/support/solutions/43000502338-relative-strength-index-rsi/
"""

stock = "AAPL"
start_date = date.get_date_month(6)
df_input = __initialize_stock(stock, start_date=start_date)


def get_RSI(df, window_size=None, plot=False):
    if window_size is None:
        window_size = 14
    adj_close = df['Adj Close']
    delta = adj_close.diff()
    delta = delta[1:]
    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0
    avg_gain = up.ewm(span=window_size).mean()
    avg_loss = down.abs().ewm(span=window_size).mean()
    RS = avg_gain / avg_loss
    RSI = 100.0 - (100.0 / (1.0 + RS))
    df['RSI'] = RSI
    if plot:
        __plot([df['RSI']], "RSI")
    else:
        df.drop(df.columns.difference(['Close', 'Adj Close', 'RSI']), 1, inplace=True)
        return df


def get_angle_by_2_points(point_a, point_b):
    delta_x = point_b[0] - point_a[0]
    delta_y = point_b[1] - point_a[1]
    return math.degrees(math.atan2(delta_y, delta_x))


def get_linear_list_from_df(dataframe, property_given):
    linear_regression_data = linear_regression(dataframe[1:], property_to_check=property_given, plot=False)
    return linear_regression_data['Linear'].tolist()


RSI_data = get_RSI(df_input)
print(RSI_data)

# RSI_linear_list = get_linear_list_from_df(RSI_data, "RSI")
# close_linear_list = get_linear_list_from_df(df, 'Close')
