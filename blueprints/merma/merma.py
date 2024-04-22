from flask import Blueprint, render_template, request, redirect, url_for, flash, session, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from blueprints.receta.models import Galleta
from blueprints.merma.model_merma import Merma
from .form_merma import  MermaForm
from .function.abm import GestionMerma


merma_bp = Blueprint("merma", __name__, template_folder="templates")

@merma_bp.route('/merma' ,methods=['GET', 'POST'])
def merma():
    merma_form = MermaForm(request.form)
    print('Prueba')
    print(request.method )
    messages = ''
    alert = ''
    g = {}
    if request.method == 'POST':
      print('entro a la validacion')
      id = current_user.id
      messages, alert = GestionMerma().guardar_merma(merma_form, id)
      if alert == '':
        alert = 'success'
        messages = 'La merma se ha registrado correctamente.'
      flash(messages)
      g = Galleta.query.all();
      return render_template("merma.html", form=merma_form, galleta= g , n=alert)
    g = Galleta.query.all();
    
    return render_template("merma.html", form=merma_form, galleta= g , n=alert)


@merma_bp.route('/merma_tablero')
def merma_tablero():
    g = Merma.query.all();
    return render_template("tablero_merma.html", merma = g )