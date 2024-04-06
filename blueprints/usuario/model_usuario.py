from flask_sqlalchemy import SQLAlchemy
import datetime

db_usuario=SQLAlchemy()
class Usuario(db_usuario.Model):
    id=db_usuario.Column(db_usuario.Integer, primary_key=True)
    nombre=db_usuario.Column(db_usuario.String(50))
    pwd=db_usuario.Column(db_usuario.String(100))
    correo=db_usuario.Column(db_usuario.String(50))
    rol=db_usuario.Column(db_usuario.String(50))
    estatus = db_usuario.Column(db_usuario.String(10))
    create_date=db_usuario.Column(db_usuario.DateTime, default=datetime.datetime.now)