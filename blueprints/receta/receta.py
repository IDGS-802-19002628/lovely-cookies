from flask import Blueprint, render_template
from flask_login import login_required

recetas_bp = Blueprint("receta", __name__, template_folder="templates")


@recetas_bp.route("/receta")
@login_required
def receta():
    return render_template("receta.html")
