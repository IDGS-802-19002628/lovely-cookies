from flask import Blueprint, render_template, request, redirect, url_for, abort, current_app, jsonify
from .model_compras import CompraProducto, CompraTotal, db
from blueprints.proveedor.model_proveedor import Proveedor, ingredienteProveedor
from blueprints.mp.models import Mp

compra_dp = Blueprint("compras", __name__, template_folder="templates")

# Ruta para mostrar la interfaz de compras
# Ruta para mostrar la interfaz de compras
@compra_dp.route('/compras', methods=['GET', 'POST'])
def compras():
    proveedor_id = request.args.get('proveedor_id')
    lista_materias_primas = []
    listaIngre = []

    if request.method == 'POST':
        proveedor_id = request.form.get('proveedor')
        materias_primas = request.form.getlist('mp_id')
        cantidades = request.form.getlist('mp_cantidad')
        
        if proveedor_id and materias_primas and cantidades:
            compra_total = CompraTotal()
            db.session.add(compra_total)
            db.session.commit()
            
            total = 0
            for mp_id, cantidad in zip(materias_primas, cantidades):
                mp = Mp.query.get(mp_id)
                sub_total = float(cantidad) * mp.precio
                total += sub_total
                
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
            
            compra_total.total = total
            db.session.add(compra_total)
            db.session.commit()
            
            return redirect(url_for('.compras'))

    # Obtener la lista de proveedores activos
    lista_proveedores = Proveedor.query.filter_by(estatus=True).all()
    
    # Obtener la lista de materias primas si se seleccionó un proveedor
    if proveedor_id:
        lista_materias_primas = ingredienteProveedor.query.filter_by(idProveedor=proveedor_id).all()
        
        # Obtener ingredientes por ID de materia prima
        listaIngre = []
        for ingre in lista_materias_primas:
            mp = Mp.query.filter_by(idMP=ingre.idMP).all()
            for m in mp:
                print(f'Ingrediente: {m.ingrediente}, Medición: {m.medicion}, Precio: {m.precio}')
                listaIngre.append(m)
    
    return render_template(
        'compras.html',
        lista_proveedores=lista_proveedores,
        lista_materias_primas=lista_materias_primas,
        proveedor_id=proveedor_id,
        listaIngre=listaIngre
    )
