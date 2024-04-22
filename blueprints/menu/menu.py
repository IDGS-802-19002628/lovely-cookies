from flask import Blueprint, render_template,send_from_directory
from flask_login import login_required, current_user


menu_bp = Blueprint("menu", __name__, template_folder="templates")

def page_not_found(e):
    return send_from_directory(app.static_folder,'404.html'), 404
@menu_bp.route("/menu")
@login_required
def menu():
    nombre = current_user.nombre
    rol = current_user.rol
    ultima_c = current_user.ultima_conexion
    return render_template("menu.html", username = nombre, rol = rol, ultima = ultima_c)