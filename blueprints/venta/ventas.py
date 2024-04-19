from flask import Blueprint, render_template, request,flash, redirect, url_for, jsonify, Response, send_from_directory
from blueprints.receta.models import Galleta
from .venta_form import GalletaForm
from flask_login import login_required, current_user
from .model_venta import  InventarioG, VentaGalleta, VentaTotal, Cajach,Pago_p
from config import db
from datetime import datetime

venta_bp = Blueprint("venta", __name__, template_folder="templates")

preVenGa = []  # Lista para almacenar las ventas
ventaTotalG = 0

@venta_bp.errorhandler(403)
def acceso_forbidden(error):
    static_folder = 'static'
    return send_from_directory(static_folder, 'acceso_rol.html'), 403

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
@login_required
def venta():
    ventaTotalB = 0
    idg = request.args.get('id')
    galleta = None
    galletaoinve = None
    galletaInven = InventarioG.query.all()
    galletas = Galleta.query.all()
    
    if request.method == 'POST' or 'GET':
        if idg is not None:
            galleta = consultar_galleta_por_id(idg)
            galletaoinve = consultar_InventarioGalleta_por_id(idg)
            # PreVenGa no parece estar definido en este código, asegúrate de que está definido.
            # Si es una lista de elementos de subtotal, puedes sumarlos aquí.
        ventaTotalB = sum(float(total['subTotal']) for total in preVenGa)
        print(ventaTotalB)

    # Combina las listas `galletas` y `galletaInven` usando `zip`.
    galletas_y_inventario = zip(galletas, galletaInven)

    return render_template(
        "ventas.html",
        galletaInven=galletaInven,
        galleta=galleta,
        Databla=preVenGa,
        total=ventaTotalB,
        galletas_y_inventario=galletas_y_inventario,
        galletaoinve = galletaoinve
    )


@venta_bp.route("/imagen/<int:id>")
def obtener_imagen(id):
    # Consulta la galleta por ID en la base de datos
    galleta = Galleta.query.get(id)
    if galleta and galleta.imagen:
        # Devuelve la imagen como respuesta HTTP con el tipo MIME apropiado
        return Response(galleta.imagen, mimetype='image/jfif')  # Ajusta el MIME type según el formato de la imagen
    else:
        # Maneja el caso en el que no se encuentra la imagen
        return "Imagen no encontrada", 404

@venta_bp.route("/guatabla", methods=['GET', 'POST'])
@login_required
def tabGalleta():
    # Obtener datos del formulario
    idg = request.args.get('idG')
    nombre_galleta = request.args.get('nombre')
    precio = request.args.get('txtPrecio')
    cantidad = request.args.get('txtCantidadPieza')
    tipo = request.args.get('categoria')
    subTotal = request.args.get('txtTotalPiezas')
    peso = request.args.get('peso')

    cantidadPCPE = request.args.get('caja')
    if cantidadPCPE == None or 0:
        cantidadPCPE = int(float(peso)*float(cantidad))
    print(cantidadPCPE)

    if subTotal == None or 0:
        subTotal = request.args.get('TotalPeso')
        if subTotal == None or 0:
            subTotal = request.args.get('TotalCaja')

    if cantidad == None or 0:
        cantidad = request.args.get('cantidadGalletaP')
        if cantidad == None or 0:
            cantidad = request.args.get('CantidadGalletasCaja')
    
    print(subTotal)
    # Validación de datos
    if not idg or not cantidad or not tipo or not subTotal:
        return jsonify({'error': 'Faltan datos en el formulario'}), 400
    
    tipoVe=""

    if tipo == "1":
        tipoVe = "Pieza"
    elif tipo == "2":
        tipoVe = "Gramos"
    elif tipo == "3":
        tipoVe = "Caja"

    # Agregar datos a la lista preVenGa
    preVenGa.append({
        'idGalleta': idg,
        'nombreGalleta': nombre_galleta,
        'precio': precio,
        'cantidad': cantidad,
        'peso' : cantidadPCPE,
        'tipoVenta': tipoVe,
        'tipo':tipo,
        'subTotal': subTotal
    })

    # Imprimir la lista para verificar
    print(preVenGa)

    # Redireccionar a la página de venta
    return redirect(url_for('.venta'))

# Otras rutas y funciones pueden seguir aquí


def consultar_galleta_por_id(id_galleta):
    try:
        # Consulta la galleta por su ID
        galleta = Galleta.query.filter_by(idGalleta=id_galleta).first()
        return galleta
    except Exception as e:
        print("Error al consultar la galleta por ID:", e)
        return None

def consultar_InventarioGalleta_por_id(id_galleta):
    try:
        # Consulta la galleta por su ID
        galleta = InventarioG.query.filter_by(idGalleta=id_galleta).first()
        return galleta
    except Exception as e:
        print("Error al consultar la galleta por ID:", e)
        return None
    
@venta_bp.route("/limTabla", methods=['GET', 'POST'])
@login_required
def limTabla():
    preVenGa.clear()
    return redirect(url_for('.venta'))

