from DataAnalizer import get_EMA, __initialize_stock
from Helper import date_format as date

stock = "AAPL"
start_date = date.get_date_month(6)
df = __initialize_stock(stock, start_date=start_date)
EMA = get_EMA(df, plot=True)
# print(EMA)


