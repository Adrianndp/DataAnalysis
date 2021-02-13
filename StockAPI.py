from pandas_datareader import data
from yahoo_fin import stock_info as si
import requests_html  # important to have for yahoo_fin to work


def get_data(stock, start_date, end_date, head=False, index_date=False):
    """
    :param str stock: The symbol of the stock for example AAPL
    :param str start_date: Begin of the data he data
    :param str end_date: End of data. Must be more recent than start_date
    :param bool head: if is True then returns the first  5 Rows of the data
    :param bool index_date: if its true DATE will be a column instead of index.
    :return: Data of a stock
    :raises Exception: if data not founded
    """
    try:
        stock_data = data.DataReader(stock, 'yahoo', start_date, end_date)
        if index_date:
            stock_data.reset_index(level=0, inplace=True)
        if head:
            return stock_data.head(5)
        else:
            return stock_data
    except Exception as p:
        print(f'Error during parsing data. Reason: {p}')
        return


def get_current_stock_price(stock):
    return si.get_live_price(stock)


def get_most_active_stocks():
    # TOO 100
    return si.get_day_most_active()


def get_bigger_gainers():
    # TOO 100
    return si.get_day_gainers()


def get_worst_performers():
    # TOO 100
    return si.get_day_losers()


def get_market_cap(stock):
    market_dict = data.get_quote_yahoo(stock)['marketCap'].to_dict()
    return market_dict[stock]


print(get_market_cap("AAPL"))