from rich import print

with open("input", "r") as f:
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

bits = [
    bit01,
    bit02,
    bit03,
    bit04,
    bit05,
    bit06,
    bit07,
    bit08,
    bit09,
    bit10,
    bit11,
    bit12,
]

gamma = []  # Most Common
epsilon = []  # Least Common


for line in data:
    for position, bit in enumerate(line):
        if position == 0:
            bit01.append(bit)
        if position == 1:
            bit02.append(bit)
        if position == 2:
            bit03.append(bit)
        if position == 3:
            bit04.append(bit)
        if position == 4:
            bit05.append(bit)
        if position == 5:
            bit06.append(bit)
        if position == 6:
            bit07.append(bit)
        if position == 7:
            bit08.append(bit)
        if position == 8:
            bit09.append(bit)
        if position == 9:
            bit10.append(bit)
        if position == 10:
            bit11.append(bit)
        if position == 11:
            bit12.append(bit)


for bit in bits:
    if bit.count("1") <= 500:
        epsilon.append("1")
        gamma.append("0")
    else:
        epsilon.append("0")
        gamma.append("1")

epsilon = int("".join(epsilon), 2)
gamma = int("".join(gamma), 2)
power = epsilon * gamma


o2 = []
co2 = []


print(f"Puzzle one: {power}")
# print(f'Puzzle two: {life_support}')
