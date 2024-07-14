# Enigma

Enigma uses the `cryptography` module, based on Fernet symmetric encryption. Fernet is built on top of a number of standard cryptographic primitives:

- Advanced Encryption Standard (AES) in Cipher Block Chaining (CBC) mode with a 128-bit key for encryption; using PKCS7 padding.
- Hash-Based Message Authentication (HMAC) using SHA256 cryptographic hash function.


### Setup
---------------------------------------------------

1. Set path for python, on windows:
```
set PYTHONPATH=..
```
while on MacOS or Linux:
```
export PYTHONPATH=..
```

2. Run app:

```
python app/gui.py
```

3. To build a standalone executable:

```
pyinstaller --onefile -w app/gui.py
```

For this, you may need to temporarily disable the antivirus.



