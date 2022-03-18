import pytest
from api import create_app
from api.db import db
from flask import session


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({'TESTING': True})
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def test_get_status(client):
    response = client.get('/status')
    print(response.get_data(as_text=True))
    print(response.request)
    assert b'1' in response.data


def test_access_session(client):
    with client:
        response = client.post("/login", data={'username': 'Quinlan', 'password': '5210'})
        print(response.data)

# def test_db_post_model(app):
#     with app.app_context():
#         post = db.session.query(Post).get(1)