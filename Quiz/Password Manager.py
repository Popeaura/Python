from cryptography.fernet import Fernet

# Function to write a key to a file (use this to generate the key initially)
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Function to load the encryption key
def load_key():
    try:
        with open("key.key", "rb") as file:
            key = file.read()
        return key
    except FileNotFoundError:
        print("Key file not found! Please generate a key using the 'write_key' function.")
        exit()

# Prompt user for master password
master_pwd = input('What is the master password? ').encode()

# Load the key and use the master password to derive the encryption key
base_key = load_key()
key = Fernet(base_key)  # Use only the base key for Fernet encryption
fer = Fernet(base_key)

# Function to view stored passwords
def view():
    try:
        with open('passwords.txt', 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                user, passw = data.split("|")
                decrypted_password = fer.decrypt(passw.encode()).decode()
                print(f"User: {user}, Password: {decrypted_password}\n")
    except FileNotFoundError:
        print("No passwords stored yet!")
    except ValueError:
        print("The file format is incorrect. Please check the file contents.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to add new passwords
def add():
    name = input('Account Name: ')
    pwd = input('Password: ')

    encrypted_password = fer.encrypt(pwd.encode()).decode()
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + encrypted_password + "\n")

# Main program loop
while True:
    mode = input('Would you like to add a new password or view existing ones? (view/add), press q to quit: ').lower()
    if mode == 'q':
        break
    
    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print('Invalid mode')
