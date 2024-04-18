from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from config import db

class MP(db.Model):
    idMP = db.Column(db.Integer, primary_key=True)
    ingrediente = db.Column(db.String(30)) 
    medicion = db.Column(db.String(15))
    descripcion = db.Column(db.Integer, db.ForeignKey('galleta.idGalleta')) 
    precio = db.Column(db.Double)