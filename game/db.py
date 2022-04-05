import click
import csv
import sqlite3

from flask import current_app, g
from flask.cli import with_appcontext

CONTENTS_FN = "game/static/db_content/"

def _get_file_contents(filename):
    with open(f"{CONTENTS_FN}{filename}.tsv") as f:
        reader = csv.reader(f, delimiter='\t')
        reader.__next__()
        return [row for row in reader]

def get_db():
    """ Connect to the application's configured database. The connection is
    unique for each request and will be reused if this is called again.
    """

    if "db" not in g:
        g.db = sqlite3.connect(
            current_app.config["DATABASE"],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    """ If this request is connected to the database, close the connection. """
    db = g.pop("db", None)

    if db is not None:
        db.close()


def init_db():
    """ Clear existing data and create new tables with card data populated """
    db = get_db()

    with current_app.open_resource("schema.sql") as f:
        db.executescript(f.read().decode("utf8"))

    # Populate the cards
    for row in _get_file_contents("disaster_cards"):
        db.execute(""" INSERT INTO disaster_cards
                       VALUES(?, ?, ?, ?); """, (row))
    for row in _get_file_contents("point_cards"):
        db.execute("""INSERT INTO point_cards
                      VALUES(?, ?, ?, ?, ?); """, (row))
    for row in _get_file_contents("instant_cards"):
        db.execute(""" INSERT INTO instant_cards
                       VALUES(?, ?, ?); """, (row))

@click.command("init-db")
@with_appcontext
def init_db_command():
    """ Clear existing data and create new tables. """
    init_db()
    click.echo("Initialized the database")


def init_app(app):
    """ Register the database functions with the Flask app. """
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
