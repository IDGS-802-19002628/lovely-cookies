from werkzeug.security import generate_password_hash

contraseña_hasheada = generate_password_hash("12345", method='pbkdf2:sha256')
print(contraseña_hasheada)