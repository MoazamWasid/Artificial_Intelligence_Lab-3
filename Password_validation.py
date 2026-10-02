
password = input("Enter your password: ")
valid = True
s_count = 0

if (len(password) < 6 or len(password) > 16):
    print("Password must be at least 6 characters and at most 16 characters long.")   
    valid = False

for char in password:
    if 'a' <= char <= 'z':
        break
else:
    print("Password must contain at least one lowercase letter.")
    valid = False

for char in password:
    if 'A' <= char <= 'Z':
        break
else:
    print("Password must contain at least one uppercase letter.")
    valid = False

for char in password:
    if '0' <= char <= '9':
        break
else:
    print("Password must contain at least one digit(0-9).")
    valid = False

for char in password:
    if char == '$' or char == '#' or char == '@':
        s_count= s_count + 1

if s_count < 2:
    print("Password must contain at least two special character ($, #, @).")
    valid = False

if valid:
    print("Valid Password") 
else:
    print("Invalid Password")



