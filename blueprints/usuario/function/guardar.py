from flask import flash
import bcrypt
from ..model_usuario import Usuario, db_usuario


class GestorUsuario:
    def guardar_usuario(self, form_user):
        nombre = form_user.nombre.data
        pwd = form_user.pwd.data
        correo = form_user.correo.data
        rol = form_user.rol.data
        salt = bcrypt.gensalt()
        hash_pwd = bcrypt.hashpw(pwd.encode('utf-8'), salt)
        nuevo_usuario = Usuario(nombre=nombre,
                                pwd=hash_pwd,
                                correo=correo,
                                rol=rol,
                                estatus="activo")
        db_usuario.session.add(nuevo_usuario)
        db_usuario.session.commit()
        messages = "Se a creado un nuevo usuario"
        return messages
    def obtener_usuarios(self, estatus):
         b = Usuario.query.filter_by(estatus = estatus).all()
         return b
    def eliminar_usuario(self, id_usuario):
         usuario_a_eliminar = Usuario.query.filter_by(id=id_usuario).first()
         db_usuario.session.delete(usuario_a_eliminar)
         db_usuario.session.commit()
         messages = "Se a eliminado el usuario {}".format(usuario_a_eliminar.nombre)
         return messages
    def modificar_usuario(self, id_usuario, form_usuario, method):
         print('method ', method)
         print('id prueba', id_usuario)
         usuario_a_modificar = {}
         id = 0
         if method == 'GET':
           usuario_a_modificar = Usuario.query.filter(Usuario.id == id_usuario).first()
           form_usuario.id.data = usuario_a_modificar.id
           form_usuario.nombre.data = usuario_a_modificar.nombre
           form_usuario.pwd.data = usuario_a_modificar.pwd
           form_usuario.correo.data = usuario_a_modificar.correo
           form_usuario.rol.data = usuario_a_modificar.rol
         print("cargando datos en form", form_usuario.pwd.data)
         if method == 'POST':
           id = form_usuario.id.data
           print('id form post', id)
           usuario_a_modificar = Usuario.query.filter(Usuario.id == id_usuario).first()
           usuario_a_modificar.nombre = form_usuario.nombre.data
           usuario_a_modificar.correo = form_usuario.correo.data
           usuario_a_modificar.rol = form_usuario.rol.data 
         messages = "Se a actualizado el usuario {}".format(usuario_a_modificar.nombre)
         return messages, form_usuario