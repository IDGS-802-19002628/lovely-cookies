from flask import Blueprint, render_template, request, redirect, url_for, abort, send_from_directory
from blueprints.mp.models import MP
from flask_login import login_required, current_user
from .model_compras import CompraProducto, CompraTotal
import os


compra_dp = Blueprint("Compras", __name__, template_folder="templates")

static_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')


@compra_dp.errorhandler(403)
def acceso_forbidden(error):
    static_folder = 'static'
    return send_from_directory(static_folder, 'acceso_rol.html'), 403

@compra_dp.route("/compras", methods=["GET", "POST"])
@login_required
def compras():
    rol = current_user.rol
    print('rol:', rol)
    if rol != 'administrador':
        print('entro a la validacion')
        print(static_folder)
        abort(403)
    return render_template("compras.html")
