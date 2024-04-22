from flask import Blueprint, render_template,json, request, redirect, url_for, flash
from collections import defaultdict
from werkzeug.security import generate_password_hash
from .models import Mp, db
from .forms import MPForm
from blueprints.mp.models import Mp
from flask_login import login_required
from werkzeug.utils import secure_filename
import os
# Crear el Blueprint

mp_bp = Blueprint("mp", __name__, template_folder="templates")

@mp_bp.route("/mp", methods=['GET', 'POST'])
@login_required
def ingresar_mp():
    mp_form =MPForm(request.form)
    if request.method=='POST' and mp_form.validate():
            mp=Mp(ingrediente=mp_form.ingrediente.data,
                        medicion=mp_form.medicion.data,
                        descripcion=mp_form.descripcion.data,
                        precio=mp_form.precio.data
                        )
            db.session.add(mp)
            db.session.commit()
            flash('Ingrediente agregado correctamente')
            return redirect(url_for('mp.ingresar_mp'))
    materias_primas = Mp.query.all()  # Obtener todas las materias primas   
    return render_template("mp.html", mp_form=mp_form, materias_primas=materias_primas)

@mp_bp.route("/mp/<int:id>", methods=['POST'])
@login_required
def eliminar_mp(id):
    if request.method == 'POST':
        materia_prima = Mp.query.get_or_404(id)
        db.session.delete(materia_prima)
        db.session.commit()
        flash('Ingrediente eliminado correctamente')
    return redirect(url_for('mp.ingresar_mp'))

@mp_bp.route("/mp/<int:id>/modificar", methods=['GET', 'POST'])
@login_required
def modificar_mp(id):
    materia_prima = Mp.query.get_or_404(id)
    form = MPForm(request.form, obj=materia_prima)
    if form.validate_on_submit():
        form.populate_obj(materia_prima)
        db.session.commit()
        flash('Ingrediente modificado correctamente')
        return redirect(url_for('mp.ingresar_mp'))
    return render_template('modificar_mp.html', form=form)