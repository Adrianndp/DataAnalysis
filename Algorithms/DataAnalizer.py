import matplotlib.pyplot as plt
from Helper import date_format as date
from sklearn.linear_model import LinearRegression
from APIS import StockAPI as myAPI
import numpy as np
import math


def visualize_close(stock_name, time=None):
    if time == 'year':
        start_date = date.get_date_year(1)
    elif time == 'month':
        start_date = date.get_date_month(1)
    elif time == 'day':
        start_date = date.get_date_day(1)
    else:
        start_date = date.get_date_month(6)
    df = __initialize_stock(stock_name, start_date, close=True)
    __plot([df['Close']], "Close value")


def get_EMA(df, window_size=None, plot=False):
    if window_size is None:
        # 8- and 20-day for day traders while the 50 and 200-day EMA for long term investors.
        window_size = 20
    close = df['Close']
    moving_average_list = df['Close'].rolling(window=window_size).mean()
    if not plot:
        df["Moving average"] = moving_average_list
        return df
    else:
        data_to_plot = [close, moving_average_list]
        __plot(data_to_plot, "EMA")


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


def linear_regression(df, property_to_check=None, plot=False):
    dataframe = df.copy()
    dataframe.reset_index(level=0, inplace=True)
    if property_to_check is None:
        property_to_check = 'Close'
    if property_to_check in dataframe:
        property_index = list(dataframe).index(property_to_check)
    else:
        print("property not in dataset")
        return
    dataframe['ID'] = dataframe.index
    id_index = list(dataframe).index('ID')
    dataframe = dataframe.iloc[:, [id_index, property_index]]
    X = dataframe.iloc[:, 0].values.reshape(-1, 1)
    Y = dataframe.iloc[:, 1].values.reshape(-1, 1)
    linear_regressor = LinearRegression()
    linear_regressor.fit(X, Y)
    Y_pred = linear_regressor.predict(X)
    if plot:
        plt.figure(num="Graph", figsize=(10, 6), dpi=80, facecolor='k', edgecolor='c')
        with plt.style.context('dark_background'):
            plt.scatter(X, Y)
            plt.plot(X, Y_pred, color='white')
        font = {'family': 'arial', 'color': 'white', 'weight': 'normal', 'size': 20}
        plt.title("Linear Regression", fontdict=font)
        plt.show()
    else:
        linear = np.array(Y_pred).reshape(1, len(dataframe.index)).tolist()[0]
        dataframe['Linear'] = linear
        dataframe = dataframe.drop(columns=['ID'])
        return dataframe


def __initialize_stock(stock_name, start_date=None, end_date=None, head=None, index_date=False, close=False):
    if start_date is None:
        start_date = date.get_date_month(6)  # 6 months ago Default
    return myAPI.get_data(stock_name=stock_name, start_date=start_date, end_date=end_date, head=head,
                          index_date=index_date, close=close)


def __plot(columns_to_plot, title):
    """
    :param list columns_to_plot: Columns
    :param str title: Title of the  graph
    """
    plt.figure(num="Graph", figsize=(10, 6), dpi=80, facecolor='k', edgecolor='c')
    with plt.style.context('dark_background'):
        for row in columns_to_plot:
            plt.plot(row)

    indexes = columns_to_plot[0].index.tolist()
    index_list, intersections = get_intersections(columns_to_plot[0].tolist(), columns_to_plot[1].tolist(), indexes)
    plt.plot(index_list, intersections, 'ro')

    font = {'family': 'arial', 'color': 'white', 'weight': 'normal', 'size': 20}
    plt.title(title, fontdict=font)
    plt.show()


def get_intersections(list_a, list_b, indexes):
    """
    :param column of dataframe list_a: intersects list_b
    :param column of dataframe list_b: intersects list_a
    :param index of df indexes:
    :return: x and y coordinates of the points to plot
    """
    list_a = list(map(lambda x: round(x), list_a))
    list_b = list(map(lambda x: round(x) if not math.isnan(x) else x, list_b))
    intersections_and_index = [(list_a[x], x) for x in range(len(list_a)) if list_a[x] == list_b[x]]
    x_values = [indexes[intersections_and_index[i][1]] for i in range(len(intersections_and_index))]
    y_values = [intersections_and_index[i][0] for i in range(len(intersections_and_index))]
    return x_values, y_values
