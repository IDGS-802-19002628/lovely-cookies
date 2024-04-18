from flask import Blueprint, render_template, request, redirect, url_for, abort, send_from_directory
from blueprints.mp.models import Mp
from flask_login import login_required, current_user
from .model_compras import CompraProducto, CompraTotal, db
from blueprints.proveedor.model_proveedor import Proveedor
from blueprints.mp.models import Mp
import os


compra_dp = Blueprint("Compras", __name__, template_folder="templates")

static_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')


@compra_dp.errorhandler(403)
def acceso_forbidden(error):
    static_folder = 'static'
    return send_from_directory(static_folder, 'acceso_rol.html'), 403

""" @compra_dp.route("/compras", methods=["GET", "POST"])
@login_required
def compras():
    rol = current_user.rol
    print('rol:', rol)
    if rol != 'administrador':
        print('entro a la validacion')
        print(static_folder)
        abort(403)
    return render_template("compras.html") """

# Ruta para mostrar la interfaz de compras
@compra_dp.route('/compras', methods=['GET', 'POST'])
def compras():
    if request.method == 'POST':
        # Procesar el formulario de compra
        proveedor_id = request.form.get('proveedor')
        materias_primas = request.form.getlist('mp_id')
        cantidades = request.form.getlist('mp_cantidad')
        
        # Iniciar la transacción
        compra_total = CompraTotal()
        db.session.add(compra_total)
        db.session.commit()
        
        total = 0
        
        for mp_id, cantidad in zip(materias_primas, cantidades):
            mp = Mp.query.get(mp_id)
            sub_total = float(cantidad) * mp.precio
            total += sub_total
            
            # Guardar los datos de la compra
            compra_producto = CompraProducto(
                nombreProducto=mp.ingrediente,
                cantidad=float(cantidad),
                medida=mp.medicion,
                subTotal=sub_total,
                idProveedor=proveedor_id,
                idMP=mp_id,
                id=compra_total.idCompraTotal
            )
            db.session.add(compra_producto)
        
        # Guardar la compra total
        compra_total.total = total
        db.session.add(compra_total)
        db.session.commit()
        
        return redirect(url_for('compras'))
    
    # Obtener la lista de proveedores y materias primas para mostrar en la interfaz
    lista_proveedores = Proveedor.query.all()
    lista_materias_primas = Mp.query.all()
    
    return render_template('compras.html', lista_proveedores=lista_proveedores, lista_materias_primas=lista_materias_primas)
