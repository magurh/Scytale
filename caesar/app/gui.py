import tkinter as tk
from tkinter import messagebox, scrolledtext
from caesar.app.cipher import generate_random_key, validate_key, encrypt, decrypt, frequency_analysis

class CipherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Caesar")
        self.root.configure(bg="light blue")  # Set background color of the root window

        # Key Input Section
        self.key_label = tk.Label(root, text="Key:", bg="light blue")
        self.key_label.grid(row=0, column=0, sticky="w")
        
        self.key_entry = tk.Entry(root, width=40)
        self.key_entry.grid(row=0, column=1, sticky="ew")

        self.insert_key_button = tk.Button(root, text="Insert Key", command=self.toggle_insert_key, width=15, bg="light blue")
        self.insert_key_button.grid(row=0, column=2)

        self.generate_key_button = tk.Button(root, text="Generate Key", command=self.toggle_generate_key, width=15, bg="light blue")
        self.generate_key_button.grid(row=0, column=3)
        
        self.insert_key = True
        self.insert_key_button.config(relief=tk.SUNKEN)
        
        # Text Input
        self.text_label = tk.Label(root, text="Input Text:", bg="light blue")
        self.text_label.grid(row=1, column=0, sticky="w")
        
        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10)
        self.text_area.grid(row=2, column=0, columnspan=4, sticky="ew")

        # Buttons for Actions
        self.encrypt_button = tk.Button(root, text="Encrypt", command=self.encrypt_text, width=15, bg="light blue")
        self.encrypt_button.grid(row=3, column=0, sticky="ew")

        self.decrypt_button = tk.Button(root, text="Decrypt", command=self.decrypt_text, width=15, bg="light blue")
        self.decrypt_button.grid(row=3, column=1, sticky="ew")

        self.freq_analysis_button = tk.Button(root, text="Decrypt by Frequency", command=self.freq_analysis, width=20, bg="light blue")
        self.freq_analysis_button.grid(row=3, column=2, sticky="ew")

        # Result Display
        self.result_label = tk.Label(root, text="Result:", bg="light blue")
        self.result_label.grid(row=4, column=0, sticky="w")
        
        self.result_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10)
        self.result_area.grid(row=5, column=0, columnspan=4, sticky="ew")

        # Set initial button states
        self.encrypt_button.config(bg="light blue")
        self.decrypt_button.config(bg="light blue")
        self.freq_analysis_button.config(bg="light blue")

    def toggle_insert_key(self):
        self.insert_key = True
        self.insert_key_button.config(relief=tk.SUNKEN)
        self.generate_key_button.config(relief=tk.RAISED)

    def toggle_generate_key(self):
        self.insert_key = False
        self.insert_key_button.config(relief=tk.RAISED)
        self.generate_key_button.config(relief=tk.SUNKEN)
        self.generate_random_key()

    def generate_random_key(self):
        key = generate_random_key()
        self.key_entry.delete(0, tk.END)
        self.key_entry.insert(0, key)

    def encrypt_text(self):
        self.encrypt_button.config(relief=tk.SUNKEN, bg="red")
        self.decrypt_button.config(relief=tk.RAISED, bg="light blue")
        self.freq_analysis_button.config(relief=tk.RAISED, bg="light blue")

        text = self.text_area.get("1.0", tk.END).strip()
        key = self.key_entry.get().strip()

        if self.insert_key and not key:
            messagebox.showerror("Invalid Key", "Please insert a key or generate one.")
            return

        try:
            validate_key(key)
            encrypted_text = encrypt(text, key)
            self.result_area.delete("1.0", tk.END)
            self.result_area.insert(tk.END, encrypted_text)
        except ValueError as e:
            messagebox.showerror("Invalid Key", str(e))

    def decrypt_text(self):
        self.encrypt_button.config(relief=tk.RAISED, bg="light blue")
        self.decrypt_button.config(relief=tk.SUNKEN, bg="green")
        self.freq_analysis_button.config(relief=tk.RAISED, bg="light blue")

        text = self.text_area.get("1.0", tk.END).strip()
        key = self.key_entry.get().strip()

        try:
            validate_key(key)
            decrypted_text = decrypt(text, key)
            self.result_area.delete("1.0", tk.END)
            self.result_area.insert(tk.END, decrypted_text)
        except ValueError as e:
            messagebox.showerror("Invalid Key", str(e))

    def freq_analysis(self):
        self.encrypt_button.config(relief=tk.RAISED, bg="light blue")
        self.decrypt_button.config(relief=tk.RAISED, bg="light blue")
        self.freq_analysis_button.config(relief=tk.SUNKEN, bg="green")

        text = self.text_area.get("1.0", tk.END).strip()
        guessed_text, guessed_key = frequency_analysis(text)
        self.result_area.delete("1.0", tk.END)
        self.result_area.insert(tk.END, f"Guessed Key: {guessed_key}\nDecrypted Text:\n{guessed_text}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CipherApp(root)
    root.mainloop()
