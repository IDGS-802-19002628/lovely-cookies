from flask import Blueprint, render_template, request, redirect, url_for, flash
from .model_compras import CompraProducto, CompraTotal, db
from blueprints.proveedor.model_proveedor import Proveedor, ingredienteProveedor
from blueprints.mp.models import Mp
from flask_login import login_required
from flask_login import current_user  # Agregado
from datetime import datetime

compra_dp = Blueprint("compras", __name__, template_folder="templates")
comprasIng = []  # Movido para evitar problemas de alcance global

@compra_dp.route('/compras', methods=['GET', 'POST'])
def compras():
    proveedor_id = request.args.get('proveedor_id')
    lista_materias_primas = []
    listaIngre = []
    total = 0

    lista_proveedores = Proveedor.query.filter_by(estatus=True).all()

    if proveedor_id:
        lista_materias_primas = ingredienteProveedor.query.filter_by(idProveedor=proveedor_id).all()
        listaIngre = []
        for ingre in lista_materias_primas:
            mp = Mp.query.filter_by(idMP=ingre.idMP).all()
            for m in mp:
                listaIngre.append(m)
    if comprasIng:
        for compra in comprasIng:
            # Verificar si el diccionario tiene el atributo 'subTotal'
            if 'subTotal' in compra:
                total += compra['subTotal']
            else:
                # Si no tiene 'subTotal', manejar el caso de error aquí
                # Por ejemplo, puedes imprimir un mensaje de advertencia
                print("Advertencia: No se encontró 'subTotal' en el diccionario:", compra)

    return render_template(
        'compras.html',
        lista_proveedores=lista_proveedores,
        lista_materias_primas=lista_materias_primas,
        proveedor_id=proveedor_id,
        listaIngre=listaIngre,
        comprasIng=comprasIng,  # Pasado como argumento
        total = total
    )

@compra_dp.route("/guatablaCom", methods=['POST'])
@login_required
def tabGalleta():
    proveedor_id = request.form.get('proveedor_id')
    materias_primas = request.form.getlist('ingrediente_id')
    cantidades = request.form.getlist('cantidad')
    caducidad = request.form.getlist('fecha_vencimiento')
    if proveedor_id and materias_primas and cantidades:
        ingSel = Mp.query.filter(Mp.idMP.in_(materias_primas)).all()

        if ingSel:
            for mp, cantidad in zip(ingSel, cantidades):
                if mp.ingrediente == 'pz':
                    subT = round((float(cantidad) * float(mp.precio)),2)
                else:
                    subT = round((float(cantidad) * (float(mp.precio)/1000)),2)
                comprasIng.append({
                    'idProveedor': proveedor_id,
                    'idMp': mp.idMP,
                    'nomPro': mp.ingrediente,
                    'subTotal': subT,
                    'cantidad': cantidad,
                    'medida': mp.medicion,
                    'precio' : mp.precio,
                    'fecha_vencimiento': caducidad
                })
            return redirect(url_for('.compras', proveedor_id = proveedor_id))
        else:
            return render_template('error.html', message='No se encontraron materias primas seleccionadas')
    else:
        return render_template('error.html', message='Faltan datos en el formulario')

@compra_dp.route("/eliminarIngTab", methods=["GET", "POST"])
def eliminarIngTab():
    posicion = int(request.args.get('id'))
    proveedor_id = request.args.get('proveedor_id')  # Obtener desde request.args
    print(proveedor_id)
    if request.method=='GET':
        comprasIng.pop(posicion)
        return redirect(url_for('.compras', proveedor_id=proveedor_id))

@compra_dp.route("/limTablaCom", methods=['GET', 'POST'])
@login_required
def limTabla():
    comprasIng.clear()
    return redirect(url_for('.compras'))

