from cryptography.fernet import Fernet

# Function to generate the encryption key
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Function to load the encryption key
def load_key():
    try:
        with open("key.key", "rb") as key_file:
            key = key_file.read()
        return key
    except FileNotFoundError:
        print("Key file not found! Please run the 'write_key()' function to generate the key.")
        exit()

# Generate the encryption object using the key and master password
def get_fernet(master_pwd):
    key = load_key()
    full_key = key + master_pwd.encode()
    try:
        return Fernet(full_key[:32])  # Fernet key must be exactly 32 bytes
    except ValueError:
        print("Invalid master password or key.")
        exit()

# Functions for viewing and adding passwords
def view(fer):
    try:
        with open('passwords.txt', 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                user, passw = data.split("|")
                decrypted_pwd = fer.decrypt(passw.encode()).decode()
                print(f"User: {user}, Password: {decrypted_pwd}")
    except FileNotFoundError:
        print("No passwords stored yet!")
    except ValueError:
        print("The file format is incorrect. Please check the file contents.")

def add(fer):
    name = input("Account Name: ")
    pwd = input("Password: ")
    encrypted_pwd = fer.encrypt(pwd.encode()).decode()

    with open('passwords.txt', 'a') as f:
        f.write(f"{name}|{encrypted_pwd}\n")
    print("Password saved successfully.")

# Main logic for interacting with the program
def main():
    print("Welcome to the Password Manager!")
    
    master_pwd = input("What is the master password? ")
    fer = get_fernet(master_pwd)

    while True:
        mode = input("Would you like to add a new password or view existing ones? (view/add), press q to quit: ").lower()
        if mode == 'q':
            print("Goodbye!")
            break
        elif mode == 'view':
            view(fer)
        elif mode == 'add':
            add(fer)
        else:
            print("Invalid mode. Please choose 'view', 'add', or 'q'.")

# Uncomment the next line to generate the key file (only do this once!)
# write_key()

if __name__ == "__main__":
    main()
