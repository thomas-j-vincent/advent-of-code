from math import prod

total = 0
lines, ops = [], []
operands = { '+': lambda x: sum(x), '*': lambda x: prod(x) }

with open('Day6Input.txt', 'r') as file:
    lines = [line.split() for line in file]
    ops = lines[4]
    lines = [map(int, line) for line in lines[:4]]

lines = list(zip(*lines))

for i in range(len(lines)):
    total += operands[ops[i]](list(lines[i]))

print(total)