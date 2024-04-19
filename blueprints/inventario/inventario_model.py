from flask_sqlalchemy import SQLAlchemy
from config import db
from blueprints.mp.models import Mp


class InventarioMP(db.Model):
    __tablename__ = 'InventarioMP'  # Especifica el nombre de la tabla en la base de datos

    # Define las columnas de la tabla
    idMateria = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idMP = db.Column(db.Integer, db.ForeignKey('MP.idMP'), nullable=False)
    existencias = db.Column(db.Integer, nullable=False)
    fecha_caducidad = db.Column(db.String(15), nullable=False)


