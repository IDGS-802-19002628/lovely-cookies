from werkzeug.security import generate_password_hash, check_password_hash
import bcrypt
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from blueprints.venta.model_venta import Galleta
""" contraseña_hasheada = generate_password_hash("12345", method='pbkdf2:sha256')
print(contraseña_hasheada)
pwd = "Angel12@"
salt = bcrypt.gensalt()
hash_pwd = bcrypt.hashpw(pwd.encode('utf-8'), salt)
print(hash_pwd)


if check_password_hash(contraseña_hasheada, "123456"):
    print("Identica")
else:
    print("Distinto")
 """

import io

ruta_imagen1 = "C:/Users/franc/Desktop/Lovely Cookies/lovely-cookies/static/img/Galletas/chocoMenta.jfif"

# Lee la imagen en modo binario
with open(ruta_imagen1, "rb") as file:
    # Lee los bytes de la imagen
    bytes_imagen1 = file.read()
    print(bytes_imagen1)

ruta_imagen2 = "C:/Users/franc/Desktop/Lovely Cookies/lovely-cookies/static/img/Galletas/avenaNues.jfif"

# Lee la imagen en modo binario
with open(ruta_imagen2, "rb") as file:
    # Lee los bytes de la imagen
    bytes_imagen2 = file.read()
    print(bytes_imagen2)

ruta_imagen3 = "C:/Users/franc/Desktop/Lovely Cookies/lovely-cookies/static/img/Galletas/limon.jfif"

# Lee la imagen en modo binario
with open(ruta_imagen3, "rb") as file:
    # Lee los bytes de la imagen
    bytes_imagen3 = file.read()
    print(bytes_imagen3)

ruta_imagen4 = "C:/Users/franc/Desktop/Lovely Cookies/lovely-cookies/static/img/Galletas/coco.jfif"

# Lee la imagen en modo binario
with open(ruta_imagen4, "rb") as file:
    # Lee los bytes de la imagen
    bytes_imagen4 = file.read()
    print(bytes_imagen4)

ruta_imagen5 = "C:/Users/franc/Desktop/Lovely Cookies/lovely-cookies/static/img/Galletas/descargar.jfif"

# Lee la imagen en modo binario
with open(ruta_imagen5, "rb") as file:
    # Lee los bytes de la imagen
    bytes_imagen5 = file.read()
    print(bytes_imagen5)

ruta_imagen6 = "C:/Users/franc/Desktop/Lovely Cookies/lovely-cookies/static/img/Galletas/almendra.jfif"

# Lee la imagen en modo binario
with open(ruta_imagen6, "rb") as file:
    # Lee los bytes de la imagen
    bytes_imagen6 = file.read()
    print(bytes_imagen6)

ruta_imagen7 = "C:/Users/franc/Desktop/Lovely Cookies/lovely-cookies/static/img/Galletas/mantequillaMani.jfif"

# Lee la imagen en modo binario
with open(ruta_imagen7, "rb") as file:
    # Lee los bytes de la imagen
    bytes_imagen7 = file.read()
    print(bytes_imagen7)

ruta_imagen8 = "C:/Users/franc/Desktop/Lovely Cookies/lovely-cookies/static/img/Galletas/chiaCoco.jfif"

# Lee la imagen en modo binario
with open(ruta_imagen8, "rb") as file:
    # Lee los bytes de la imagen
    bytes_imagen8 = file.read()
    print(bytes_imagen8)

ruta_imagen9 = "C:/Users/franc/Desktop/Lovely Cookies/lovely-cookies/static/img/Galletas/almendraNaranja.jfif"

# Lee la imagen en modo binario
with open(ruta_imagen9, "rb") as file:
    # Lee los bytes de la imagen
    bytes_imagen9 = file.read()
    print(bytes_imagen9)

ruta_imagen10 = "C:/Users/franc/Desktop/Lovely Cookies/lovely-cookies/static/img/Galletas/maiz.jpg"

