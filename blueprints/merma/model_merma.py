
from config import db
import datetime


class Merma(db.Model):
    idMerma=db.Column(db.Integer, primary_key=True)
    fecha=db.Column(db.String(30), default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
    producto=db.Column(db.String(50))
    cantidad=db.Column(db.Integer)
    id=db.Column(db.Integer)
    observacion=db.Column(db.Text)
    
    
