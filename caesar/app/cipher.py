import random
import string

# Frequency of letters in English language (in percentage)
ENGLISH_FREQ = {
    'a': 8.167, 'b': 1.492, 'c': 2.782, 'd': 4.253, 'e': 12.702, 'f': 2.228, 'g': 2.015,
    'h': 6.094, 'i': 6.966, 'j': 0.153, 'k': 0.772, 'l': 4.025, 'm': 2.406, 'n': 6.749,
    'o': 7.507, 'p': 1.929, 'q': 0.095, 'r': 5.987, 's': 6.327, 't': 9.056, 'u': 2.758,
    'v': 0.978, 'w': 2.360, 'x': 0.150, 'y': 1.974, 'z': 0.074
}

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
    """Decrypt ciphertext using the substitution cipher."""
    validate_key(key)
    decrypted_text = []
    reverse_key = {key[i]: chr(i + ord('a')) for i in range(26)}
    for char in text:
        if char.isalpha():
            decrypted_text.append(reverse_key[char])
        else:
            decrypted_text.append(char)
    return ''.join(decrypted_text)

def frequency_analysis(text):
    """Perform frequency analysis on the ciphertext."""
    letter_counts = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
    total_letters = 0
    for char in text.lower():
        if char.isalpha():
            letter_counts[char] += 1
            total_letters += 1
    
    text_freq = {char: (count / total_letters) * 100 for char, count in letter_counts.items()}
    sorted_text_freq = sorted(text_freq.items(), key=lambda x: x[1], reverse=True)
    sorted_english_freq = sorted(ENGLISH_FREQ.items(), key=lambda x: x[1], reverse=True)
    
    guessed_key = [''] * 26
    for i in range(26):
        guessed_key[ord(sorted_text_freq[i][0]) - ord('a')] = sorted_english_freq[i][0]
    
    guessed_key_str = ''.join(guessed_key)
    guessed_text = decrypt(text, guessed_key_str)
    
    return guessed_text, guessed_key_str
