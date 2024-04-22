from flask import Blueprint, render_template,abort, send_from_directory
from flask_login import login_required, current_user
from blueprints.tablero.function.abm import Dashboard

import os

tablero_bp = Blueprint("tablero", __name__, template_folder="templates")

static_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

@tablero_bp.errorhandler(403)
def acceso_forbidden(error):
    static_folder = 'static'
    return send_from_directory(static_folder, 'acceso_rol.html'), 403

@tablero_bp.route("/dashboard")
@login_required
def tablero():
    print('Antes de la validacion')
    rol = current_user.rol
    print('rol:', rol)
    if rol != 'administrador':
      print('entro a la validacion')
      print(static_folder)
      abort(403)
    dash = Dashboard()
    dash.guardar_dashboard()
    return render_template("tablero.html")