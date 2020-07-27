line = input()

users = {}

while line != "Statistics":
    line = line.split('->')
    command = line[0]
    username = line[1]

    if command == 'Add':
        if username in users.keys():
            print(f'{username} is already registered')
        else:
            users[username] = []

    elif command == "Send":
        email = line[2]
        users[username].append(email)
    elif command == 'Delete':
        if username in users.keys():
            del users[username]
        else:
            print(f'{username} not found!')

    line = input()

users = dict(sorted(users.items(),key=lambda x: (-len(x[1]), x[0])))

print(f'Users count: {len(users.keys())}')
for name, email in users.items():
    print(name)
    for i in email:
        print(f' - {i}')

# Add->Mike
# Add->George
# Send->George->Hello World
# Send->George->Some random test mail
# Send->Mike->Hello, do you want to meet up tomorrow?
# Send->George->It would be a pleasure
# Send->Mike->Another random test mail
# Statistics

# Add->Mike
# Add->George
# Send->George->Hello World
# Send->George->Your loan is overdue
# Add->Mike
# Send->Mike->Hello, do you want to meet up tomorrow?
# Delete->Peter
# Send->George->I'm busy
# Send->Mike->Another random test mail
# Delete->George
# Statistics


