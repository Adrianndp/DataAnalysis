import pytest
from Application import create_app
import json


@pytest.fixture
def client():
    app = create_app({'TESTING': True, 'HOST': 'http://localhost'})
    with app.test_client() as client:
        yield client


def test_home(client):
    rv = client.get('/')
    assert rv.status_code == 200


def test_graph(client):
    rv = client.get('/graph')
    assert rv.status_code == 200


def test_tops(client):
    rv = client.post('/tops')
    assert rv.status_code == 400
    rv = client.post('/tops', data={"submit_button": 'Show Top GAINERS Today'})
    data = rv.data.decode("utf-8")
    assert "/table?data=" in data  # link to send to /table


def test_table(client):
    rv = client.get('/table')
    assert rv.status_code == 400
    data = {"Symbol": "SWTX", "Name": "SpringWorks Therapeutics, Inc.",
            "Price": "78.22", "Change": "2.28", "change_percentage": 3.0, "Volume": "188911000000000.0",
            "market_cap": "3838000000.0"}
    rv = client.get(f'/table?data={json.dumps([data])}')
    assert rv.status_code == 200


def test_get_graph_api(client):
    rv = client.get('/get_graph_api')
    assert rv.status_code == 404
    rv = client.get('/get_graph_api?stock=AAPL')
    assert rv.status_code == 200
    data = json.loads(rv.data.decode('utf-8'))
    assert "Volume" in data
    assert "EMA" in data
    assert "RSI" in data


def test_get_stats(client):
    rv = client.get('/get_stats')
    assert rv.status_code == 404
    rv = client.get('/get_stats_api?stock=AAPL')
    assert rv.status_code == 200
    data = json.loads(rv.data.decode('utf-8'))
    assert "Last Dividend" in data
    rv = client.get('/get_stats_api?stock=TSLA')
    assert rv.status_code == 200
    data = json.loads(rv.data.decode('utf-8'))
    assert "Last Dividend" not in data
