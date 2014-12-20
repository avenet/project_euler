f = open("names.txt")

people_names = []

def append_names(line):
    global people_names
    people_names = [x[1:-1] for x in line.split(",")]

for line in f:
    append_names(line)
    

def score(name, position):
    return position * sum([ord(c)-64 for c in name])

people_names.sort()

total_sum = 0

for index, name in enumerate(people_names):
    total_sum += score(name, index+1)
    
print total_sum