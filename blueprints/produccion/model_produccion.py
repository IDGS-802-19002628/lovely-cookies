import datetime
from config import db

class Produccion(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(50))
    pwd=db.Column(db.String(100))
    correo=db.Column(db.String(50))
    rol=db.Column(db.String(50))
    estatus = db.Column(db.String(10))
    create_date=db.Column(db.DateTime, default=datetime.datetime.now)