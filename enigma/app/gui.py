"""
Graphical User Interface using tkinter using Tkinter.
"""
import tkinter as tk
from tkinter import messagebox
from enigma.app.encryption import generate_key, encrypt_message, decrypt_message
import base64
import os

class EncryptorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Enigma")

        # Set background color for the main window
        self.root.configure(bg='lightblue')

        self.create_widgets()

    def create_widgets(self):
        # Key toggle
        self.key_var = tk.StringVar()
        self.key_mode = tk.BooleanVar(value=False)  # Default to "Insert Key"

        self.key_label = tk.Label(self.root, text="Encryption Key", bg='lightblue')
        self.key_label.grid(row=0, column=0, padx=10, pady=10)

        self.key_entry = tk.Entry(self.root, textvariable=self.key_var, width=50)
        self.key_entry.grid(row=0, column=1, padx=10, pady=10)

        self.key_toggle = tk.Checkbutton(self.root, text="Generate Key", variable=self.key_mode, command=self.toggle_key_mode)
        self.key_toggle.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Action buttons
        self.action_var = tk.StringVar(value="encrypt")

        self.encrypt_button = tk.Radiobutton(self.root, text="Encrypt", variable=self.action_var, value="encrypt", indicatoron=0, width=20, command=self.toggle_action, bg='lightgreen')
        self.encrypt_button.grid(row=2, column=0, padx=10, pady=10)

        self.decrypt_button = tk.Radiobutton(self.root, text="Decrypt", variable=self.action_var, value="decrypt", indicatoron=0, width=20, command=self.toggle_action, bg='lightcoral')
        self.decrypt_button.grid(row=2, column=1, padx=10, pady=10)

        self.input_label = tk.Label(self.root, text="Input Text", bg='lightblue')
        self.input_label.grid(row=3, column=0, padx=10, pady=10)

        self.input_text = tk.Text(self.root, height=10, width=50)
        self.input_text.grid(row=3, column=1, padx=10, pady=10)

        self.result_label = tk.Label(self.root, text="Result Text", bg='lightblue')
        self.result_label.grid(row=4, column=0, padx=10, pady=10)

        self.result_text = tk.Text(self.root, height=10, width=50)
        self.result_text.grid(row=4, column=1, padx=10, pady=10)

        self.process_button = tk.Button(self.root, text="Process", command=self.process_text, bg='lightyellow')
        self.process_button.grid(row=5, column=0, columnspan=2, pady=10)

    def toggle_key_mode(self):
        if self.key_mode.get():
            key = generate_key()
            self.key_var.set(key.decode())
            self.key_entry.configure(state='readonly')
            self.key_toggle.config(text="Insert Key")
        else:
            self.key_var.set("")
            self.key_entry.configure(state='normal')
            self.key_toggle.config(text="Generate Key")

    def toggle_action(self):
        pass  # No additional actions needed for now, Radiobuttons handle toggling

    def process_text(self):
        key = self.key_var.get().encode()
        input_text = self.input_text.get("1.0", tk.END).strip()

        if self.action_var.get() == "encrypt":
            encrypted_text = encrypt_message(input_text, key).decode()
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, encrypted_text)
        elif self.action_var.get() == "decrypt":
            try:
                decrypted_text = decrypt_message(input_text, key)
                self.result_text.delete("1.0", tk.END)
                self.result_text.insert(tk.END, decrypted_text)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to decrypt: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = EncryptorApp(root)
    root.mainloop()




