from flask import Blueprint, render_template,json, request, redirect, url_for, flash ,abort, send_from_directory
from collections import defaultdict
from werkzeug.security import generate_password_hash
from .models import Receta, Galleta, db
from .forms import RecetaForm,GalletaForm
from blueprints.mp.models import MP
from flask_login import login_required , current_user
import os

# Crear el Blueprint

recetas_bp = Blueprint("recetas", __name__, template_folder="templates")

static_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

# Definir la ruta y la vista correspondiente

@recetas_bp.errorhandler(403)
def acceso_forbidden(error):
    static_folder = 'static'
    return send_from_directory(static_folder, 'acceso_rol.html'), 403

@recetas_bp.route("/recetas", methods=['GET', 'POST'])
@login_required
def crear_receta():
    rol = current_user.rol
    print('rol:', rol)
    if rol != 'administrador':
        print('entro a la validacion')
        print(static_folder)
        abort(403)
    # Crear las instancias de los formularios
    galleta_form = GalletaForm(request.form)
    recetas_form = RecetaForm(request.form)
    ingredientes_texto = request.form.get('ingredientes_texto')
    ingredientes = []
    if ingredientes_texto is not None:
        ingredientes = json.loads(ingredientes_texto)

    # Obtener las opciones para los campos de selección
    lista_ingredientes = [(mp.idMP, mp.ingrediente) for mp in MP.query.all()]
    lista_galletas = [(galleta.idGalleta, galleta.nombre) for galleta in Galleta.query.all()]

    # Asignar las opciones a los campos de selección
    recetas_form.idMp.choices = lista_ingredientes
    recetas_form.idGalleta.choices = lista_galletas

    # Manejar el envío del formulario
    if request.method == 'POST':
        if 'crear_galleta' in request.form:
            if galleta_form.validate():
                # Crear una nueva galleta
                nueva_galleta = Galleta(nombre=galleta_form.nombre.data)
                db.session.add(nueva_galleta)
                db.session.commit()
                flash('¡Galleta creada correctamente!', 'success')

                # Redireccionar a la página principal para evitar reenvío del formulario
                return redirect(url_for('recetas.crear_receta'))

        elif 'crear_receta' in request.form:
            if recetas_form.validate():
                # Obtener los datos del formulario
                id_galleta = recetas_form.idGalleta.data
                ingredientes_seleccionados = request.form.getlist('idMp')
                cantidades = request.form.getlist('cantidad')

                # Crear una nueva receta para cada ingrediente seleccionado
                for ingrediente in ingredientes:
                    nueva_receta = Receta(
                        idMP=ingrediente['idMp'],
                        cantidad=ingrediente['cantidad'],
                        idGalleta=ingrediente['idGalleta']
                    )
                    db.session.add(nueva_receta)
                print(ingredientes)
                print(ingredientes_texto)
                # Guardar los cambios en la base de datos
                db.session.commit()
                flash('¡Recetas creadas correctamente!', 'success')

                # Redireccionar a la página principal para evitar reenvío del formulario
                return redirect(url_for('recetas.crear_receta'))

    # Agrupar las recetas por galleta
    recetas_agrupadas = defaultdict(list)
    for receta in Receta.query.all():
        ingrediente = MP.query.get(receta.idMP)
        ingrediente_nombre = ingrediente.ingrediente
        medicion = ingrediente.medicion
        galleta_nombre = Galleta.query.filter_by(idGalleta=receta.idGalleta).first().nombre
        receta_dict = {
            'ingrediente': ingrediente_nombre,
            'medicion': medicion,
            'cantidad': receta.cantidad,
            'galleta': galleta_nombre
        }
        recetas_agrupadas[receta.idGalleta].append(receta_dict)

    # Renderizar la plantilla HTML con los datos
    return render_template('recetas.html', galleta_form=galleta_form, recetas_form=recetas_form,
                           recetas_agrupadas=recetas_agrupadas)