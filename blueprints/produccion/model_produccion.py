from flask_sqlalchemy import SQLAlchemy
from config import db



class Produccion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    cantidad = db.Column(db.Integer)
    estatus = db.Column(db.String(10))
    create_date = db.Column(db.DateTime)