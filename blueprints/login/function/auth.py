import bcrypt
from blueprints.usuario.model_usuario import Usuario

class Autenticador:
    def login(self, correo, password):
        print(correo)
        print(password)
        usuario_a_login = Usuario.query.filter_by(correo=correo).first()
        id = usuario_a_login.id
        
        if not usuario_a_login:
          print("No se encontro usuario")
          alert = 'warning'
          messages = "No se encontro el correo {} con el que intentas acceder".format(correo)
          return messages, alert, id
        
        if usuario_a_login:
            hashed_password_bytes = usuario_a_login.pwd.encode('utf-8')
            print(hashed_password_bytes)    
            print(password.encode('utf-8'))
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password_bytes):
                alert = 'success'
                messages = "Login exitoso"
                return messages, alert, id
            else:
                
                alert = 'warning'
                messages = "Nombre de usuario o contraseña incorrectos. Por favor, inténtelo de nuevo." 
                return messages, alert, id
        else:
            alert = 'warning'
            messages = "Nombre de usuario o contraseña incorrectos. Por favor, inténtelo de nuevo." 
            return messages, alert, id

