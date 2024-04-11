from flask import Blueprint, render_template,json, request, redirect, url_for, flash
from collections import defaultdict
from werkzeug.security import generate_password_hash
from .models import Receta, Galleta, db
from .forms import RecetaForm,GalletaForm
from blueprints.mp.models import Mp
from flask_login import login_required

# Crear el Blueprint

recetas_bp = Blueprint("recetas", __name__, template_folder="templates")


# Definir la ruta y la vista correspondiente
@recetas_bp.route("/recetas", methods=['GET', 'POST'])
@login_required
def crear_receta():
    # Crear las instancias de los formularios
    galleta_form = GalletaForm(request.form)
    recetas_form = RecetaForm(request.form)

    # Obtener las opciones para los campos de selección
    lista_ingredientes = [(mp.idMP, mp.ingrediente) for mp in Mp.query.all()]
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
                for ingrediente_id, cantidad in zip(ingredientes_seleccionados, cantidades):
                    # Crear la nueva receta
                    nueva_receta = Receta(
                        idMP=ingrediente_id,
                        cantidad=cantidad,
                        idGalleta=id_galleta
                    )
                    db.session.add(nueva_receta)

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