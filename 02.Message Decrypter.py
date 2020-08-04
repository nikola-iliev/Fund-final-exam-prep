import re
pattern = r'(\$|\%)([A-Z][a-z]{2,})\1: (\[[0-9]+\])\|(\[[0-9]+\])\|(\[[0-9]+\])\|$'

n = int(input())

for _ in range(n):
    line = input()
    match = re.match(pattern, line)

    if match is None:
        print('Valid message not found!')
        continue
    else:
        tag = match[2]
        message = ''
        for i in range(3, 6):
            numbers = ''
            number = match[i]
            for digit in number:
                if digit.isdigit():
                    numbers += digit
            letter = chr(int(numbers))
            message += letter

    print(f'{tag}: {message}')

