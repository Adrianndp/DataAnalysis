import pytest
from Application import create_app


@pytest.fixture
def client():
    app = create_app({'TESTING': True, 'HOST': 'http://localhost'})
    with app.test_client() as client:
        yield client
