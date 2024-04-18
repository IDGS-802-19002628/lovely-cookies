from flask import Blueprint, render_template, request, redirect, url_for, abort, send_from_directory
from blueprints.mp.models import MP
from .proveedor_form import ProveedorForm
from flask_login import login_required, current_user
from .model_proveedor import Proveedor,db,ingredienteProveedor
from .proveedor_form import ProveedorForm, MateriaPForm
import os

proveedor_bp = Blueprint("proveedor", __name__, template_folder="templates")

static_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')


@proveedor_bp.errorhandler(403)
def acceso_forbidden(error):
    static_folder = 'static'
    return send_from_directory(static_folder, 'acceso_rol.html'), 403
@proveedor_bp.route("/insProveedor", methods=["GET", "POST"])
@login_required
def insProveedor():
    rol = current_user.rol
    print('rol:', rol)
    if rol != 'administrador':
        print('entro a la validacion')
        print(static_folder)
        abort(403)
    formProvedor = ProveedorForm(request.form)
    formMateriaP = MateriaPForm(request.form)
    ingredientes_choices = None
    
    ingredientes_choices = [(ingrediente.idMP, ingrediente.ingrediente) for ingrediente in MP.query.all()]

    pro = Proveedor.query.all()
    
    resultados = db.session.query(
    Proveedor.idProveedor,
    Proveedor.nomEmpresa,
    Proveedor.direccion,
    Proveedor.telefono,
    Proveedor.nomTrabajador,
    db.func.group_concat(MP.ingrediente)
        ).join(
    ingredienteProveedor, Proveedor.idProveedor == ingredienteProveedor.idProveedor
        ).join(
    MP, ingredienteProveedor.idMP == MP.idMP
        ).filter(
    Proveedor.estatus.is_(True)  # Filtrar por estatus verdadero (True)
        ).group_by(
    Proveedor.idProveedor
        ).all()

    print(resultados)
    datos_tabla = [(idProveedor, proveedor, direccion, telefono, nomTrabajador, ingredientes.split(',')) for idProveedor, proveedor, direccion, telefono, nomTrabajador, ingredientes in resultados]
    
    if request.method == 'POST' and formProvedor.validate():
        proveedor = Proveedor(
            nomEmpresa=formProvedor.nomEmpresa.data,
            direccion=formProvedor.direccion.data,
            telefono=formProvedor.telefono.data,
            nomTrabajador=formProvedor.nomTrabajador.data,
            estatus = 1
        )
        
        # Insertar el proveedor en la base de datos
        db.session.add(proveedor)
        db.session.commit()

        # Procesar los ingredientes seleccionados
        ingredientes_seleccionados = formMateriaP.ingredientes.data
        ingredientes = [int(id_ingrediente) for id_ingrediente in ingredientes_seleccionados]
        print("Ingredientes seleccionados:", ingredientes)

        ultimoProveedor = Proveedor.query.order_by(Proveedor.idProveedor.desc()).first()
        idUltimoProveedor = ultimoProveedor.idProveedor
        print(idUltimoProveedor)

        # Lista para almacenar todas las instancias de IngredienteProveedor
        nuevos_ingred_proveedores = []

        for pro in ingredientes:
            ingredProve = ingredienteProveedor(
                idProveedor=idUltimoProveedor,
                idMP=pro
            )
            nuevos_ingred_proveedores.append(ingredProve)
        print(nuevos_ingred_proveedores)
        # Agregar todas las instancias a la sesión de la base de datos
        db.session.add_all(nuevos_ingred_proveedores)
        # Hacer el commit una sola vez
        db.session.commit()        
        return redirect(url_for('.insProveedor'))  # Redireccionar a la página principal o donde sea necesario
    
    return render_template("insProveedor.html", form=formProvedor, formMateP=ingredientes_choices, datos_tabla=datos_tabla)

@proveedor_bp.route("/eliminarP", methods=["GET", "POST"])
@login_required
def eliminar():
    provee = int(request.args.get('id'))
    proveedor = Proveedor.query.get(provee)
    if proveedor:
        proveedor.estatus = not proveedor.estatus  # Cambiar a True si es False y viceversa
        db.session.commit()
    return redirect(url_for('.insProveedor'))

    # Ruta para mostrar el formulario de actualización con los datos del proveedor seleccionado
@proveedor_bp.route("/actualizar", methods=["GET", "POST"])
def actualizar():
    if request.method == "POST":
        
        return "Proveedor actualizado exitosamente"
    else:
        proveedor_id = request.args.get('id')
        resultados = db.session.query(
    Proveedor.idProveedor,
    Proveedor.nomEmpresa,
    Proveedor.direccion,
    Proveedor.telefono,
    Proveedor.nomTrabajador,
    db.func.group_concat(MP.ingrediente)
        ).join(
    ingredienteProveedor, Proveedor.idProveedor == ingredienteProveedor.idProveedor
        ).join(
    MP, ingredienteProveedor.idMP == MP.idMP
        ).filter(
    Proveedor.idProveedor == proveedor_id  # Filtrar por estatus verdadero (True)
        ).group_by(
    Proveedor.idProveedor
        ).all()

        print(resultados)
        datos_tabla = [(idProveedor, proveedor, direccion, telefono, nomTrabajador, ingredientes.split(',')) for idProveedor, proveedor, direccion, telefono, nomTrabajador, ingredientes in resultados]

        proveedor = Proveedor.query.get(proveedor_id)
        return render_template("InsProveedor.html", proveedor=datos_tabla)