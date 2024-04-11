import logging
import os
from flask import Flask, render_template, send_from_directory
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from config import DevelomentConfig, db
from flask_wtf.csrf import CSRFProtect

from blueprints.receta.receta import recetas_bp
from blueprints.menu.menu import menu_bp
from blueprints.login.login import login_bp
from blueprints.produccion.produccion import produccion_bp
from blueprints.usuario.usuario import usuario_bp
from blueprints.usuario.model_usuario import Usuario




app = Flask(__name__)
app.config.from_object(DevelomentConfig)
app._static_folder = 'static'
login_manager = LoginManager(app)
log_directory = '/logs'
logging.basicConfig(filename=os.path.join('logs/app.log'), level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.getLogger('werkzeug').setLevel(logging.ERROR)
csrf = CSRFProtect(app)



@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

@app.errorhandler(404)
def page_not_found(e):
    return send_from_directory(app.static_folder,'404.html'), 404

app.register_blueprint(recetas_bp)
app.register_blueprint(menu_bp)
app.register_blueprint(usuario_bp)
app.register_blueprint(login_bp)
app.register_blueprint(produccion_bp)
if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()