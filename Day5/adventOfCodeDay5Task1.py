with open("AdventOfCodeDay5Range.txt") as f:
    between = [line.strip() for line in f]

with open("AdventOfCodeDay5FormattedValues.txt") as file:
    numbers = [int(line.strip()) for line in file]

fresh = set()   # avoid duplicates

for r in between:
    start, end = map(int, r.split("-"))

    for number in numbers:
        if start <= number <= end:
            fresh.add(number)

print("total:", len(fresh))