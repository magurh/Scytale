"""
Graphical User Interface using tkinter using Tkinter.
"""

import tkinter as tk
from tkinter import messagebox
from app.encryption import generate_key, encrypt_message, decrypt_message

class EncryptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Encryption App")

        self.key = None

        self.label = tk.Label(root, text="Enter message:")
        self.label.pack()

        self.entry = tk.Entry(root, width=50)
        self.entry.pack()

        self.encrypt_button = tk.Button(root, text="Encrypt", command=self.encrypt)
        self.encrypt_button.pack()

        self.decrypt_button = tk.Button(root, text="Decrypt", command=self.decrypt)
        self.decrypt_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def encrypt(self):
        message = self.entry.get()
        if not self.key:
            self.key = generate_key()
        encrypted_message = encrypt_message(message, self.key)
        self.result_label.config(text=encrypted_message)
        self.entry.delete(0, tk.END)

    def decrypt(self):
        encrypted_message = self.entry.get()
        if not self.key:
            messagebox.showerror("Error", "No key found!")
            return
        try:
            decrypted_message = decrypt_message(encrypted_message.encode(), self.key)
            self.result_label.config(text=decrypted_message)
        except Exception as e:
            messagebox.showerror("Error", str(e))
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = EncryptionApp(root)
    root.mainloop()
