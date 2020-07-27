import re

username_pattern = r'U\$([A-Z][a-z]{2,})U\$'
password_pattern = r'P@\$([A-Za-z]{5,}[0-9]+P)@\$'
pattern = fr'{username_pattern}{password_pattern}'

successful_registrations = 0

number = int(input())

for _ in range(number):
    line = input()
    match = re.match(pattern, line)

    if match is None:
        print('Invalid username or password')
        continue

    successful_registrations += 1

    print('Registration was successful')
    print(f'Username: {match[1]}, Password: {match[2]}')

print(f'Successful registrations: {successful_registrations}')