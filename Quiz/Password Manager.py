from cryptography.fernet import Fernet

master_pwd = input('What is the master password? ')

def write_key():
    key = Fernet.generate_key()
    with open("key .key", "wb") as key_file:
        key_file.write(key)

def view():
    try:
        with open('passwords.txt', 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                user, passw = data.split("|")
                print("User:", user, ", Password:", passw)
    except FileNotFoundError:
        print("No passwords stored yet!")
    except ValueError:
        print("The file format is incorrect. Please check the file contents.")

def add():
    name = input('Account Name: ')
    pwd = input('Password: ')

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n")

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
