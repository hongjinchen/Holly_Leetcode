from werkzeug.security import generate_password_hash

password = "123123123"
hashed_password = generate_password_hash(password)
print(hashed_password)