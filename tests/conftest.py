import pytest
from app import create_app


@pytest.fixture
def app():
    app = create_app()
    app.config["TESTING"] = True
    return app


@pytest.fixture
def client(app):
    client = app.test_client()
    with client.session_transaction() as sess:
        sess["username"] = "admin"
    return client
