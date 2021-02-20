import requests
import json

API_KEY = "b1836b964cec4509b16bc96eae9a21c5"
search = "tesla"
start_date = "2021-02-19"
r = requests.get(f'http://newsapi.org/v2/everything?q={search}&from={start_date}&sortBy=publishedAt&apiKey={API_KEY}')
json_data = json.loads(r.text)
status_code = json_data['status']  # ok
results = json_data['totalResults']
# json_data['articles'][0].keys() = ['source', 'author', 'title', 'description', 'url', 'urlToImage', 'publishedAt', 'content']

