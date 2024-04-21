from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from config import db

class Inventariomp(db.Model):
    idMateria = db.Column(db.Integer, primary_key=True)
    idMP = db.Column(db.Integer) 
    existencias = db.Column(db.Integer)
    fecha_caducidad = db.Column(db.Date)     
    