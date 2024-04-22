from flask import session
import bcrypt
from blueprints.usuario.model_usuario import Usuario, db

class desactivar_cuenta:
    def intentos(self,):
        if 'contador' not in session:
            session['contador'] = 0
        messages = ''
        contador = session['contador']
        contador += 1
        print('intento', contador)
        if contador > 3:
          messages = "Ha superado el número máximo de intentos. Su cuenta ha sido desactivada."
        
        session['contador'] = contador
        return messages , contador
    def desactivar(self, id):
        usuario_a_desactivar = Usuario.query.filter_by(id=id).first()
        usuario_a_desactivar.estatus = "inactivo"
        db.session.add(usuario_a_desactivar)
        db.session.commit()
        return
        
        
