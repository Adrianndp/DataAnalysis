import pytest
from Application.Server import create_app


@pytest.fixture
def client():
    app = create_app({'TESTING': True, 'HOST': 'http://localhost'})
    with app.test_client() as client:
        yield client


def test_home(client):
    rv = client.get('/')
    assert rv.status_code == 200

