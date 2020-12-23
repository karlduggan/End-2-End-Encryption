import os
from cryptography.hazmat.primitives import serialization 
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend 

# Generating Private and public keys 
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
# Get the public key that links to the private key 
public_key = private_key.public_key()

pem_private = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

pem_public = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)
# Create a directory Keys where we will save our Private and public keys
path = os.getcwd() + "/Keys"
try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s " % path)

# Save the two generated keys
with open(path + '/private_key.pem', 'wb') as f:
    f.write(pem_private)

with open(path + '/public_key.pem', 'wb') as f:
    f.write(pem_public)

