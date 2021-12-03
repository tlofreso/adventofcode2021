from rich import print

with open('input', 'r') as f:
    data = f.read().splitlines()

bit01 = []
bit02 = []
bit03 = []
bit04 = []
bit05 = []
bit06 = []
bit07 = []
bit08 = []
bit09 = []
bit10 = []
bit11 = []
bit12 = []

for line in data:
    bit01.append(line[0])
    bit02.append(line[1])
    bit03.append(line[2])
    bit04.append(line[3])
    bit05.append(line[4])
    bit06.append(line[5])
    bit07.append(line[6])
    bit08.append(line[7])
    bit09.append(line[8])
    bit10.append(line[9])
    bit11.append(line[10])
    bit12.append(line[11])

print(bit04.count('1'))