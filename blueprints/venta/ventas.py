from flask import Blueprint, render_template, request, redirect, url_for, jsonify, Response
from .venta_form import GalletaForm
from flask_login import login_required, current_user
from .model_venta import Galleta, InventarioG, VentaGalleta, VentaTotal
from config import db
from datetime import datetime

venta_bp = Blueprint("venta", __name__, template_folder="templates")

preVenGa = []  # Lista para almacenar las ventas
ventaTotalG = 0

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