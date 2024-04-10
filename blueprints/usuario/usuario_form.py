from wtforms import Form
from wtforms import PasswordField, EmailField, StringField, RadioField, SelectField, IntegerField
from wtforms import validators

class UserForm(Form):
    id = IntegerField('id', [validators.number_range(min=1, max=20, message='valor no valido')])
    nombre = StringField("Nombre",[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=0, max=30, message="Ingresa contraseña valido")
    ])
    pwd = PasswordField("Contraseña",[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=0, max=150, message="Ingresa contraseña valido")
    ])
    correo = EmailField("Correo",[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=0, max=50, message="Ingresa correo valido")
    ])
    rol_choices = [('empleado', 'Empleado'),('administrador', 'Administrador'),  ('proveedor', 'Proveedor')]
    rol = SelectField("Rol", choices=rol_choices, validators=[validators.DataRequired(message='El campo es requerido')])
    estatus_choices = [('activo', 'Activo'),('inactivo', 'Inactivo')]
    estatus = SelectField("Estatus", choices=estatus_choices, validators=[validators.DataRequired(message='El campo es requerido')])