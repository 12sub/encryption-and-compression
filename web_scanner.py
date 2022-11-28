from cryptography.fernet import Fernet
import gzip
import os

key = Fernet.generate_key()
def key_symmetry():
    global key
    with open('file.key', 'wb') as file:
        file.write(key)
    with open('file.key', 'rb') as file:
        key = file.read(key)


def encrypt(isert):
    fernet = Fernet(key)
    with open(isert, 'rb') as file:
        # os.popen(isert)
        origin = file.read()
    encrypt = fernet.encrypt(origin)
    with open(isert, 'wb') as encrypted:
        file_encrypt = encrypted.write(encrypt)
    file_compress = gzip.compress(bytes(file_encrypt))
    

def decrypt(isert):
    with open(isert, 'rb') as encrypt_file:
        encrypted = encrypt_file.read()
    decrypt = Fernet.decrypt(encrypted)
    with open(isert, 'wb') as decrypt_file:
        decrypt_file.write(decrypt)

# def compress(isert):
#     # data = b'Compressed file...'
#     # with gzip.open(isert, 'rb') as file:
#     #     file.read(isert)
#     # with gzip.open(isert, 'wb') as file:
#     #     file.write(isert)

#     file = gzip.compress(isert)


# key = key_symmetry()
isert = input('Select the file you want to Encrypt: ')
encrypt_info = encrypt(isert)
# decrypt_info = decrypt(isert)


