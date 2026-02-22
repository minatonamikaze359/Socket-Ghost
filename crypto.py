from cryptography.fernet import Fernet

# In a real repo, the key should be managed securely
DEFAULT_KEY = Fernet.generate_key() 

def encrypt_payload(data, key=DEFAULT_KEY):
    f = Fernet(key)
    return f.encrypt(data.encode())

def decrypt_payload(token, key=DEFAULT_KEY):
    f = Fernet(key)
    return f.decrypt(token).decode()
