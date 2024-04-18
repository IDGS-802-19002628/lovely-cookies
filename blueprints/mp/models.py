from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from config import db

class Mp(db.Model):
    idMP = db.Column(db.Integer, primary_key=True)
    ingrediente = db.Column(db.String) 

    medicion = db.Column(db.String)
    descripcion = db.Column(db.Integer, db.ForeignKey('galleta.idGalleta')) 
    precio = db.Column(db.Float)