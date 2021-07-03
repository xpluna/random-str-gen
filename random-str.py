import random

chars = list(
    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()`~-_=+\,.<>/?;:\'"')
strs = []

classif = int(input(
    '[1] Generate string with manual lengths?\n[2] Make the program generate strings with number\n    of outputs you provide?\n\n>>> '))

if classif == 1:

    print("\nEnter 'Q' to quit\n\nOutput Length (Positive counting number)")

    while True:
        n = input("\n>>> ")

        if n.lower().strip() == 'q':
            break

        else:
            i = 0
            message = ''
            while i != int(n):
                message += random.choice(chars)
                i += 1

            print(message)
            strs.append(message)

    with open('strings.txt', 'w') as fobj:
        for string in strs:
            fobj.write(f'{string}\n\n')

elif classif == 2:
    
    Os = int(input('\nNumber of strings to export\n>>> '))
    Ls = int(input('\nLength of each string\n>>> '))
    i = 0
    
    while Os != 0:
        i = 0
        message = ''
        while i != Ls:
            message += random.choice(chars)
            i += 1
        strs.append(message)
        Os -= 1
    
    with open('strings.txt', 'w') as fobj:
        for string in strs:
            fobj.write(f'{string}\n\n')
