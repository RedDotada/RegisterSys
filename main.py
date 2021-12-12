import hashlib
Ver = False
#import and make user verifed
rlogin = open('login.txt', 'r')
readlogin = rlogin.readline()
#make or read file
def rl():
    global Ver
    if readlogin == '':
            passwordinput = input("Password:")
            passcode = passwordinput.encode('utf-8')
            password = hashlib.md5(passcode).hexdigest()
            #from password we make code password 
            loginw = open("login.txt", 'a')
            loginw.write(password)
            #make write a password 
            Ver = True
    else:
            passwordinput = input("Login:")
            passcode = passwordinput.encode('utf-8')
            password = hashlib.md5(passcode).hexdigest()
            if password == readlogin:
                print("Success!")
                Ver = True
            if password != readlogin:
                print("Not success!")
                Ver = False
            if passwordinput == str(readlogin):
                print("You a hecker!")
                Ver = Falsed
rl()

