from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_login import login_user, logout_user, login_required, current_user
from blueprints.usuario.model_usuario import Usuario
from .login_form import loginForm
from .function.auth import Autenticador


login_bp = Blueprint("login", __name__, template_folder="templates")

@login_bp.route("/login", methods=['GET', 'POST'])
def login():
    form_auth = loginForm(request.form)
    messages = ''
    alert = ''
    
    if request.method == 'POST':
        messages, alert, user_id = Autenticador().login(form_auth.correo.data, form_auth.pwd.data)
        if alert == 'warning':
            
            flash(messages) 
            return render_template('login.html', form=form_auth, n=alert)
        elif alert == 'success':
            user = Usuario.query.get(user_id)
            login_user(user)
            return render_template('menu.html', username = user.nombre)  
            
    return render_template('login.html', form=form_auth, n=alert)


@login_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/login')