from werkzeug.security import generate_password_hash, check_password_hash
import bcrypt

contraseña_hasheada = generate_password_hash("12345", method='pbkdf2:sha256')
print(contraseña_hasheada)
pwd = "Angel12@"
salt = bcrypt.gensalt()
hash_pwd = bcrypt.hashpw(pwd.encode('utf-8'), salt)
print(hash_pwd)


if check_password_hash(contraseña_hasheada, "123456"):
    print("Identica")
else:
    print("Distinto")
