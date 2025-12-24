from math import prod


total = 0
lines, ops = [], []
operands = { '+': lambda x: sum(x), '*': lambda x: prod(x) }

with open('adventOfCodeDay6FormattedValues.txt', 'r') as f:
    lines = [ln.split() for ln in f]
    ops = lines[4]
    lines = [map(int, ln) for ln in lines[:4]]

lines = list(zip(*lines))

for i in range(len(lines)):
    total += operands[ops[i]](list(lines[i]))

print(total)