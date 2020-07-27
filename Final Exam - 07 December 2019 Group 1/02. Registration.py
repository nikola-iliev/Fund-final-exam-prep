import re
pattern = r'U\$[A-Z][a-z]{2,}U\$P@\$[A-Za-z]{5,}[0-9]+P@\$'

number = int(input())

input_data = []

successful_registrations = 0

for _ in range(number):
    line = input()
    input_data.append(line)

for text in input_data:
    match = re.match(pattern, text)

    if match is None:
        print('Invalid username or password')
        continue

    match = match[0]
    email = match.split('P@$')
    full_username = email[0].split('U$')
    username = full_username[1]
    password = email[1]

    print('Registration was successful')
    print(f'Username: {username}, Password: {password}')
    successful_registrations += 1

print(f'Successful registrations: {successful_registrations}')

# 3
# U$MichaelU$P@$asdqwe123P@$
# U$NameU$P@$PasswordP@$
# U$UserU$P@$ad2P@$
#
# 2
# U$TommyU$P@$asdqwe123P@$
# Sara 1232412

