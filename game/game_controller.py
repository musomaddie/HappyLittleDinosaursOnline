from . import socketio
from flask import Blueprint, redirect, request, render_template, url_for
from flask_socketio import emit

bp = Blueprint("game", __name__, url_prefix="/game")


@bp.route("/", methods=("GET", "POST"))
def join_or_start_game_page():
    """ Manages the initial navigation to the game main page which contains two
    choices: start a new game or join an existing one.
    """
    if request.method == "GET":
        return render_template("game_menu.html")
    if "new_game" in request.form:
        return redirect(url_for("game.start_new_game"))
    return redirect(url_for("game.join_game"))


@bp.route("/start", methods=("GET", "POST"))
def start_new_game():
    """ Manages starting a new game. """
    if request.method == "GET":
        return render_template("game_start_new.html")
    # TODO: I need to generate an ID for the game and use it as the room name
    #  for socket io.
    return redirect(url_for("game.waiting_room"))


@bp.route("/join", methods=("GET",))
def join_game():
    """ Manages joining an existing game. """
    return render_template("game_join.html")


@bp.route("/waiting_room", methods=("GET",))
def waiting_room():
    """ Manages the waiting room before a game starts. """
    return render_template("game_waiting_room.html")

@socketio.event
def connect():
    print("joined python");
    emit("my_response", {"data": "Connected"})
