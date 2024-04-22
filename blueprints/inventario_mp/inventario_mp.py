from flask import Blueprint, render_template
from .models import Inventariomp, db
from blueprints.mp.models import Mp



inventario_mp_bp = Blueprint("inventario_mp", __name__, template_folder="templates")

@inventario_mp_bp.route('/mostrar_inventario')
def mostrar_inventario():
    inventario = db.session.query(Inventariomp, Mp).join(Mp, Inventariomp.idMP == Mp.idMP).all()
    return render_template('mostrar_inventario.html', inventario=inventario)