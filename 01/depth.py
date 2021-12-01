from rich import print

with open('input', 'r') as f:
    data = [int(line) for line in f.read().splitlines()]

# Puzzle 1
count1 = 0
for index, depth in enumerate(data):
    if depth > data[index - 1]:
        count1 += 1

# Puzzle 2
count2 = 0
groups = []
for index, depth in enumerate(data):
    if index <= len(data) - 3:
        group = sum([depth, data[index+1], data[index+2]])
        groups.append(group)

for index, group in enumerate(groups):
    if group > groups[index - 1]:
        count2 +=1


print(f'Puzzle one: {count1}')
print(f'Puzzle two: {count2}')