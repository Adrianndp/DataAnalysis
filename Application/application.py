import os
from Algorithms.DataAnalizer import __initialize_stock


def df_to_csv(stock, file_name, start_date=None, end_date=None):
    """
    :param str stock: Stock symbol for example AAPL
    :param file_name: name of file to be created
    :param start_date: format Year-month-day for example: 2021-12-28
    :param end_date: format Year-month-day
    :default the last six months
    """
    dataframe = __initialize_stock(stock, start_date, end_date)
    cwd = f"{os.getcwd()}/{file_name}.csv"
    if not os.path.isfile(cwd):
        dataframe.to_csv(cwd, index=False, header=True)
    else:
        print("File already exists")


def get_close(stock, start_date, end_date):
    df = __initialize_stock(stock, start_date, end_date)
    return df.to_html()
