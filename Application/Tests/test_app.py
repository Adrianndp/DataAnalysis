import requests

res = requests.get('http://localhost:5000/get_graph_api?stock=AAPL')
print('response from server:', res.json())
dictFromServer = res.json()
