import matplotlib.pyplot as plt
import date_format as date
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
    end_date = date.get_current_date()
    df = __initialize_stock(stock, start_date, end_date)
    df['Close'].plot()
    plt.show()


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


def __initialize_stock(stock, start_date=None, end_date=None):
    if start_date is None:
        start_date = date.get_date_month(6)  # 6 months ago Default
    if end_date is None:
        end_date = date.get_current_date()
    return myAPI.get_data(stock, start_date, end_date)
