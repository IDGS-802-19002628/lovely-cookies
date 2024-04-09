from flask import Blueprint, render_template

recetas_bp = Blueprint("receta", __name__, template_folder="templates")


@recetas_bp.route("/receta")
def receta():
    return render_template("receta.html")
