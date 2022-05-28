from flask import Blueprint, redirect, request, render_template, url_for

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

@bp.route("/start_new", methods=("GET",))
def start_new_game():
    """ Manages starting a new game. """
    return render_template("game_start_new.html")

@bp.route("/join", methods=("GET",))
def join_game():
    """ Manages joining an existing game. """
    return render_template("game_join.html")
