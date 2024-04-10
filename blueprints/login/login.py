from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_login import login_user, logout_user, login_required, current_user
from blueprints.usuario.model_usuario import Usuario
from .login_form import loginForm
from .function.auth import Autenticador
from .function.intentos_f import desactivar_cuenta

login_bp = Blueprint("login", __name__, template_folder="templates")

@login_bp.route("/login", methods=['GET', 'POST'])
def login():
    form_auth = loginForm(request.form)
    messages = ''
    alert = ''
    
    if request.method == 'POST':
        messages, alert, user_id = Autenticador().login(form_auth.correo.data, form_auth.pwd.data)
        messages, contador = desactivar_cuenta().intentos()
        
        if alert == 'warning':
            if contador > 3:
             desactivar_cuenta().desactivar(user_id)
             flash(messages)
             return render_template('login.html', form=form_auth, n=alert)
            if messages == '':
              messages = 'Nombre de usuario o contraseña incorrectos. Por favor, inténtelo de nuevo.'
            flash(messages) 
            return render_template('login.html', form=form_auth, n=alert)
        elif alert == 'success':
            session['contador'] = 0  
            user = Usuario.query.get(user_id)
            login_user(user)
            return render_template('menu.html', username=current_user.nombre , rol = current_user.rol)  
            
    return render_template('login.html', form=form_auth, n=alert)


@login_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/login')
