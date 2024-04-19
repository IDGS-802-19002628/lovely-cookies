import logging
import os
from flask_cors import CORS
from flask import Flask, render_template, send_from_directory
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
from config import DevelomentConfig, db
from flask_wtf.csrf import CSRFProtect
from blueprints.menu.menu import menu_bp
from blueprints.login.login import login_bp
from blueprints.produccion.produccion import produccion_bp
from blueprints.usuario.usuario import usuario_bp
from blueprints.mp.mp import mp_bp
from blueprints.tablero.tablero import tablero_bp
from blueprints.usuario.model_usuario import Usuario
from blueprints.venta.ventas import venta_bp
from blueprints.proveedor.proveedor import proveedor_bp
from blueprints.receta.recetas import recetas_bp
from blueprints.Compras.compra import compra_dp
from blueprints.merma.merma import merma_bp

app = Flask(__name__)
app.config.from_object(DevelomentConfig)
app._static_folder = 'static'


allowed_ips = ["127.0.0.1","192.168.1.100"]


cors = CORS(app, resources={r"*": {"origins": allowed_ips}})

login_manager = LoginManager(app)
log_directory = '/logs'
logging.basicConfig(filename=os.path.join('logs/app.log'), level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.getLogger('werkzeug').setLevel(logging.ERROR)
csrf = CSRFProtect(app)

@app.errorhandler(401)
def unauthorized_error(error):
    return send_from_directory(app.static_folder,'no_autorizado.html'), 401


@login_manager.user_loader
def load_user(user_id): 
    return Usuario.query.get(int(user_id))

@app.errorhandler(404)
def page_not_found(e):
    return send_from_directory(app.static_folder,'404.html'), 404


app.register_blueprint(menu_bp)
app.register_blueprint(usuario_bp)
app.register_blueprint(venta_bp)
app.register_blueprint(recetas_bp)
app.register_blueprint(proveedor_bp)
app.register_blueprint(login_bp)
app.register_blueprint(produccion_bp)
app.register_blueprint(mp_bp)
app.register_blueprint(tablero_bp)
app.register_blueprint(compra_dp)
app.register_blueprint(merma_bp)

if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()