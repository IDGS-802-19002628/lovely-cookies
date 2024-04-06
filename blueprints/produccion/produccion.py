from flask import Blueprint, render_template, request, redirect, url_for
from .produccion_form import ProduccionForm
produccion_bp = Blueprint("produccion", __name__, template_folder="templates")

@produccion_bp.route('/produccion', methods=['GET', 'POST'])
def produccion_index():
    form_produccion = ProduccionForm(request.form)
    if request.method == 'POST':
      print('')
    edit = request.form.get('disabled')
    print('prueba', edit)
    if edit == 'editar':
      print('entro a la url')
      return redirect(url_for('produccion.produccion_cantidad'))
    return render_template("produccion.html", form = form_produccion)

@produccion_bp.route('/produccion_cantidad', methods=['GET', 'POST'])
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