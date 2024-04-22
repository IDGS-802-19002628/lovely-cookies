from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from config import db
from sqlalchemy import event
from sqlalchemy.orm import validates
from sqlalchemy import event
from sqlalchemy.orm import validates

class Receta(db.Model):
    idReceta = db.Column(db.Integer, primary_key=True)
    idMP = db.Column(db.Integer, db.ForeignKey('mp.idMP'))
    cantidad = db.Column(db.Float)
    idGalleta = db.Column(db.Integer, db.ForeignKey('galleta.idGalleta'))



class Galleta(db.Model):
    idGalleta = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(50))
    descripcion = db.Column(db.String(80))
    precio = db.Column(db.Float)
    peso = db.Column(db.Float)
    imagen = db.Column(db.String(120))  # Ruta de la imagen


