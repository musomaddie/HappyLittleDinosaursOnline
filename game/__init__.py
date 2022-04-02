import os

from flask import Flask
from game import db

def create_app(test_config=None):
    """ Create and configure an instance of the Flask application. """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # TODO: update this for production to actually be secret
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path,
                              "happy-little-dinosaur.sqlite")
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)

    return app
