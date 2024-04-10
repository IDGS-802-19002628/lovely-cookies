import bcrypt
from ..model_usuario import Usuario, db
from .validar_pwd import ValidadorContraseña
from .caracteres import VerificadorCaracteres

class GestorUsuario:
    def guardar_usuario(self, form_user):
        nombre = form_user.nombre.data
        pwd = form_user.pwd.data
        correo = form_user.correo.data
        rol = form_user.rol.data
        validacion = ValidadorContraseña().validar(pwd)
        if validacion:
          alert = 'warning'
          return validacion, alert
        caracteres = VerificadorCaracteres().es_segura(pwd)
        
        if caracteres:
          alert = 'warning'
          return caracteres, alert
        
        
        salt = bcrypt.gensalt()
        hash_pwd = bcrypt.hashpw(pwd.encode('utf-8'), salt)
        nuevo_usuario = Usuario(nombre=nombre,
                                pwd=hash_pwd,
                                correo=correo,
                                rol=rol,
                                estatus="activo")
        db.session.add(nuevo_usuario)
        db.session.commit()
        messages = "Se a creado un nuevo usuario"
        alert = 'success'
        return messages, alert
    def obtener_usuarios(self):
         b = Usuario.query.all()
         return b
    def eliminar_usuario(self, id_usuario):
         alert = 'success'
         usuario_a_eliminar = Usuario.query.filter_by(id=id_usuario).first()
         usuario_a_eliminar.estatus = "inactivo"
         db.session.add(usuario_a_eliminar)
         db.session.commit()
         messages = "La cuenta del usuario {} se a desactivado".format(usuario_a_eliminar.nombre)
         return messages, alert
    def modificar_usuario(self, id_usuario, form_usuario, method):
         pwd = form_usuario.pwd.data
         print('pass desde form {}'.format(pwd))
         usuario_a_modificar = {}
         id = 0
         if method == 'GET':
           usuario_a_modificar = Usuario.query.filter(Usuario.id == id_usuario).first()
           form_usuario.id.data = usuario_a_modificar.id
           form_usuario.nombre.data = usuario_a_modificar.nombre
           form_usuario.pwd.data = usuario_a_modificar.pwd
           form_usuario.correo.data = usuario_a_modificar.correo
           form_usuario.rol.data = usuario_a_modificar.rol
           form_usuario.estatus.data = usuario_a_modificar.estatus
         print("cargando datos en form", form_usuario.pwd.data)
         if method == 'POST':
           id = form_usuario.id.data
           usuario_a_modificar = Usuario.query.filter(Usuario.id == id).first()
           if not form_usuario.pwd.data:
             usuario_a_modificar.nombre = form_usuario.nombre.data
             usuario_a_modificar.correo = form_usuario.correo.data
             usuario_a_modificar.rol = form_usuario.rol.data
             usuario_a_modificar.estatus = form_usuario.estatus.data
           else:
             usuario_a_modificar.nombre = form_usuario.nombre.data
             usuario_a_modificar.correo = form_usuario.correo.data
             validacion = ValidadorContraseña().validar(pwd)
             if validacion:
               alert = 'warning'
               return validacion, alert
             caracteres = VerificadorCaracteres().es_segura(pwd)
             if caracteres:
               alert = 'warning'
               return caracteres, alert
             salt = bcrypt.gensalt()
             hash_pwd = bcrypt.hashpw(pwd.encode('utf-8'), salt)
             usuario_a_modificar.pwd = hash_pwd
             usuario_a_modificar.rol = form_usuario.rol.data
             usuario_a_modificar.estatus = form_usuario.estatus.data
           db.session.add(usuario_a_modificar)
           db.session.commit()
         alert = 'success' 
         messages = "Se a actualizado el usuario {}".format(usuario_a_modificar.nombre)
         return messages, form_usuario, alert