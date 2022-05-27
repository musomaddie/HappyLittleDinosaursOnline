from flask import Blueprint, render_template

bp = Blueprint("content", __name__)

@bp.route("/", methods=("GET",))
def home_page():
    return render_template("home_page.html")

@bp.route("/rules", methods=("GET",))
def rules():
    return render_template("rules.html")
