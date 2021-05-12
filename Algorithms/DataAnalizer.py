import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from Application import api as myAPI, date_format as date
import numpy as np


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


def linear_regression(df, property_to_check=None, plot=False):
    dataframe = df.copy()
    dataframe.reset_index(level=0, inplace=True)
    if property_to_check is None:
        property_to_check = 'Close'
    if property_to_check in dataframe:
        property_index = list(dataframe).index(property_to_check)
    else:
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
    font = {'family': 'arial', 'color': 'white', 'weight': 'normal', 'size': 20}
    plt.title(title, fontdict=font)
    plt.show()
