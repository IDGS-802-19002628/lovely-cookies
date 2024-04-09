from flask import Blueprint, render_template
from flask_login import login_required

menu_bp = Blueprint("menu", __name__, template_folder="templates")


@menu_bp.route("/menu")
@login_required
def receta():
    return render_template("menu.html")