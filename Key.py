import os
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import filedialog, messagebox


def generate_key():
    if not os.path.exists("secret.key"):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
        print("Encryption key saved as 'secret.key'. Keep this safe!")
    else:
        print("Key already exists, skipping key generation.")