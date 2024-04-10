from flask import Blueprint, render_template, request, url_for, redirect, session, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, login_manager
from .usuario_form import UserForm
from .model_usuario import Usuario
from .function.guardar import GestorUsuario


usuario_bp = Blueprint("usuario", __name__, template_folder="templates")

@usuario_bp.route("/usuario", methods=['GET', 'POST'])
def usuario():
    form_user = UserForm(request.form)
    gestor_usuario = GestorUsuario()
    usuarios = ''
    alert = ''
    
    if request.method == "POST":
        messages, alert = gestor_usuario.guardar_usuario(form_user)
        flash(messages)
    usuarios = gestor_usuario.obtener_usuarios()
    
    return render_template("usuario.html", form=form_user, r_usuarios=usuarios, n=alert)

@usuario_bp.route("/eliminar", methods=['GET', 'POST'])
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