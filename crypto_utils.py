#Encryption utilities

import base64
import hashlib
from cryptography.fernet import Fernet

#3.1 Generate an encryption key from master password
def generate_key(master_password: str) -> bytes:
    hash_digest = hashlib.sha256(master_password.encode()).digest()
    key = base64.urlsafe_b64encode(hash_digest)
    return key

#3.2 Encrypt a password
def encrypt_password(password: str, key: bytes) -> str:
    fernet = Fernet(key)
    encrypted = fernet.encrypt(password.encode())
    return encrypted.decode()

#3.3 Decrypt a password
def decrypt_password(encrypted_password: str, key: bytes) -> str:
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_password.encode())
    return decrypted.decode()
