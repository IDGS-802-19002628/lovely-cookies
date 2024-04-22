
from config import db
import datetime


class Notificacion(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nombre_u=db.Column(db.String(50))
    nombre_g = db.Column(db.String(10))
    estatus = db.Column(db.String(10))
    create_date=db.Column(db.DateTime, default=datetime.datetime.now)
    
