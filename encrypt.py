from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend 

#Read Public Key
def encrypt_data(data, pub_key):
    data = data.encode()
    with open(pub_key, "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend())

    encrypted = public_key.encrypt(data,padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None))

    with open('encrypted.txt', 'wb') as f:
        f.write(encrypted)

with open("message_in.txt","r") as f:
    data = f.read()

encrypt_data(data,"Keys/public_key.pem")


