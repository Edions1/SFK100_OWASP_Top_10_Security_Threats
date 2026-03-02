import hashlib

texto = "Password1!"
print(repr(texto))
print(hashlib.md5(texto.encode()).hexdigest())
