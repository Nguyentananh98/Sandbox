MINIMUM_LENGTH = 8

password = input("Please enter your password: ")
while len(password) < MINIMUM_LENGTH:
    print("THe password length must be 8 letters or more!")
    password = input("Please enter your password: ")

for i in range(len(password)):
    print('*', end='')
