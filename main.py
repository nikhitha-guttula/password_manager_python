#Password Manager

#A local password manager that can:
#Ask the user for a master password
#Encrypt passwords before saving them to a file
#Decrypt them only when the correct master password is provided
#Store data safely on disk
#Use real encryption (Fernet / AES under the hood)

import json
import os
import hashlib
from crypto_utils import generate_key, encrypt_password, decrypt_password


#Master password setup
MASTER_FILE = "master.hash"
STORAGE_FILE = "storage.json"

def set_master_password():
    master = input("Set master password: ")
    confirm = input("Confirm master password: ")

    if master != confirm:
        print("Passwords do not match.")
        return None

    hashed = hashlib.sha256(master.encode()).hexdigest()

    with open(MASTER_FILE, "w") as f:
        f.write(hashed)

    print("Master password set.")
    return master  


#Verify master password
def verify_master_password():
    if not os.path.exists(MASTER_FILE):
        return set_master_password()

    entered = input("Enter master password: ")
    entered_hash = hashlib.sha256(entered.encode()).hexdigest()

    with open(MASTER_FILE, "r") as f:
        saved_hash = f.read()

    if entered_hash == saved_hash:
        return entered
    else:
        print("Incorrect master password.")
        return None

#Add a new password
def add_password(key):
    service = input("Service name: ")
    username = input("Username: ")
    password = input("Password: ")

    encrypted_pw = encrypt_password(password, key)

    data = {}
    if os.path.exists(STORAGE_FILE):
        with open(STORAGE_FILE, "r") as f:
            data = json.load(f)

    data[service] = {
        "username": username,
        "password": encrypted_pw
    }

    with open(STORAGE_FILE, "w") as f:
        json.dump(data, f, indent=4)

    print("Password saved securely.")

#Retrieve a password
def get_password(key):
    service = input("Service name to retrieve: ")

    if not os.path.exists(STORAGE_FILE):
        print("No passwords saved.")
        return

    with open(STORAGE_FILE, "r") as f:
        data = json.load(f)

    if service not in data:
        print("Service not found.")
        return

    decrypted_pw = decrypt_password(data[service]["password"], key)

    print(f"Username: {data[service]['username']}")
    print(f"Password: {decrypted_pw}")

#Main program loop
def main():
    master_password = verify_master_password()
    if not master_password:
        return

    key = generate_key(master_password)

    while True:
        print("\n1. Add password")
        print("2. Get password")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_password(key)
        elif choice == "2":
            get_password(key)
        elif choice == "3":
            break
        else:
            print("Invalid choice.")
if __name__ == "__main__":
    main()
    
