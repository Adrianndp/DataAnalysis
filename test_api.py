from Application.api import *
import Application.date_format as date


def test_get_data():
    api_data = get_data("AAPL", date.get_date_month(4))
    assert api_data is not None
    assert "Close" in api_data.to_json()


def test_most_actives():
    most_actives = get_most_active_stocks()
    assert "Symbol" in most_actives.to_json()


def test_get_bigger_gainers():
    gainers = get_bigger_gainers()
    assert "Symbol" in gainers.to_json()


def test_get_worst_performers():
    worst_performers = get_worst_performers()
    assert "Symbol" in worst_performers.to_json()


def test_get_market_cap():
    aapl_market_cap = get_market_cap("AAPL")
    assert "Symbol" in aapl_market_cap.to_json()


def test_get_dividend_share():
    dividend = get_dividend_share("AAPL")
    assert "Symbol" in dividend.to_json()


def test_get_last_cash_flow():
    cash_flow = get_last_cash_flow("AAPL")
    assert "Symbol" in cash_flow.to_json()


def test_get_current_price():
    api_price = get_current_stock_price("AAPL")
    assert "Symbol" in api_price.to_json()
