import bcrypt
from blueprints.usuario.model_usuario import Usuario, db

class Autenticador:
    def login(self, correo, password):
        print(correo)
        print(password)
        alert =''
        usuario_a_login = Usuario.query.filter_by(correo=correo).first()
        id = usuario_a_login.id
        if usuario_a_login:
            hashed_password_bytes = usuario_a_login.pwd.encode('utf-8')
            print(hashed_password_bytes)    
            print(password.encode('utf-8'))
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password_bytes):
                alert = 'success'
                messages = "Login exitoso"
                return messages, alert
            else:
                alert = 'warning'
                messages = "Nombre de usuario o contraseña incorrectos. Por favor, inténtelo de nuevo." 
                return messages, alert
        else:
            alert = 'warning'
            messages = "Nombre de usuario o contraseña incorrectos. Por favor, inténtelo de nuevo." 
            return messages, alert, id