@venta_bp.route("/guardar", methods=['GET', 'POST'])
@login_required
def guardar():
    # Obtener la fecha y hora actual
    ahora = datetime.now()

    # Extraer solo la fecha actual
    fecha_actual = ahora.date()
    tota = request.args.get('total')
    user_id = current_user.id
    ventaTotaldb = VentaTotal(
            total = tota,
            id = user_id,
            fecha = fecha_actual
        )
    sumar_totales_ventas(tota)
    db.session.add(ventaTotaldb)
    db.session.commit()
             
    ultimoVenta = VentaTotal.query.order_by(VentaTotal.idVentaTotal.desc()).first()
    print(ultimoVenta)
    # Lista para almacenar todas las instancias de IngredienteProveedor
    listaCompra = []
    for venGa in preVenGa:
        ingredProve = VentaGalleta(
            idGalleta = venGa["idGalleta"],
            idVentaTotal = ultimoVenta.idVentaTotal,
            subTotal = venGa["subTotal"],
            cantidad = venGa["cantidad"],
            tipoVenta = venGa["tipo"],
            peso = venGa["peso"]
        )
        listaCompra.append(ingredProve)
        print(listaCompra)
    # Agregar todas las instancias a la sesión de la base de datos
    db.session.add_all(listaCompra)
    # Hacer el commit una sola vez
    db.session.commit()
    
    for desgaInt in preVenGa:
        id_galleta = desgaInt["idGalleta"]
        cantidad_vendida = desgaInt["cantidad"]
        actualizar_inventario_por_id(int(id_galleta), int(cantidad_vendida))


    preVenGa.clear()
    return redirect(url_for('.venta'))

def actualizar_inventario_por_id(id_galleta, cantidad_vendida):
    # Filtra la tabla para encontrar el registro con el id de la galleta que deseas actualizar
    inventario = InventarioG.query.filter_by(idGalleta=id_galleta).first()
    
    if inventario:
        # Resta la cantidad vendida de la cantidad actual
        inventario.cantidad -= cantidad_vendida
        
        # Confirma los cambios en la base de datos
        db.session.commit()
        
        print(f"Inventario actualizado: cantidad de galletas restantes: {inventario.cantidad}")
    else:
        print(f"No se encontró un registro con idGalleta {id_galleta}.")


def sumar_totales_ventas(tota):
        # Consultar todas las ventas en la tabla VentaTotal
    ventas = VentaTotal.query.all()
        
        # Inicializar la variable para almacenar la suma de los totales
    suma_totales = 0
        
        # Sumar los totales de todas las ventas
    for venta in ventas:
        suma_totales += venta.total
        
        # Actualizar el campo total en la tabla Cajach con la suma de los totales
    cajach = Cajach.query.first()
    cajach.total += float(tota)
        
        # Guardar los cambios en la base de datos
    db.session.commit()

@venta_bp.route("/ventas_totales", methods=['GET'])
@login_required
def ventas_totales():
    # Consulta todos los registros en la tabla VentaTotal
    ventas_totales = VentaTotal.query.filter(VentaTotal.fecha == datetime.now().date()).all()
    pagosp = Pago_p.query.all()
    # Crear una lista para almacenar los datos de las ventas
    ventas_totales_datos = []

    # Iterar sobre cada venta total y agregar sus datos a la lista
    suma_ventas = 0  # Variable para almacenar la suma de todas las ventas

    for venta in ventas_totales:
        venta_datos = {
            'idVentaTotal': venta.idVentaTotal,
            'total': venta.total,
            'id': venta.id,
            'fecha': venta.fecha  # Si 'fecha' ya es una cadena, no necesitas usar strftime
        }
        ventas_totales_datos.append(venta_datos)

        suma_ventas += venta.total  # Sumar el total de cada venta

    # Renderizar la plantilla y pasar los datos de las ventas totales y la suma de las ventas
    return render_template('ventasD.html', ventas_totales=ventas_totales_datos, suma_ventas=suma_ventas,pagos=pagosp)

@venta_bp.route("/restar_venta", methods=['POST'])
@login_required
def restar_venta():
    # Obtener la cantidad del formulario
    cantidad = request.form.get('cantidad')

    # Convertir la cantidad a float
    cantidad = float(cantidad)

    # Consultar el registro de CajaCh
    caja_ch = Cajach.query.first()

    # Verificar si hay suficiente total en CajaCh
    if caja_ch.total < cantidad:
        flash('No hay suficiente total en CajaCh para restar esta cantidad.', 'error')
        return redirect(url_for('venta.ventas_totales'))

    # Restar la cantidad al total de CajaCh
    caja_ch.total -= cantidad

    # Crear un nuevo registro en Pago_p con la cantidad restada
    nuevo_pago = Pago_p(cantidad=cantidad, fecha=datetime.now().date())
    db.session.add(nuevo_pago)

    # Guardar los cambios en la base de datos
    db.session.commit()

    flash('La cantidad ha sido restada exitosamente.', 'success')
    return redirect(url_for('venta.ventas_totales'))