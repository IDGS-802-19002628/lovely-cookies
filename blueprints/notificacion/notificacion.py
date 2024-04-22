from flask import Blueprint, render_template, redirect  , request
from flask_login import login_required, current_user
from .notificacion_form import NotificacionForm


notificaciones_bp = Blueprint("notificaciones", __name__, template_folder="templates")


@notificaciones_bp.route("/notificacion")
@login_required
def ntf():
    ntf = NotificacionForm()
    nombre = current_user.nombre
    if request.method == 'POST':
      return redirect('/venta')

    