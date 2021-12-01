from rich import print

with open('input', 'r') as f:
    data = [int(line) for line in f.read().splitlines()]

count = 0

for index, depth in enumerate(data):
    if depth > data[index - 1]:
        count += 1

print(f'Puzzle one: {count}')
print(f'Puzzle two: ---')