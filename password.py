password = raw_input('Enter password: ')
print(password[0] + "*"*(len(password)-2) + password[-1])