@compra_dp.route("/guardarCompras", methods=['GET', 'POST'])
@login_required
def guardarCompras():
    # Obtener la fecha y hora actual
    ahora = datetime.now()
    total = 0
    # Extraer solo la fecha actual
    fecha_actual = ahora.date()
    if comprasIng:
        for compra in comprasIng:
            # Verificar si el diccionario tiene el atributo 'subTotal'
            if 'subTotal' in compra:
                total += compra['subTotal']
            else:
                # Si no tiene 'subTotal', manejar el caso de error aquí
                # Por ejemplo, puedes imprimir un mensaje de advertencia
                print("Advertencia: No se encontró 'subTotal' en el diccionario:", compra)
    folio = generar_folio()
    user_id = current_user.id
    compraT = CompraTotal(
            total = total,
            id = user_id,
            ticket = folio,
            fecha_compra = ahora
        )
    db.session.add(compraT)
    db.session.commit()
    ultimoCompra = CompraTotal.query.order_by(CompraTotal.idCompraTotal.desc()).first()
    print(ultimoCompra)
    # Lista para almacenar todas las instancias de IngredienteProveedor
    listaCompra = []
    for comIng in comprasIng:
        ingredProve = CompraProducto(
            cantidad = comIng["cantidad"],
            idCompraTotal = ultimoCompra.idCompraTotal,
            subTotal = comIng["subTotal"],
            fecha_caducidad = comIng["fecha_vencimiento"],
            idProveedor = comIng["idProveedor"],
            idMP = comIng["idMp"]
        )
        listaCompra.append(ingredProve)
        print(listaCompra)
    # Agregar todas las instancias a la sesión de la base de datos
    db.session.add_all(listaCompra)
    # Hacer el commit una sola vez
    db.session.commit()
    
    comprasIng.clear()
    return redirect(url_for('.compras'))

def generar_folio():
    # Obtener la fecha y hora actual
    ahora = datetime.now()

    # Formatear la fecha y hora actual como parte del folio
    folio = ahora.strftime("%Y%m%d%H%M%S")

    # Puedes agregar más información al folio si lo deseas, como un prefijo o sufijo
    # Por ejemplo: folio = "COM" + ahora.strftime("%Y%m%d%H%M%S")

    return folio

@compra_dp.route("/mostrar_compras")
def mostrar_compras():
    datos_compras = db.session.query(
        CompraTotal.idCompraTotal,
        Proveedor.nomEmpresa,
        Mp.ingrediente,
        CompraProducto.cantidad,
        CompraProducto.subTotal,
        CompraTotal.total
    ).join(
        CompraProducto, CompraTotal.idCompraTotal == CompraProducto.idCompraTotal
    ).join(
        Mp, CompraProducto.idMP == Mp.idMP
    ).join(
        Proveedor, CompraProducto.idProveedor == Proveedor.idProveedor
    ).all()

    # Agrupar los datos por ID de compra total
    datos_compras_grouped = {}
    for compra in datos_compras:
        id_compra = compra[0]
        if id_compra not in datos_compras_grouped:
            datos_compras_grouped[id_compra] = []
        datos_compras_grouped[id_compra].append({
            'proveedor': compra[1],
            'ingrediente': compra[2],
            'cantidad': compra[3],
            'subtotal': compra[4],
            'total': compra[5]
        })

    return render_template("mostrar_compras.html", datos_compras=datos_compras_grouped)


@compra_dp.route("/aceptar_pedido")
def aceptar_pedido():
    id_compra = request.args.get('id')
    print(id_compra)
    # Obtener la compra total
    compra_total = CompraTotal.query.get(id_compra)
    if compra_total:
        # Verificar si el estado de la compra es 0 (pendiente)
        if compra_total.estatus == 0:
            # Obtener los detalles de compra asociados a esta compra total
            detalles_compra = CompraProducto.query.filter_by(idCompraTotal=id_compra).all()
            if detalles_compra:
                try:
                    # Actualizar las cantidades de los ingredientes
                    for detalle in detalles_compra:
                        ingrediente = Mp.query.get(detalle.idMP)
                        if ingrediente:
                            ingrediente.cantidad -= detalle.cantidad
                            db.session.commit()

                    # Cambiar el estado de la compra a 1 (aceptada)
                    compra_total.estatus = 1
                    db.session.commit()

                    # Redirigir a alguna página de éxito o mostrar un mensaje
                    flash("Pedido aceptado con éxito.", "success")
                    return redirect(url_for("compra_dp.mostrar_compras"))
                except Exception as e:
                    # Manejar cualquier error que pueda ocurrir durante la actualización de la base de datos
                    db.session.rollback()
                    flash("Error al procesar el pedido: " + str(e), "error")
            else:
                flash("No se encontraron detalles de compra para esta compra total.", "error")
        else:
            flash("La compra ya ha sido aceptada previamente.", "info")
    else:
        flash("Compra total no encontrada.", "error")
    
    # Redirigir a alguna página de error en caso de problemas
    return redirect(url_for(".mostrar_compras"))
