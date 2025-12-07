with open("AdventOfCodeDay5Range.txt") as f:
    between = [line.strip() for line in f]

for r in between:
    start, end = map(int, r.split("-"))
    print(r, "size:", end - start + 1)