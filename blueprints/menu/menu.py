from flask import Blueprint, render_template

menu_bp = Blueprint("menu", __name__, template_folder="templates")


@menu_bp.route("/menu")
def receta():
    return render_template("menu.html")