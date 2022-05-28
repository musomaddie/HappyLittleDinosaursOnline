import os

from flask import Flask, render_template
from flask_socketio import SocketIO
from game import game_controller, web_content, db

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

    app.register_blueprint(game_controller.bp)
    app.register_blueprint(web_content.bp)

    return app

if __name__ == "__main__":
    app = create_app()
    socketio = SocketIO(app)
    socketio.run(app)

