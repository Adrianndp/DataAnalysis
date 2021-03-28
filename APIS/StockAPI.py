from pandas_datareader import data
from yahoo_fin import stock_info as si
from Helper.date_format import get_current_date
import requests_html  # important to have for yahoo_fin to work


def get_data(stock_name, start_date, end_date=None, head=None, index_date=False, close=False):
    """
    :param bool close: get only the close values
    :param str stock_name: The symbol of the stock for example AAPL
    :param str start_date: Begin of the data he data
    :param str end_date: End of data. Must be more recent than start_date
    :param int head: if is True then returns the first  5 Rows of the data
    :param bool index_date: if its true DATE will be a column instead of index.
    :return: Data of a stock
    :raises Exception: if data not founded
    """
    if end_date is None:
        end_date = get_current_date()
    try:
        stock_data = data.DataReader(stock_name, 'yahoo', start_date, end_date)
        if close:
            stock_data = stock_data[['Close']]
        if index_date:
            stock_data.reset_index(level=0, inplace=True)
        if head is not None:
            return stock_data.head(90)
        return stock_data
    except Exception as p:
        # print(f'Error during parsing data. Reason: {p}')
        return


def get_current_stock_price(stock_name):
    return si.get_live_price(stock_name)


def get_most_active_stocks():
    # TOO 100
    return si.get_day_most_active()


def get_bigger_gainers():
    # TOO 100
    return si.get_day_gainers()


def get_worst_performers():
    # TOO 100
    return si.get_day_losers()


def get_market_cap(stock_name):
    market_dict = data.get_quote_yahoo(stock_name)['marketCap'].to_dict()
    return market_dict[stock_name]


def get_dividend_share(stock):
    return si.get_dividends(stock)


def get_last_cash_flow(stock):
    return si.get_cash_flow(stock).iloc[:, 0]
