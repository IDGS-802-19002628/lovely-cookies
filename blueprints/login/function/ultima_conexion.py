import datetime
from flask import session
import bcrypt
from blueprints.usuario.model_usuario import Usuario, db



class registro:
    def ultima_conexion(self, id):
        ultima_c = Usuario.query.filter_by(id=id).first()
        ultima_c.ultima_conexion = datetime.datetime.now()
        db.session.add(ultima_c)
        db.session.commit()
        return
