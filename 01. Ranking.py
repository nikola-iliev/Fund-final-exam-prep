line = input()

contests = {}
user_contest_points = {}
total_points = {}

while line != "end of contests":
    tokens = line.split(':')
    contest = tokens[0]
    password = tokens[1]

    if contest not in contests:
        contests[contest] = password

    line = input()

line = input()

while line != 'end of submissions':
    tokens = line.split('=>')
    contest = tokens[0]
    current_password = tokens[1]
    username = tokens[2]
    points = int(tokens[3])

    if contest in contests and contests[contest] == current_password:
        if username not in user_contest_points:
            user_contest_points[username]= {}
            user_contest_points[username][contest] = points
        if username in user_contest_points:
            if contest not in user_contest_points[username]:
                user_contest_points[username][contest] = points
            if user_contest_points[username][contest] < points:
                user_contest_points[username][contest] = points

    line = input()

keys = list(user_contest_points.values())
#print(user_contest_points)
#print(keys)
for name in user_contest_points.keys():
    res = []
    for contest, points in user_contest_points[name].items():
        res.append(points)
        total_points_name = sum(res)
        total_points[name] = total_points_name

#print(total_points)
#total_points = sorted(total_points.values(), reverse=True)
#print(total_points[0])
total_points = sorted(total_points.items(), key=lambda x: (-x[1], x[0]))
#print(f'Total points:{total_points}')
print(f'Best candidate is {total_points[0][0]} with total {total_points[0][1]} points.')
#print(f'ucs: {user_contest_points}')
sorted_users = dict(sorted(user_contest_points.items(), key=lambda n: n[0]))
#print(sorted_users)
print('Ranking:')
new_value = []
for key, value in sorted_users.items():
    print(f'{key}')
    #print(f'{value}')
    #for k,v in value.items():
        #print(f'{k}')
        #print(f'{v}')
    sorted_value = dict(sorted(value.items(), key=lambda x: -x[1]))
    #print(sorted_value)
    for k,v in sorted_value.items():
        print(f'#  {k} -> {v}')

# Part One Interview:success
# Js Fundamentals:Pesho
# C# Fundamentals:fundPass
# Algorithms:fun
# end of contests
# C# Fundamentals=>fundPass=>anya=>350
# Algorithms=>fun=>anya=>380
# Part One Interview=>success=>Nikola=>120
# Java Basics Exam=>pesho=>Petkan=>400
# Part One Interview=>success=>anya=>220
# OOP Advanced=>password123=>BaiIvan=>231
# C# Fundamentals=>fundPass=>anya=>250
# C# Fundamentals=>fundPass=>Nikola=>200
# Js Fundamentals=>Pesho=>anya=>400
# end of submissions

# Java Advanced:funpass
# Part Two Interview:success
# Math Concept:asdasd
# Java Web Basics:forrF
# end of contests
# Math Concept=>ispass=>Monika=>290
# Java Advanced=>funpass=>Simona=>400
# Part Two Interview=>success=>Drago=>120
# Java Advanced=>funpass=>Petyr=>90
# Java Web Basics=>forrF=>Simona=>280
# Part Two Interview=>success=>Petyr=>0
# Math Concept=>asdasd=>Drago=>250
# Part Two Interview=>success=>Simona=>200
# end of submissions

