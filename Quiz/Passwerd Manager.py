master_pwd = input ('What is the master Password ??')


def view():
    pass

def add():
    name = input('Account Name:')

while True:
    mode = input('Would you like to add a new password or view an existing one (view/ add), press q to quit') lower.()
    if mode == 'q':
        break
    
    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else :
        print('Invalid Mode')
        continue