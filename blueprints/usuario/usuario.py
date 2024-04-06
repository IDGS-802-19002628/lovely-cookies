from flask import Blueprint, render_template, request, url_for, redirect, session
from .usuario_form import UserForm
from .function.guardar import GestorUsuario  
from flask import flash

usuario_bp = Blueprint("usuario", __name__, template_folder="templates")

@usuario_bp.route("/usuario", methods=['GET', 'POST'])
def usuario():
    form_user = UserForm(request.form)
    gestor_usuario = GestorUsuario()
    usuarios = ''
    #Julian es puto XD
    if request.method == "POST":
        print('hola')
        messages = gestor_usuario.guardar_usuario(form_user)
        print("usuarios de la base de datos",usuarios)
        flash(messages)
    usuarios = gestor_usuario.obtener_usuarios("activo")
    return render_template("usuario.html", form=form_user, r_usuarios = usuarios)

@usuario_bp.route("/eliminar", methods=['GET', 'POST'])
def eliminar():
    gestor_usuario = GestorUsuario()
    id_usuario = request.args.get('id')
    messages = gestor_usuario.eliminar_usuario(id_usuario)
    flash(messages)
    return redirect('/usuario')

@usuario_bp.route("/modificar", methods=['GET', 'POST'])
def modificar():
    form_user = UserForm(request.form)
    gestor_usuario = GestorUsuario()
    id_usuario = request.args.get('id')
    session['id_usuario'] = id_usuario
    id_u = session.get('id_usuario')
    method = request.method
    print('metodo ejecutado ', method)
    messages, form_usuario = gestor_usuario.modificar_usuario(id_u, form_user, method)
    flash(messages)
    if request.method == 'POST':
      return redirect('/usuario')
    return render_template('modificar_usuario.html', form= form_usuario)