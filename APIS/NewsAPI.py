import requests
import Helper.date_format as date

API_KEY = "b1836b964cec4509b16bc96eae9a21c5"


def get_news(keyword, start_date=None):
    if start_date is None:
        start_date = date.get_date_day(10)
    request = requests.get(
        f'http://newsapi.org/v2/everything?q={keyword}&from={start_date}&sortBy=publishedAt&apiKey={API_KEY}')
    return request.json()
