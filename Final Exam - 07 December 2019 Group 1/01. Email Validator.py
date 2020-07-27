email = input()

line = input()

while line != 'Complete':
    args = line.split()
    command = args[0]
    if line == 'Make Upper':
        email = email.upper()
        print(email)

    elif line == 'Make Lower':
        email = email.lower()
        print(email)

    elif command == 'GetDomain':
        count = int(args[1])
        print(email[-count:])

    elif line == 'GetUsername':
        index = email.find('@')
        if index == -1:
            print(f'The email {email} doesn\'t contain the @ symbol.')
        else:
            print(email[:index])

    elif command == 'Replace':
        char = args[1]
        if char in email:
            email = email.replace(char, '-')
            print(email)
        else:
            print(email)

    elif line == 'Encrypt':
        for char in email:
            print(ord(char), end=' ')

    line = input()

# Mike123@somemail.com
# Make Upper
# GetDomain 3
# GetUsername
# Encrypt
# Complete
