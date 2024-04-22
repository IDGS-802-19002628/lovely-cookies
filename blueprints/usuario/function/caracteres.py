import re

class VerificadorCaracteres:
   
    def es_segura(self, contraseña):
        tiene_mayuscula = any(c.isupper() for c in contraseña)
        tiene_minuscula = any(c.islower() for c in contraseña)
        tiene_numero = any(c.isdigit() for c in contraseña)
        tiene_especial = re.search(r'[!@#$%^&*()_+{}\[\]:;<>,.?\/\\-]', contraseña) is not None
        
        if not (tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_especial):
           messages = 'La contraseña debe contener al menos una mayúscula, una minúscula, un número y un carácter especial. [!@#$%^&*()_+{}\[\]:;<>,.?\/\\-]'
           return messages
        if None == None:
           pass
        

