from cryptography.fernet import Fernet

"""
Fernet is an implementation of symmetric (also known as “secret key”) authenticated cryptography. 
"""

def generate_key():
    """
    Generate a random key using Fernet's generate_key.
    """
    return Fernet.generate_key()

def encrypt_message(
    message: str, 
    key: str
) -> str:
    """
    Given a message and a (Secret) key, encrypt the message using symmetryc key cryptography.
    """
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message

def decrypt_message(
    encrypted_message: str,
    key: str
) -> str:
    """
    Given a message and a (secret) key, decrypt the message using symmetryc key cryptography.
    """
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message).decode()
    return decrypted_message


