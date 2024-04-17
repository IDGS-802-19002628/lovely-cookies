from flask import Blueprint, render_template, request, redirect, url_for, flash, session, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from blueprints.usuario.model_usuario import Usuario
from .login_form import loginForm
from .function.auth import Autenticador
from .function.intentos_f import desactivar_cuenta
from .function.ultima_conexion import registro
from urllib.parse import urlencode
from flask_cors import CORS
import logging

login_bp = Blueprint("login", __name__, template_folder="templates")




@login_bp.route("/login", methods=['GET', 'POST'])
def login():
    form_auth = loginForm(request.form)
    messages = ''
    alert = ''
    
    if request.method == 'POST':
        try:
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
                username = current_user.nombre
                rol = current_user.rol
                ultima = current_user.ultima_conexion
                logging.info('Inicio de sesión con el correo %s', user.correo)
                return render_template('menu.html' , username = username, rol = rol, ultima = ultima)
        except Exception as e:
            alert = "warning"
            
            flash("No se encontro el correo con el que intenta ingresa")
            return render_template('login.html', form=form_auth, n=alert)
            
    return render_template('login.html', form=form_auth, n=alert)



@login_bp.route("/logout")
@login_required
def logout():
    form_auth = loginForm(request.form)
    id = current_user.id
    registro().ultima_conexion(id)
    logout_user()
    mesasges = 'Has cerrado sesión.'
    alert ='info'
    flash('Has cerrado sesión.')
    return render_template('login.html', n=alert, form = form_auth)
