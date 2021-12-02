from rich import print

with open('input', 'r') as f:
    data = f.read().splitlines()


# Puzzle 1
positions = []
for e in data:
    position = {e.split()[0]:e.split()[1]}
    positions.append(position)

horizontal = 0
depth = 0
for position in positions:
    for k, v in position.items():
        if k == 'forward':
            horizontal += int(v)
        if k == 'up':
            depth -= int(v)
        if k == 'down':
            depth += int(v)

final1 = horizontal * depth

# Puzzle 2
positions = []
for e in data:
    position = {e.split()[0]:e.split()[1]}
    positions.append(position)

horizontal = 0
depth = 0
aim = 0
for position in positions:
    for k, v in position.items():
        if k == 'forward':
            horizontal += int(v)
            depth += aim * int(v)
        if k == 'up':
            aim -= int(v)
        if k == 'down':
            aim += int(v)

final2 = horizontal * depth

print(f'Puzzle one: {final1}')
print(f'Puzzle two: {final2}')