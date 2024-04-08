from wtforms import Form
from wtforms import PasswordField, EmailField, StringField, RadioField, SelectField, BooleanField
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
    producto1 = BooleanField('Producto 1')
    producto2 = BooleanField('Producto 2')
    producto3 = BooleanField('Producto 3')
    producto4 = BooleanField('Producto 4')
    producto5 = BooleanField('Producto 5')
    producto6 = BooleanField('Producto 6')
    producto7 = BooleanField('Producto 7')
    producto8 = BooleanField('Producto 8')
    producto9 = BooleanField('Producto 9')
    producto10 = BooleanField('Producto 10')