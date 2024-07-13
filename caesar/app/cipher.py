import random
import string


def generate_random_key():
    """Generate a random substitution cipher key."""
    letters = list(string.ascii_lowercase)
    random.shuffle(letters)
    return ''.join(letters)

def validate_key(key):
    """Validate that the key is a valid substitution cipher key."""
    if len(key) != 26:
        raise ValueError("Key must contain exactly 26 letters.")
    if not key.isalpha():
        raise ValueError("Key must only contain alphabetic characters.")
    if len(set(key)) != 26:
        raise ValueError("Key must not contain duplicate letters.")

def encrypt(text, key):
    """Encrypt plaintext using the substitution cipher."""
    validate_key(key)
    text = text.lower()
    encrypted_text = []
    for char in text:
        if char.isalpha():
            encrypted_text.append(key[ord(char) - ord('a')])
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)

def decrypt(text, key):
    inv_key_map = {key[i]: chr(i + ord('a')) for i in range(26)}
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                decrypted_text += inv_key_map[char]
            else:
                decrypted_text += inv_key_map[char.lower()].upper()
        else:
            decrypted_text += char
    return decrypted_text

