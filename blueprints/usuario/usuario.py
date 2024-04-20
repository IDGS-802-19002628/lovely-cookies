from flask import Blueprint, render_template, request, url_for, redirect, session, flash, send_from_directory, abort
from flask_login import current_user,  login_required
from .usuario_form import UserForm
from .model_usuario import Usuario
from .function.guardar import GestorUsuario
from urllib.parse import urlencode
import logging
import os
from cryptography.fernet import Fernet

usuario_bp = Blueprint("usuario", __name__, template_folder="templates")

static_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')



@usuario_bp.route('/redireccionar')
def redireccionar():
    clave = Fernet.generate_key()
    cipher_suite = Fernet(clave)


    url_original = "http://localhost:5000/modificar?id"
    url_encriptada = cipher_suite.encrypt(url_original.encode())
    print(url_encriptada)
    return redirect(url_encriptada)

@usuario_bp.errorhandler(403)
def acceso_forbidden(error):
    static_folder = 'static'
    return send_from_directory(static_folder, 'no_autorizado.html'), 403

@usuario_bp.route("/usuario", methods=['GET', 'POST'])
@login_required
def usuario():
    form_user = UserForm(request.form)
    gestor_usuario = GestorUsuario()
    usuarios = ''
    alert = ''
    messages =''
    print('Antes de la validacion')
   
    if request.method == "POST":
        messages, alert = gestor_usuario.guardar_usuario(form_user)
        print('prueba')
        if messages == 'info':
          print('desactivar')
        
    flash(messages)
    usuarios = gestor_usuario.obtener_usuarios()
    return render_template("usuario.html", form=form_user, r_usuarios=usuarios, n=alert)

@usuario_bp.route("/eliminar", methods=['GET', 'POST'])
@login_required
def eliminar():
    form_user = UserForm(request.form)
    gestor_usuario = GestorUsuario()
    id_usuario = request.args.get('id')
    messages, alert = gestor_usuario.eliminar_usuario(id_usuario)
    flash(messages)
    usuarios = gestor_usuario.obtener_usuarios()
    return render_template('usuario.html', form=form_user, r_usuarios = usuarios ,n=alert)

@usuario_bp.route("/modificar", methods=['GET', 'POST'])

def modificar():
    
    form_user = UserForm(request.form)
    gestor_usuario = GestorUsuario()
    id_usuario = request.args.get('id')
    session['id_usuario'] = id_usuario
    id_u = session.get('id_usuario')
    method = request.method
    print('metodo ejecutado ', method)
    messages, form_usuario, alert = gestor_usuario.modificar_usuario(id_u, form_user, method)
    if request.method == 'POST':
      messages, form_usuario ,alert = gestor_usuario.modificar_usuario(id_u, form_usuario, method)
      flash(messages)
      usuarios = gestor_usuario.obtener_usuarios()
      form_user = UserForm()

      return render_template('usuario.html', form=form_user, r_usuarios = usuarios ,n=alert)
    return render_template('modificar_usuario.html', form= form_usuario)