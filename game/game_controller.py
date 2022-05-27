from flask import Blueprint, render_template

bp = Blueprint("game", __name__, url_prefix="/game")

@bp.route("/", methods=("GET", "POST"))
def start_game_page():
    return render_template("game_menu.html")
