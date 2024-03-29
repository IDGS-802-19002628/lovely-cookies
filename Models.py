from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import check_password_hash

db = SQLAlchemy()
class Usuario(db.Model, UserMixin):
    idUsuario = db.Column(db.Integer, primary_key=True)  # Renombramos el atributo a 'id'
    nomUsuario = db.Column(db.String(25))
    contraseña = db.Column(db.String(255))
    rol = db.Column(db.Integer)
    estatus = db.Column(db.Boolean)
    nombre = db.Column(db.String(25))
    apellidoP = db.Column(db.String(25))
    apellidoM = db.Column(db.String(25))
    telefono = db.Column(db.String(10))
    correo = db.Column(db.String(30))

    def get_id(self):
        return str(self.idUsuario)  # Convertimos el id a string

    def check_password(self, password):
        return check_password_hash(self.contraseña, password)
