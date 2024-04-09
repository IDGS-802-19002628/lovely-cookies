from flask_sqlalchemy import SQLAlchemy
import datetime
from config import db

class Galleta(db.Model):
    idGalleta = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(25))
    descripcion = db.Column(db.Text)
    precio = db.Column(db.Float)
    peso = db.Column(db.Float)