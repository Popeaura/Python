master_pwd = input('What is the master Password ??')

def view():
      with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("user:", user, ", Password:", passw)


def add():
    name = input('Account Name:')
    pwd = input('Password:')

    with open('passwords.txt', 'a') as f:
        f.write(name + "" + pwd + "\n" )

while True:
    mode = input('Would you like to add a new password or view an existing one (view/add), press q to quit').lower()
    if mode == 'q':
        break
    
    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print('Invalid Mode')
        continue
