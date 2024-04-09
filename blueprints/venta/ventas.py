from flask import Blueprint, render_template, request, redirect, url_for
from .venta_form import GalletaForm
from flask_login import login_required
from .model_venta import Galleta

venta_bp = Blueprint("venta", __name__, template_folder="templates")


@venta_bp.route("/ventaPieza")
def ventaP():
    return render_template("ventaPieza.html")

@venta_bp.route("/ventaPeso")
def ventaPe():
    return render_template("ventaPeso.html")

@venta_bp.route("/ventaCaja")
def ventaC():
    return render_template("ventaCaja.html")

@venta_bp.route("/venta", methods=['GET', 'POST'])
def venta():
    idg = (request.args.get('id'))
    galleta = None
    if request.method == 'POST' or 'GET':
        if idg != 0:
            galleta = consultar_galleta_por_id(idg)
        
        
    return render_template("ventas.html", galleta=galleta)

def consultar_galleta_por_id(id_galleta):
    try:
        # Consulta la galleta por su ID
        galleta = Galleta.query.filter_by(idGalleta=id_galleta).first()
        return galleta
    except Exception as e:
        print("Error al consultar la galleta por ID:", e)
        return None