import matplotlib.pyplot as plt
from Helper import date_format as date
from sklearn.linear_model import LinearRegression
import StockAPI as myAPI


def visualize_close(stock, time=None):
    if time == 'year':
        start_date = date.get_date_year(1)
    elif time == 'month':
        start_date = date.get_date_month(1)
    elif time == 'day':
        start_date = date.get_date_day(1)
    else:
        start_date = date.get_date_month(6)
    df = __initialize_stock(stock, start_date, close=True)
    __plot([df['Close']], "Close value")


def moving_average(stock, window_size=None, start_date=None, data=False):
    if window_size is None:
        """
        The 8- and 20-day EMA tend to be the most popular time frames for day traders 
        while the 50 and 200-day EMA are better suited for long term investors.
        """
        window_size = 20
    if start_date is None:
        start_date = date.get_date_year(1)

    df = __initialize_stock(stock=stock, start_date=start_date, close=True)
    close = df['Close']
    moving_average_list = df['Close'].rolling(window=window_size).mean()
    if data:
        df["Moving average"] = moving_average_list
        return df
    else:
        data_to_plot = [close, moving_average_list]
        __plot(data_to_plot, "Moving average")


def linear_regression(stock, property_to_check=None, start_date=None, end_date=None):
    df = __initialize_stock(stock, start_date, end_date)
    if df is None:
        print("Dataset is empty")
        return
    dataframe = df.copy()
    dataframe.reset_index(level=0, inplace=True)
    if property_to_check is None and 'Close' in dataframe:
        property_to_check = 'Close'
    else:
        print('Close value is not in dataframe')
        return
    if property_to_check in dataframe:
        property_index = list(dataframe).index('Close')
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
    plt.scatter(X, Y)
    plt.plot(X, Y_pred, color='red')
    plt.show()


def __initialize_stock(stock, start_date=None, end_date=None, head=False, index_date=False, close=False):
    if start_date is None:
        start_date = date.get_date_month(6)  # 6 months ago Default
    return myAPI.get_data(stock=stock, start_date=start_date, end_date=end_date, head=head,
                          index_date=index_date, close=close)


def __plot(rows_to_plot, name):
    plt.figure(num="Graph", figsize=(10, 6), dpi=80, facecolor='k', edgecolor='c')
    with plt.style.context('dark_background'):
        for row in rows_to_plot:
            plt.plot(row)
    font = {'family': 'arial', 'color': 'white', 'weight': 'normal', 'size': 20}
    plt.title(name, fontdict=font)
    plt.show()
