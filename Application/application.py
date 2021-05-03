from Algorithms.DataAnalizer import __initialize_stock
from Algorithms.Indicators import get_EMA, get_RSI
import Helper.date_format as date
from flask import abort
from APIS.StockAPI import get_bigger_gainers, get_dividend_share, get_market_cap, get_current_stock_price, \
    get_last_cash_flow, get_worst_performers, get_most_active_stocks
import json


def get_graph_with_indicators(stock, start_date=None):
    if stock is None:
        return abort(404, "Not stock was given")
    if start_date is None:
        start_date = date.get_date_month(10)
    end_date = date.get_current_date()
    try:
        df = __initialize_stock(stock, start_date, end_date, index_date=True)
    except:
        return
    if df is None:
        abort(404, f"No data fetched for symbol {stock}")
    df = get_EMA(df, plot=False)
    df = get_RSI(df)
    df.reset_index(level=0, inplace=True)
    upper = ["rsi", "ema"]
    for col in df.columns:
        if col in upper:
            df = df.rename(columns={col: col.upper()})
        else:
            df = df.rename(columns={col: col.capitalize()})
    df.drop(['Rs_14', 'Rsi_14', 'Closepm_14_smma', 'Closepm', 'Closenm_14_smma', 'Closenm',
             'Close_-1_s', 'Close_-1_d'], axis=1, inplace=True)
    df = json.loads(df.to_json())
    df['zoom_range'] = date.get_date_month(4)
    return json.dumps(df)


def get_top(top):
    if top == 'gainers':
        top = get_bigger_gainers()
    elif top == 'losers':
        top = get_worst_performers()
    top['change_percentage'] = top.pop('% Change')
    top['Price'] = top.pop('Price (Intraday)')
    top['market_cap'] = top.pop('Market Cap')
    data = json.loads(top.to_json())
    total = []
    for i in range(len(data['Symbol'])):
        i = str(i)
        data_dict = {'Symbol': data['Symbol'][i], 'Name': data['Name'][i], 'Change': data['Change'][i],
                     'Volume': data['Volume'][i], 'change_percentage': data['change_percentage'][i],
                     'Price': data['Price'][i],
                     'market_cap': data['market_cap'][i]}
        total.append(data_dict)
    return json.dumps(total)


def get_stats(ticker):
    data = {'Price': get_current_stock_price(ticker), 'Market Cap': get_market_cap(ticker)}
    try:
        dividends = get_dividend_share(ticker).to_json()
        dividends = json.loads(dividends)
        data['Last Dividend'] = list(dividends['dividend'].items())[-1]
    except AssertionError:
        pass
    cash_flow = get_last_cash_flow(ticker).to_json()
    cash_flow = json.loads(cash_flow)
    data['Net Income'] = cash_flow['netIncome']
    data['Depreciation'] = cash_flow['depreciation']
    data['Total Cash Flow from Investing activities'] = cash_flow['totalCashflowsFromInvestingActivities']
    return data


def get_dividends(ticker):
    dividends = get_dividend_share(ticker).to_json()
    dividends = json.loads(dividends)
    return dividends['dividend']
