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


def select_directory(action):
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        try:
            process_files(folder_selected, action)
            messagebox.showinfo("Success", f"Files have been {action}ed successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showwarning("Warning", "No directory selected!")



def main():
    root = tk.Tk()
    root.title("File Encryption/Decryption Tool")

    root.geometry("400x200")

    label = tk.Label(root, text="Encrypt/Decrypt Files in Directory", font=("Arial", 14))
    label.pack(pady=20)

    encrypt_button = tk.Button(root, text="Encrypt Files", width=20, command=lambda: select_directory("encrypt"))
    encrypt_button.pack(pady=10)

    decrypt_button = tk.Button(root, text="Decrypt Files", width=20, command=lambda: select_directory("decrypt"))
    decrypt_button.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    generate_key() 
    main()  



