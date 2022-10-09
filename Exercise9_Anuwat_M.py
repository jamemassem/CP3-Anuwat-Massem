username =  ''
password =  ''

while True: 
    username = input('username : ') 
    password = input('password : ') 
    if username!='jamemassem' or password!='123456789':
        print('Your username or password is not correct, please try again.') 
    elif username=='jamemassem' and password=='123456789': 
        break

print('Login Success!!!')