from wtforms import Form
from wtforms import PasswordField, EmailField
from wtforms import validators

class loginForm(Form):
    pwd = PasswordField("",[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=0, max=30, message="Ingresa contraseña valido")
    ])
    correo = EmailField("",[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=0, max=50, message="Ingresa correo valido")])
    
    