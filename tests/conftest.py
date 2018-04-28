from pytest import fixture

from config.app import create_app


@fixture
def app():
  yield create_app({
    "TESTING": True,
  })

@fixture
def client(app):
  return app.test_client()