# Lee la imagen en modo binario
with open(ruta_imagen10, "rb") as file:
    # Lee los bytes de la imagen
    bytes_imagen10 = file.read()
    print(bytes_imagen10)

import pymysql

# Configuración de la conexión a la base de datos
host = '127.0.0.1'  # Dirección del servidor (localhost o la dirección IP del servidor de la base de datos)
user = 'root'  # Nombre de usuario de la base de datos
password = '12345'  # Contraseña del usuario de la base de datos
database = 'don_galleto'  # Nombre de la base de datos a la que te conectas

# Conéctate a la base de datos
connection = pymysql.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

try:
    # Crea un cursor para ejecutar consultas
    cursor = connection.cursor()

    # Consulta SQL para insertar datos en la base de datos
    sql = """
    INSERT INTO Galleta (imagen, nombre, descripcion, precio, peso)
    VALUES (%s, %s, %s, %s, %s)
    """

    galletas_datos = [
        {'imagen': str(bytes_imagen10), 'nombre': 'Galletas de maíz', 'descripcion': 'Crunchy galletas con sabor a maíz', 'precio': 2.1, 'peso': 46.0}
    ]
    """ {'imagen': str(bytes_imagen1), 'nombre': 'Galletas de chocolate y menta', 'descripcion': 'Deliciosas galletas de chocolate con sabor a menta', 'precio': 2.5, 'peso': 50.0},
    {'imagen': str(bytes_imagen2), 'nombre': 'Galletas de avena y nueces', 'descripcion': 'Galletas nutritivas de avena con trozos de nueces', 'precio': 2.0, 'peso': 45.0},
    {'imagen': str(bytes_imagen3), 'nombre': 'Galletas de limón', 'descripcion': 'Refrescantes galletas con un toque de limón', 'precio': 2.2, 'peso': 48.0},
    {'imagen': str(bytes_imagen4), 'nombre': 'Galletas de coco', 'descripcion': 'Irresistibles galletas con sabor a coco', 'precio': 2.3, 'peso': 47.0},
    {'imagen': str(bytes_imagen5), 'nombre': 'Galletas de chocolate blanco y arándanos', 'descripcion': 'Galletas con trozos de chocolate blanco y arándanos', 'precio': 2.8, 'peso': 55.0},
    {'imagen': str(bytes_imagen6), 'nombre': 'Galletas de almendra', 'descripcion': 'Deliciosas galletas con trozos de almendra', 'precio': 2.4, 'peso': 50.0},
    {'imagen': str(bytes_imagen7), 'nombre': 'Galletas de mantequilla de maní', 'descripcion': 'Suaves galletas con sabor a mantequilla de maní', 'precio': 2.6, 'peso': 52.0},
    {'imagen': str(bytes_imagen8), 'nombre': 'Galletas de chía y coco', 'descripcion': 'Galletas saludables con semillas de chía y coco rallado', 'precio': 2.2, 'peso': 49.0},
    {'imagen': str(bytes_imagen9), 'nombre': 'Galletas de almendra y naranja', 'descripcion': 'Galletas con un toque cítrico de naranja y almendra', 'precio': 2.5, 'peso': 51.0}, """
    

    galletas_datos_tuplas = [(datos['imagen'], datos['nombre'], datos['descripcion'], datos['precio'], datos['peso']) 
                        for datos in galletas_datos]
    
    # Ejecuta la consulta para cada fila de datos
    cursor.executemany(sql, galletas_datos_tuplas)

    # Confirma la transacción
    connection.commit()

except pymysql.MySQLError as e:
    # En caso de error, imprime el mensaje de error
    print(f"Error al insertar datos: {e}")
    # Puedes revertir la transacción si es necesario
    connection.rollback()

finally:
    # Cierra el cursor y la conexión
    cursor.close()
    connection.close()
