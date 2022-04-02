import os
import tempfile

import pytest

from game import create_app
from game.db import init_db


@pytest.fixture
def app():
    """ Create and configure a new app instance for each test. """
    db_fd, db_path = tempfile.mkstemp()
    app = create_app({"TESTING": True, "DATABASE": db_path})

    with app.app_context():
        init_db()

    yield app

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    """A test client for the app. """
    return app.test_client()

@pytest.fixture
def runner(app):
    """ A test runner for the app's Click commands. """
    return app.test_cli_runner()
