from flask_sqlalchemy import SQLAlchemy
import datetime

db_produccion=SQLAlchemy()
class Produccion(db_produccion.Model):
    id=db_produccion.Column(db_produccion.Integer, primary_key=True)
    nombre=db_produccion.Column(db_produccion.String(50))
    pwd=db_produccion.Column(db_produccion.String(100))
    correo=db_produccion.Column(db_produccion.String(50))
    rol=db_produccion.Column(db_produccion.String(50))
    estatus = db_produccion.Column(db_produccion.String(10))
    create_date=db_produccion.Column(db_produccion.DateTime, default=datetime.datetime.now)