from itsdangerous import URLSafeSerializer

class ConnectionEncryptor:

    def __init__(self, secret_key):
        self.serializer = URLSafeSerializer(secret_key)

    def encriptar(self, connection_string):
        return self.serializer.dumps(connection_string)

    def desencriptar(self, encrypted_connection_string):
        return self.serializer.loads(encrypted_connection_string)


SECRET_KEY = 'Jz4wT#Lc9R@!xFqG'

encrptador = ConnectionEncryptor('Jz4wT#Lc9R@!xFqG')

conexion = 'mysql+pymysql://admin:Guanajuato2001@127.0.0.1/lovely_cookies'

encrptardor = encrptador.encriptar(conexion)

desencriptador = encrptador.desencriptar(encrptardor)

