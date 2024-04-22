from .lista_negra import insecure_passwords

class ValidadorContraseña:
    def validar(self, contraseña):
        if contraseña in insecure_passwords:
            messages = '¡La contraseña es débil! Por favor, elige una contraseña más segura.'
            print(messages)
            return messages
        
