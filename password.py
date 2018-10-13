password = raw_input('Enter password: ')
if len(password)>0:
    print(password[0] + "*"*(len(password)-2) + password[-1])
else:
    print("No password")
