from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend 

#Read Private Key
def decrypt_data(data, priv_key):
    with open(data, 'rb') as f:
        encrypted = f.read()

    with open(priv_key, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend())

    decrypted = private_key.decrypt(encrypted,padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None))
    return(decrypted.decode())


print(decrypt_data('encrypted.txt', "private_key.pem"))

