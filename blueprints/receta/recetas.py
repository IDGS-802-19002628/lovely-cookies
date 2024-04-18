from flask import Blueprint, render_template,json, request, redirect, url_for, flash
from collections import defaultdict
from werkzeug.security import generate_password_hash
from .models import Receta, Galleta, db
from .forms import RecetaForm,GalletaForm
from blueprints.mp.models import Mp
from flask_login import login_required
from werkzeug.utils import secure_filename
import os
# Crear el Blueprint

recetas_bp = Blueprint("recetas", __name__, template_folder="templates")

@recetas_bp.route("/recetas", methods=['GET', 'POST'])
@login_required
def crear_receta():
    # Crear las instancias de los formularios
    galleta_form = GalletaForm(request.form)
    recetas_form = RecetaForm(request.form)
    ingredientes_texto = request.form.get('ingredientes_texto')
    ingredientes = []
    if ingredientes_texto is not None:
        ingredientes = json.loads(ingredientes_texto)

    # Obtener las opciones para los campos de selección
    lista_ingredientes = [(mp.idMP, mp.ingrediente) for mp in Mp.query.all()]
    lista_galletas = [(galleta.idGalleta, galleta.nombre) for galleta in Galleta.query.all()]

    # Asignar las opciones a los campos de selección
    recetas_form.idMp.choices = lista_ingredientes
    recetas_form.idGalleta.choices = lista_galletas
    ultima_galleta = Galleta.query.order_by(Galleta.idGalleta.desc()).first()
    if ultima_galleta:
        recetas_form.idGalleta.data = ultima_galleta.idGalleta
    # Manejar el envío del formulario
    if request.method == 'POST':
        if 'crear_galleta' in request.form:
            if galleta_form.validate():
                # Crear una nueva galleta
                nueva_galleta = Galleta(nombre=galleta_form.nombre.data,
                                        descripcion=galleta_form.descripcion.data,
                                        precio=galleta_form.precio.data,
                                        peso=galleta_form.peso.data)

                # Guardar la imagen
                imagen = request.files['imagen']
                if imagen:
                    filename = secure_filename(imagen.filename)
                    imagen.save(os.path.join('C:/Users/Julian/Pictures/imagenes galletas', filename))
                    nueva_galleta.imagen = filename

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
        ingrediente = Mp.query.get(receta.idMP)
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

@recetas_bp.route("/eliminar_receta", methods=['POST'])
@login_required
def eliminar_receta():

    id_galleta = request.form.get('idGalleta')
    recetas = Receta.query.filter_by(idGalleta=id_galleta).all()

    for receta in recetas:
        db.session.delete(receta)

    # Guardar los cambios en la base de datos
    db.session.commit()

    flash('¡Recetas eliminadas correctamente!', 'success')

    # Redireccionar a la página principal para evitar reenvío del formulario
    return redirect(url_for('recetas.crear_receta'))

@recetas_bp.route("/calcular_utilidades", methods=['GET'])
@login_required
def calcular_utilidades():
    # Obtener todas las galletas de la base de datos
    galletas = Galleta.query.all()

    # Lista para almacenar los resultados de los cálculos
    resultados = []

    # Iterar sobre cada galleta y calcular su costo y utilidad
    for galleta in galletas:
        # Obtener los ingredientes y cantidades de la receta de la galleta
        recetas = Receta.query.filter_by(idGalleta=galleta.idGalleta).all()
        costo_total = 0

        # Calcular el costo total de los ingredientes
        for receta in recetas:
            ingrediente = Mp.query.get(receta.idMP)
            costo_total += (ingrediente.precio * receta.cantidad)

        # Calcular la utilidad y el costo por galleta
        costo_por_galleta = costo_total
        utilidad = galleta.precio - costo_por_galleta

        # Agregar los resultados a la lista
        resultados.append({
            'galleta': galleta,
            'costo_por_galleta': costo_por_galleta,
            'utilidad': utilidad
        })

    # Renderizar la plantilla HTML con los resultados
    return render_template('costo_utilidad.html', resultados=resultados)