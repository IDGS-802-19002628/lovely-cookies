from flask import Flask, request, render_template, redirect, url_for, session, Response
from config import DevelomentConfig
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from Models import Usuario, db
from captcha.image import ImageCaptcha
import random

#prueba :)

app = Flask(__name__)
app.config.from_object(DevelomentConfig)

db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

def consulta_usuario(username, password):
    # Realizar la consulta a la base de datos para validar los datos
    usuario = Usuario.query.filter_by(nomUsuario=username).first()
    if usuario:
        if usuario and usuario.check_password(password):
            return usuario
        else:
            return "Contraseña no valida"
    else:
        return 'Usuario no encontrado'    

@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        captcha = request.form['captcha']

        if captcha != session['captcha']:
            return render_template("login.html", error="Captcha incorrecto")

        mensaje = consulta_usuario(username, password)
        print(mensaje)
        if isinstance(mensaje, Usuario):
            login_user(mensaje)
            return redirect(url_for('dashboard', usuario = mensaje))
        else:
            return render_template("login.html", error=mensaje)
    else:
        return render_template("login.html")

@app.route("/home")
@login_required
def dashboard():
    usuario = current_user  # Obtener el usuario actualmente autenticado
    return render_template("home.html", nombre=usuario.nombre)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/captcha')
def generate_captcha():
    image = ImageCaptcha(width=200, height=80, font_sizes=(40, 45))
    captcha_text = ''.join(random.choices('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=6))
    session['captcha'] = captcha_text
    data = image.generate(captcha_text)
    return Response(data, mimetype='image/png')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
