from wtforms import Form
from wtforms import PasswordField, EmailField, StringField, RadioField, SelectField
from wtforms import validators

class ProvvedorForm(Form):
    nombre_em = StringField("Nombre Empresa",[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=0, max=30, message="Ingresa contraseña valido")
    ])
    direccion = StringField("Dirección",[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=0, max=30, message="Ingresa contraseña valido")
    ])
    Telefono = StringField("Teléfono",[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=0, max=30, message="Ingresa contraseña valido")
    ])
    nombre_e = StringField("Nombre Empleado",[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=0, max=30, message="Ingresa contraseña valido")
    ])