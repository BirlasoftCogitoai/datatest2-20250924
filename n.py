# tests/test_routes.py
import pytest

from app import create_app

@pytest.fixture
def app():
    app = create_app('config.TestingConfig')
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Optimized Navigation' in response.data