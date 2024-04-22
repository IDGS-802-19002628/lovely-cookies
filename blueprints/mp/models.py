from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from config import db

class Mp(db.Model):
    __tablename__ = 'mp'
    idMP = db.Column(db.Integer, primary_key=True)
    ingrediente = db.Column(db.String) 
    medicion = db.Column(db.String)
    descripcion = db.Column(db.String)  # Corregido de Integer a String
    precio = db.Column(db.Float)

class InventarioMP(db.Model):
    __tablename__ = 'InventarioMP'  # Corregido de inventarioMP a InventarioMP
    idMateria = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idMP = db.Column(db.Integer, db.ForeignKey('mp.idMP'))
    existencias = db.Column(db.Integer)
    fecha_caducidad = db.Column(db.String(15))
    mp = db.relationship("Mp")  # Corregido de mp a Mp
