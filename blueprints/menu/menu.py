from flask import Blueprint, render_template
from flask_login import login_required, current_user


menu_bp = Blueprint("menu", __name__, template_folder="templates")


@menu_bp.route("/menu")
@login_required
def menu():
    nombre = current_user.nombre
    rol = current_user.rol
    return render_template("menu.html", username = nombre, rol = rol)