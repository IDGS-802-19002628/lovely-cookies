from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_login  import login_required
from .produccion_form import ProduccionForm
from .function.abm import Gestorproduccion 
produccion_bp = Blueprint("produccion", __name__, template_folder="templates")

@produccion_bp.route('/produccion', methods=['GET', 'POST'])
@login_required
def produccion_index():
    form_produccion = ProduccionForm(request.form)
    messages =''
    alert=''
    if request.method == 'POST':
      messages, alert = Gestorproduccion().guardar_produccion(form_produccion)
    b = Gestorproduccion().obtener_produccion()
    flash(messages)
    return render_template("produccion.html", form = form_produccion, r_produccion = b , n=alert)
  
@produccion_bp.route("/modificar_produccion", methods=['GET', 'POST'])
@login_required
def modificar():
    form_produccion = ProduccionForm(request.form)
    id_produccion = request.args.get('id')
    session['id_produccion'] = id_produccion
    id_p = session.get('id_produccion')
    method = request.method
    print('metodo ejecutado ', method)
    messages, form_pro, alert = Gestorproduccion().modificar_produccion(id_p, form_produccion, method)
    if request.method == 'POST':
      
      messages, form_pro ,alert = Gestorproduccion().modificar_produccion(id_p, form_pro, method)
      form_usuario = ProduccionForm()
      flash(messages)
      producciones = Gestorproduccion().obtener_produccion()
      form_p = ProduccionForm()
      return render_template('produccion.html', form=form_p, r_produccion = producciones ,n=alert)
    return render_template('modificar_produccion.html', form= form_pro)


@produccion_bp.route('/produccion_cantidad', methods=['GET', 'POST'])
@login_required
def produccion_cantidad():
    form_produccion = ProduccionForm(request.form)
    mi_variable_disabled = False
    if mi_variable_disabled:
      print('sen cambio a False')
    edit = request.form.get('disabled')
    if edit == 'cantidad':
      print('entro a desactivar')
      return redirect(url_for('produccion.produccion_index'))
    return render_template("produccion_cantidad.html", form = form_produccion, cantidad = mi_variable_disabled)