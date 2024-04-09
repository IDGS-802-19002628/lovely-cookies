from flask import Flask, render_template, send_from_directory
from config import DevelomentConfig, db
from blueprints.receta.receta import recetas_bp
from blueprints.menu.menu import menu_bp
from blueprints.usuario.usuario import usuario_bp
from blueprints.login.login import login_bp
from blueprints.proveedor.proveedor import proveedor_bp
from blueprints.produccion.produccion import produccion_bp
from blueprints.venta.ventas import venta_bp

app = Flask(__name__)
app.config.from_object(DevelomentConfig)
app._static_folder = 'static'

@app.errorhandler(404)
def page_not_found(e):
    return send_from_directory(app.static_folder,'404.html'), 404

app.register_blueprint(recetas_bp)
app.register_blueprint(menu_bp)
app.register_blueprint(usuario_bp)
app.register_blueprint(login_bp)
app.register_blueprint(proveedor_bp)
app.register_blueprint(produccion_bp)
app.register_blueprint(venta_bp)

if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(debug=True)