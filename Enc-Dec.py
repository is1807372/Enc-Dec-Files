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


def decrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(file_path, "wb") as file:
        file.write(decrypted_data)


def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        data = file.read()
    encrypted_data = fernet.encrypt(data)
    with open(file_path, "wb") as file:
        file.write(encrypted_data)

def process_files(directory, action):
    key = load_key()
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):  
            try:
                if action == "encrypt":
                    encrypt_file(file_path, key)
                    print(f"Encrypted: {file_path}")
                elif action == "decrypt":
                    decrypt_file(file_path, key)
                    print(f"Decrypted: {file_path}")
            except Exception as e:
                print(f"Error processing {file_path}: {e}")


