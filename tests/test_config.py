from game import create_app


def test_config():
    """ Test create_app without passing the test config. """
    assert not create_app().testing
    assert create_app(test_config={"TESTING": True}).testing
