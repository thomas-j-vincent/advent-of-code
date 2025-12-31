# Load ranges
with open("Day5Range.txt") as f:
    ranges = []
    for line in f:
        start, end = map(int, line.strip().split("-"))
        ranges.append((start, end))

# Step 1: sort by starting value
ranges.sort()

# Step 2: merge overlaps
merged = []
current_start, current_end = ranges[0]

for start, end in ranges[1:]:
    if start <= current_end + 1:  # overlap or touching
        current_end = max(current_end, end)
    else:
        merged.append((current_start, current_end))
        current_start, current_end = start, end

merged.append((current_start, current_end))

# Step 3: calculate total size without iterating every number
total = sum(end - start + 1 for start, end in merged)

print("total:", total)
