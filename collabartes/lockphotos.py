from cryptography.fernet import fernet
key = fernet.generate_key()
with open('key.key' , 'wb') as f:
    f.write(key)
    fernet = fernet(key)
    with open('your image', 'rb') as f:
        Photo = f.read()
lock = fernet.encrypt(Photo)
with open('your image', 'wb') as lock_photo:
    lock_photo.write(lock)
print("Your Photo Is Locked Bruuuuh") 