from werkzeug.security import generate_password_hash, check_password_hash
from Models import MateriaP

contraseña_hasheada = generate_password_hash("12345", method='pbkdf2:sha256')
print(contraseña_hasheada)

if check_password_hash(contraseña_hasheada, "123456"):
    print("Identica")
else:
    print("Distinto")
